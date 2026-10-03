# Start with the Combined Corpus Research AI

Use your usual AI assistant to explore the corpus collection, find relevant evidence, and prepare reproducible research. Start with one file. Add the corpus evidence relevant to your question when you are ready.

## 1. Download the starter

**[Download the starter text file](https://github.com/hawkinsnick/Linear-A/raw/refs/heads/main/combined-ai-skill/downloads/Combined-Corpus-Research-Starter.txt)**

Save it as `Combined-Corpus-Research-Starter.txt`. You do not need to open or edit it. If your browser displays the text instead of downloading it, use **Save page as** or **Save link as**. On a phone or tablet, use the browser's share/save control to save it to your files.

Prefer a folder containing the instructions and their original supporting files? [Download the ZIP edition](downloads/README.md), then extract it. Windows: right-click the ZIP and choose **Extract All**. macOS: double-click the ZIP. On iPhone or iPad, tap the ZIP in Files. The starter text file is inside the extracted folder.

The starter contains the master instructions, corpus directory, comparison rules, prompts, and licensing notices. Inscription records, images, member corpus evidence, and an AI account are supplied separately.

## 2. Add the file to your AI

Open a conversation in an AI assistant that can read uploaded text files. Use its file attachment or upload control to add `Combined-Corpus-Research-Starter.txt`. Upload the extracted text file rather than the ZIP unless your assistant explicitly supports opening archives.

For ongoing work, you can keep the file and your related research sources in a project. In ChatGPT, project sources and instructions are shared across that project's chats; start your research conversation inside that project. You can also begin in an ordinary chat. File controls and availability vary by product and account.

Uploading supplies research instructions as context. Follow the activation prompt below so the assistant knows how you want to use them.

## 3. Send this first message

Copy the following message and replace the words in square brackets with your topic:

> Use the uploaded Combined-Corpus-Research-Starter.txt as the research instructions for this conversation, within your platform's rules. First confirm which uploaded files you can actually read, the starter snapshot, and how many corpus projects are registered. I am researching [your topic]. Which projects are relevant, what evidence files would we need, and what is one useful first question? Distinguish the starter directory from evidence you have actually inspected. Do not invent readings or citations.

Expect a short orientation, the relevant corpus names, and a clear explanation of any evidence that still needs to be supplied. If the assistant reports inscription findings immediately without identifying accessible evidence, ask it to complete the access check first.

## 4. Add evidence for your question

Choose the relevant corpus in the [corpus download directory](CORPUS-DOWNLOADS.md). Start with one corpus; add others when your question requires comparison.

**If your assistant can read GitHub files:** give it the corpus repository link and ask it to read the individual research instructions, authority profile, generated bundle index, and source-state file. It should report the files and version it successfully accessed before using the corpus. A link alone does not establish access.

**If your assistant needs uploads:** download the corpus ZIP from the directory and extract it. Open its `ai-skill` folder. Upload `SKILL.md`, `references/authority-profile.json`, `generated/research-bundle-index.json`, and `generated/source-state.json` when present. Then ask:

> I want to investigate [your question]. Read the uploaded corpus instructions and index. Tell me exactly which evidence files to upload next, using their folder paths, and what each will let us examine. Report any missing instructions or source-state files. Do not present index entries as inscription evidence.

The assistant should select files for your question, rather than ask you to upload the whole collection. The index is a list of evidence files; those files must also be accessible. If an upload control does not accept a file type, ask which supported text or data export preserves the fields needed for the task. Do not silently discard uncertainty, source identifiers, or licensing information to make an upload work.

Once the evidence is available, ask your question normally. [Research prompts](PROMPTS.md) provide starting points for source tracing, edition comparison, coverage, and reproducibility.

## Know when the setup worked

A useful response identifies the files it read and separates recorded evidence, source assertions, interpretations, and unknowns. It gives record identifiers and source locators where available. An uploaded file name, a public URL, or a confident answer is not proof that the underlying evidence was inspected.

Save the corpus version or commit, relevant file names, and your question with any result you intend to cite. The [research workflow](QUICKSTART.md) explains the evidence and comparison checks in more detail.

## When something gets in the way

| What you see | What to do |
|---|---|
| The download opens in the browser | Save the text file, or use the ZIP edition. |
| The assistant cannot find the starter | Attach it again in this chat or project, then ask it to identify a section it can read. |
| The assistant only sees a ZIP file | Extract it and attach the starter text file. |
| A repository link cannot be read | Use the corpus ZIP and upload the files selected for your question. |
| A generated member index or source-state file is absent | Ask the assistant to report the missing bundle and use accessible canonical files without claiming bundle validation. |
| The response says evidence is missing | Ask for the exact file paths or source acquisition needed; supply those files before drawing conclusions. |
| A comparison is BLOCKED | Ask what specific evidence or methodological check would make it supportable. Descriptive work may still be possible. |
| A file or corpus has changed | Download the current file again. Ask the assistant to identify the replacement it read; retain the earlier snapshot for prior results. |

The master starter is maintained separately from member corpus evidence. A saved copy is a snapshot, and uploads do not automatically refresh from GitHub. Its snapshot identifier records the packaged instruction state. Each participating corpus has its own evidence version and review status.

## Sharing and citation

Cite the underlying corpus and publication for research claims, with the version or commit and record/source locators where practical. You may also name the Combined Corpus Research AI as part of your method; it is not the inscription's evidentiary source.

The included licensing notices describe the project-original starter material. Member corpora and upstream sources retain their own terms. Follow your institution's policies when uploading unpublished, personal, or otherwise restricted research material to an AI service.

This directory covers the corpus collection, including the Egyptian Hieroglyphic Corpus as a comparative/control member. A future Egyptian camera/OCR application is a separate software product and must not be treated as scholarly corpus authority. LightroomIsSlow is separate from the corpus fleet.

## Platform guidance

The instructions are vendor-neutral. Use your assistant's supported file/context controls and the same access-check prompt. Product details change; current ChatGPT guidance is available in [Projects and chats](https://learn.chatgpt.com/docs/projects) and [Use ChatGPT](https://learn.chatgpt.com/docs/use-chatgpt) (checked 2 October 2026).
