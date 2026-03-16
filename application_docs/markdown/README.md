# Markdown -> PDF workflow (Banff application)

This folder is the Word-free source for application documents.

## Files
- `proposal.md`: editable source text for the Banff proposal
- `cover_letter.md`: editable source text for the Banff cover letter
- `portfolio-docs.css`: shared print styling aligned to the portfolio visual language
- `render_pdf.sh`: render script using `pandoc` + `weasyprint`
- `output/`: generated PDFs

## Render proposal PDF
```bash
application_docs/markdown/render_pdf.sh \
  application_docs/markdown/proposal.md \
  application_docs/markdown/output/Rode_Banff_Proposal_from_md.pdf \
  application_docs/markdown/proposal-header.css
```

## Render cover letter PDF
```bash
application_docs/markdown/render_pdf.sh \
  application_docs/markdown/cover_letter.md \
  application_docs/markdown/output/Rode_Banff_Cover_Letter_from_md.pdf
```

## Render a different markdown file
```bash
application_docs/markdown/render_pdf.sh /path/to/input.md /path/to/output.pdf
```

## Edit cycle
1. Edit `proposal.md` or `cover_letter.md`
2. Run `application_docs/markdown/render_pdf.sh`
3. Open the updated PDF in `output/`
