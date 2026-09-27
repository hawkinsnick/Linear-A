#!/usr/bin/env python3
"""Minimal OCaml Marshal decoder for SigLA's published database.js payload."""
from __future__ import annotations
import re, struct
from dataclasses import dataclass
from pathlib import Path
from typing import Union

MarshalValue = Union["Block", int, str, float, list[float]]

@dataclass
class Block:
    tag: int
    fields: list[MarshalValue | None]

class Unmarshal:
    def __init__(self, buf: bytes, offset: int = 0) -> None:
        self.buf, self.i, self.objects = buf, offset, []
    def u8(self): v=self.buf[self.i]; self.i+=1; return v
    def u16(self): v=struct.unpack_from(">H",self.buf,self.i)[0]; self.i+=2; return v
    def u32(self): v=struct.unpack_from(">I",self.buf,self.i)[0]; self.i+=4; return v
    def i8(self): v=struct.unpack_from(">b",self.buf,self.i)[0]; self.i+=1; return v
    def i16(self): v=struct.unpack_from(">h",self.buf,self.i)[0]; self.i+=2; return v
    def i32(self): v=struct.unpack_from(">i",self.buf,self.i)[0]; self.i+=4; return v
    def i64(self): v=struct.unpack_from(">q",self.buf,self.i)[0]; self.i+=8; return v
    def string(self,n): s=self.buf[self.i:self.i+n]; self.i+=n; return s.decode("utf-8","replace")
    def header(self):
        if self.u32()!=0x8495A6BE: raise ValueError("bad OCaml Marshal magic")
        data_len=self.u32(); objects=self.u32(); self.u32(); self.u32()
        return data_len,objects
    def shared(self,back): return self.objects[len(self.objects)-back]
    def value(self):
        code=self.u8()
        if code>=0x80:
            tag=code&0x0F; size=(code>>4)&0x07; fields=[None]*size
            block=Block(tag,fields); self.objects.append(block)
            for j in range(size): fields[j]=self.value()
            return block
        if code>=0x40: return code&0x3F
        if code>=0x20:
            s=self.string(code&0x1F); self.objects.append(s); return s
        if code==0x00:return self.i8()
        if code==0x01:return self.i16()
        if code==0x02:return self.i32()
        if code==0x03:return self.i64()
        if code==0x04:return self.shared(self.u8())
        if code==0x05:return self.shared(self.u16())
        if code==0x06:return self.shared(self.u32())
        if code==0x08:
            hdr=self.u32(); tag=hdr&0xFF; size=hdr>>10; fields=[None]*size
            block=Block(tag,fields); self.objects.append(block)
            for j in range(size): fields[j]=self.value()
            return block
        if code==0x09:
            s=self.string(self.u8()); self.objects.append(s); return s
        if code==0x0A:
            s=self.string(self.u32()); self.objects.append(s); return s
        if code==0x0B:
            v=struct.unpack_from(">d",self.buf,self.i)[0]; self.i+=8; self.objects.append(v); return v
        if code==0x0C:
            v=struct.unpack_from("<d",self.buf,self.i)[0]; self.i+=8; self.objects.append(v); return v
        if code in (0x0D,0x0E):
            n=self.u8(); fmt=">" if code==0x0D else "<"; v=list(struct.unpack_from(fmt+"d"*n,self.buf,self.i)); self.i+=8*n; self.objects.append(v); return v
        if code in (0x07,0x0F):
            n=self.u32(); fmt=">" if code==0x0F else "<"; v=list(struct.unpack_from(fmt+"d"*n,self.buf,self.i)); self.i+=8*n; self.objects.append(v); return v
        if code in (0x12,0x18,0x19):
            end=self.buf.index(b"\x00",self.i); ident=self.buf[self.i:end].decode("ascii","replace"); self.i=end+1
            if ident=="_i": v=self.i32(); self.objects.append(v); return v
            if ident=="_j": v=self.i64(); self.objects.append(v); return v
            raise ValueError(f"unsupported custom value {ident!r}")
        raise ValueError(f"unknown OCaml Marshal opcode {code:#x}")

def _unescape_js(body: str) -> bytes:
    out=bytearray(); i=0
    while i<len(body):
        if body[i]=="\\":
            j=i
            while j<len(body) and body[j]=="\\": j+=1
            if j+2<len(body) and body[j:j+3].isdigit():
                out.append(int(body[j:j+3])&255); i=j+3; continue
            out.extend(b"\\"*((j-i)//2)); i=j; continue
        out.append(ord(body[i])&255); i+=1
    return bytes(out)

def load_database(path: str|Path):
    src=Path(path).read_text(encoding="utf-8",errors="replace"); result={}
    for name in ("signs","data"):
        m=re.search(r"var\s+"+name+r"\s*=\s*'(.*?)';",src,re.S)
        if not m: continue
        raw=_unescape_js(m.group(1)); start=raw.find(b"\x84\x95\xa6\xbe")
        if start<0: raise ValueError(f"no Marshal header for {name}")
        u=Unmarshal(raw,start); u.header(); result[name]=u.value()
    return result
