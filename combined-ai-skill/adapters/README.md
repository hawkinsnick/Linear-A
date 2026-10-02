# AI Platform Adapters

The 1.0 core is vendor-neutral. Platform adapters must not weaken SKILL.md.

## ChatGPT
Upload the combined skill plus relevant member AI bundles to a project/workspace or conversation that supports files. Instruct the model to use `combined-ai-skill/SKILL.md` as governing research instructions and each member `ai-skill/SKILL.md` as the native authority.

## Claude
Place the same governing files in project knowledge/instructions. Keep the registry and member bundles available to the project.

## Gemini
Provide the same files in the relevant workspace/context mechanism and identify SKILL.md as governing instructions.

## Local/other models
Use SKILL.md as system/project instructions when supported. Otherwise prepend it to the research session and provide the registry plus required member bundles.

Platform behavior may differ. Passing the structural package validation does not certify a model's adherence; model-specific behavioral evaluation remains necessary.
