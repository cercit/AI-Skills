---
name: diary
description: |
  Process scanned handwritten diary or notebook pages. Reads handwritten PDFs/images,
  transcribes them using Claude's vision, adds short context and links, and saves clean
  markdown notes to your notes vault. Tracks processed files to avoid duplicates.
  Use when the user types /diary or says "process my diary", "read my diary pages".
---

# Diary processor

You process handwritten diary scans into clean, linked markdown notes.

## Settings (ask once, then remember)

- **Input folder:** where the scans land, e.g. `<notes>/Diary_Photos`
- **Output folder:** where the notes go, e.g. `<notes>/Vault/Diary`
- **Tracker file:** `<output folder>/processed.txt`
- **After processing:** `move` (default: move originals into `<input folder>/processed/`) or `delete` (only if the user explicitly chooses it)

Never guess these paths. If they are not set, ask.

## Procedure

1. **Scan for new files.** Read `processed.txt` to get the list of already-processed
   filenames. Then list the input folder for `*.pdf`, `*.png`, `*.jpg`, `*.jpeg`.
   Filter out any already in `processed.txt`. If nothing new, tell the user and stop.

2. **For each new file:**

   a. **Extract pages.** If PDF, use Python + PyMuPDF to extract each page as a
      PNG image to a temporary folder (200 DPI). If already an image, use directly.

   b. **Read the handwriting.** Open each extracted image with the file-reading tool;
      Claude's vision will see the handwritten text. Transcribe EVERYTHING visible:
      headings, bullet points, diagrams (describe them), underlined words, arrows, margin notes.

   c. **Build the markdown.** Structure the transcription into clean markdown:
      - Title: derive from the content (topic/date visible on the page)
      - Add YAML frontmatter: `date`, `source_file`, `pages`, `topics` (tags)
      - Preserve the author's structure: if they wrote bullets, keep bullets;
        if they drew a flowchart, describe it or render as a mermaid diagram
      - Add `## Context` section: briefly explain any frameworks, terms, or concepts
        mentioned (e.g., if MoSCoW is written, add a one-liner on what it is)
      - Add `## Links` section: link to related notes in the vault if relevant
        (e.g., course notes → link to the course folder)

   d. **Save.** Write to `<output folder>/YYYY-MM-DD-<slug>.md` where the date comes
      from the scan filename or content, and slug is a short kebab-case topic label.
      If the date isn't clear, use today's date.

   e. **Track.** Append the source filename to `processed.txt`.

   f. **Tidy up.** Only after the markdown is saved and tracked: move the original into
      `<input folder>/processed/`, or delete it if the user chose `delete`.

3. **Summary.** After processing all files, print a short summary:
   - How many files processed
   - List of output files created (as clickable file links)
   - Any pages that were hard to read (flag for user review)

## Quality rules

- Transcribe faithfully: don't invent content that isn't on the page.
- If handwriting is ambiguous, write `[unclear: best guess?]` inline.
- Ignore bleed-through text from the other side of the page.
- Diagrams: describe layout and connections; use mermaid if it's a clear flowchart.
- Keep markdown clean: no excessive headers, no boilerplate filler.
- Diary pages are private: never send their content anywhere outside the user's own folders.

## Output template

```markdown
---
date: YYYY-MM-DD
source_file: "original filename.pdf"
pages: 1
topics: [topic1, topic2]
---

# Title derived from content

[Transcribed content here]

## Context

- **Term:** Brief explanation

## Links

- Related: [Note title](../path/to/note.md)
```
