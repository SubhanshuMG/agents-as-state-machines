# Stop building agents like prompts. Build them like state machines.

> Part of **The Intelligent Infrastructure Playbook**, a 36-article series on platform, AI, and
> security engineering for 2026.

**Category:** AI · LLMOps
**Slug:** `agents-as-state-machines`
**Author:** Subhanshu Mohan Gupta
**Canonical:** https://blogs.subhanshumg.com/agents-as-state-machines

---

## TL;DR

Prompt-chained agents fail non-deterministically. State-machine agents with explicit transitions, retries, and compensations survive production.

## What's in this repo

- [`article.md`](./article.md): the full essay, Hashnode-compatible
  front-matter, ready to publish.
- [`references.md`](./references.md): primary sources and further
  reading.
- [`diagrams/`](./diagrams/): Mermaid diagrams (`.mmd`) and the cover
  image (`cover.png`).
- [`code/`](./code/): runnable snippets, manifests, and helper
  scripts referenced from the article.
- [`publish.md`](./publish.md): how this article is published and
  cross-posted.

## Tags

`agents`, `state-machines`, `reliability`

## Quickstart

```bash
# Render the cover (requires Pillow + the DejaVu / Poppins fonts).
# Run from the *main* playbook repo:
#   git clone git@github.com:SubhanshuMG/The-Intelligent-Infrastructure-Playbook.git
#   python3 tools/generate_all_covers.py B06
#
# The rendered cover is copied here as diagrams/cover.png.

# Render the diagrams (requires mermaid-cli).
for f in diagrams/*.mmd; do
    mmdc -i "$f" -o "${f%.mmd}.svg" -t dark -b transparent
done
```

## License

- **Prose (article.md, references.md, diagrams/*.md):**
  [Creative Commons Attribution 4.0 International](./LICENSE-prose)
  (CC BY 4.0). Reuse freely with attribution.
- **Code (code/*, any scripts):** [MIT License](./LICENSE-code).
- See [`LICENSE`](./LICENSE) for the combined notice.

## Citation

See [`CITATION.cff`](./CITATION.cff) for machine-readable citation
metadata.

---

[The Intelligent Infrastructure Playbook](https://blogs.subhanshumg.com) · by [Subhanshu Mohan Gupta](https://blogs.subhanshumg.com) · https://blogs.subhanshumg.com
