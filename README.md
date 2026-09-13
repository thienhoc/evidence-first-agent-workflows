<!-- WI-REPOSITORY-LOCATION -->
**Legacy / predecessor of Wi Amis.** This repository preserves the earlier product and its license. The imported source and history now live at [Wi Amis legacy/evidence-first-agent-workflows](https://github.com/Hazumi-Lab/wi-amis/tree/main/legacy/evidence-first-agent-workflows); that destination is private and requires access. Instructions below describe this historical source, not the current Wi Amis runtime. Do not infer that this old repository is the active development target.
<!-- END-WI-REPOSITORY-LOCATION -->

<p align="right"><img src="assets/wi-studio-logo-black.svg" alt="Wi Studio" width="88"></p>

# Evidence-first Agent Workflows — Wi Studio Open Lab

Small, tool-neutral contracts for research and coding workflows that need provenance, checkpoints and honest evidence boundaries.

## Included

- `capsule.json`: the task, source boundary, expected output and evidence ceiling.
- `checkpoint.json`: a resumable checkpoint with explicit state and next action.
- `execution-record.json`: the machine-readable result, validation status and artifact list.
- `tools/validate_records.py`: a dependency-free validator for the three records.
- Examples that are safe to copy into a new project.

## Quickstart

```bash
python3 tools/validate_records.py examples
```

Expected result:

```text
PASS: 3 records validated; no duplicate artifact IDs.
```

## Design rules

1. A proposal is not implementation evidence.
2. A test result names the command, environment and artifact that produced it.
3. A checkpoint can resume work without relying on hidden chat context.
4. Private paths, credentials and personal data never belong in a public record.

The contracts are intentionally small so they can be used from a shell script, a GitHub Action or another agent runtime.

## License and brand

Code is Apache-2.0. Documentation is CC BY 4.0. The Wi Studio artwork in `assets/` is a brand asset and is not covered by either license.

**Wi Studio Open Lab · by Wi**
