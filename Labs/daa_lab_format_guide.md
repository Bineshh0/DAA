# DAA Lab PDF Generator Rules

This document serves as a memory persistence file to resume DAA lab generation using the exact approved format.

## The Golden Standard Script
The approved formatting structure has been perfectly implemented in:
`c:\Users\V16\.gemini\antigravity\scratch\5th sem\DAA\Labs\generate_daa_lab8_kruskal.py`

When working on upcoming lab assignments, copy or modify that exact script to generate the PDFs for other labs.

## Approved Formatting Rules
- **Direct PDF Generation**: Use `reportlab` in Python to generate the final PDF directly. No HTML-to-PDF translations.
- **Font & Size**: **Times New Roman** must be used across the *entire* document. 
	- Section Headings (e.g., Theory, Algorithm, Source Code): **Bold, 12pt**.
	- Body Content / Lines: **Regular, 11pt**.
- **Document Structure**:
	1. **Title**: Uses format "Lab X: [Title]". (No horizontal divider lines, no large university headers or metadata tables - just jump straight into the title).
	2. **Theory**: Plain text, justified alignment.
	3. **Complexity Table**: Simple clean grid, Times-Bold headers, Times-Roman cells.
	4. **Algorithm**: Plain text flowing naturally (numbered list).
	5. **Pseudocode**: Plain text flowing naturally, respecting indentation.
	6. **Source Code**: Plain text flowing naturally, respecting indentation but preserving exact characters (e.g., `#include`). It should include the student ID `023bscit009_binesh`.
	7. **Conclusion**: Plain text, justified alignment.
- **No Borders/Boxes**: Algorithm, Pseudocode, and Source Code sections must NOT be inside of bounded GUI boxes, grey backgrounds, or tables. They must just flow as plain text within the page margins.
- **Library Requirements**: Make sure you have `reportlab` installed. Code requires `from reportlab.pdfbase.ttfonts import TTFont` to map system TrueType fonts (`times.ttf`, `timesbd.ttf`, `timesi.ttf`).

## Resume Instructions
1. Read this file.
2. Review the reference python script `generate_daa_lab8_kruskal.py`.
3. Process the new lab code and theory exactly according to this style.
