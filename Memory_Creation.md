# Memory File Creation Trigger

When the user inputs `> LEDGER`:

1.  **Determine Next Number:** Search the GitHub repository for the highest existing `memX.md` file, or ask David for the last used number.
2.  **Scan History:** Scan conversation history for verified insights, learnings, or statutory mechanics.
3.  **ENFORCE ATOMICITY:** Each distinct concept, tool, methodology, or statutory mechanism must be its own separate file. Do not combine unrelated learnings into a single session dump file.
4.  **Extract Mechanics:** For statutory mechanisms, extract the specific section, the Layer 3 mechanical causation, and the Layer 4 enforcement reality.
5.  **Generate Files:** Create sequential filenames (e.g., mem8.md, mem9.md).
6.  **Tagging:** Generate appropriate tags for retrieval via GitHub search.
7.  **Linking:** Identify related files for linking in the YAML frontmatter.
8.  **Output:** Output each file as markdown with YAML frontmatter (tags, links) followed by the insight content.
9.  **Format:** Output ONLY the raw Markdown files.

## Automated creation (when the repo is checked out)

Instead of hand-writing files, use the tool, which auto-assigns the next `memN` number and writes valid frontmatter:

```bash
python3 scripts/memory.py remember \
  --title "Concept Title" \
  --tags tag1,tag2,tag3 \
  --link mem5:shares-pattern --link mem29:extends \
  --content "The atomic insight..."
```

The same atomicity, tagging, and linking rules above still apply — one concept per invocation. This is the mechanism the Scepticism Engine's **Memory Gate** calls to capture insights automatically.
