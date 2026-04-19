# Publishing this article

**Primary venue:** Hashnode, https://blogs.subhanshumg.com/agents-as-state-machines
**Canonical URL:** https://blogs.subhanshumg.com/agents-as-state-machines
**Cross-post:** dev.to, LinkedIn, Substack (all with `canonicalUrl`
pointing back to Hashnode).

## Checklist

1. `article.md` front-matter has `canonicalUrl`, `cover`, `tags`,
   and `series` filled in.
2. `diagrams/cover.png` exists (regenerate with
   `python3 tools/generate_all_covers.py B06` from the
   main playbook repo).
3. Every `.mmd` in `diagrams/` has an alt text explaining what the
   figure shows.
4. Every external link in `references.md` is reachable.
5. `code/` snippets have shebangs / module headers where applicable
   and an MIT copyright line at the top.
6. Run the link checker (`.github/workflows/link-check.yml` in the
   main repo) against this folder.
7. Push this folder as its own public repo:
   `github.com/SubhanshuMG/agents-as-state-machines`.
8. Publish on Hashnode. Set the Hashnode post's canonical URL to
   itself if it is the primary venue.

## Cross-posting

When cross-posting to dev.to / LinkedIn / Substack, include a one-line
note at the bottom:

> Originally published on [The Intelligent Infrastructure Playbook](https://blogs.subhanshumg.com/agents-as-state-machines).
