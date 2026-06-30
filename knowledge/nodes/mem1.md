---
tags: [marker, pdf-conversion, command-line, tool, methodology, linux]
links:
  - file: atomicity-constraint.md
    relation: supports-method
  - file: memory-system-architecture.md
    relation: supports-method
---

## Marker PDF Conversion Tool

The marker tool converts PDF documents to markdown while preserving document structure (headings, sections, tables). It is ideal for legislation because it maintains hierarchical structure.

**Installation:**
```bash
pipx install marker-pdf
```

**Command syntax:**
```bash
marker_single /path/to/input.pdf --output_dir /path/to/output/
```

**Critical detail:** The flag uses an underscore (`output_dir`), not a hyphen (`output-dir`). This is a common source of errors.

**Repeated use workflow:**
Save the command template in a text file with placeholder filename, then replace the input filename each time. Example:
```bash
marker_single /home/jdd/Desktop/Bills_Acts/YOUR_PDF_NAME.pdf --output_dir /home/jdd/Desktop/Bills_Acts/MD_Legislation/
```

**For scanned PDFs:** Requires OCR first (Tesseract OCR, Adobe Acrobat, or online OCR services).
