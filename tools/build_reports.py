#!/usr/bin/env python3
import hashlib
import html
import json
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
OUT = ROOT / "public" / "reports"
VERSION = os.environ.get("REHT_REPORT_VERSION", "REHT-v1.0")
SOURCE_COMMIT = os.environ.get("GITHUB_SHA", "local")
PUBLISHED = os.environ.get("REPORT_PUBLISHED_DATE", "2026-09-05")

CSS = """
@page { size: A4; margin: 19mm 18mm 20mm; @bottom-right { content: 'VALO Research · ' counter(page); font-size: 8pt; color: #666; } }
body { font-family: sans-serif; color: #161616; font-size: 10.4pt; line-height: 1.48; }
h1 { font-size: 25pt; margin: 0 0 6mm; }
h2 { font-size: 16pt; margin-top: 8mm; }
h3 { font-size: 12.5pt; margin-top: 6mm; }
p, li { orphans: 3; widows: 3; }
code, pre { font-family: monospace; font-size: 9pt; }
pre { white-space: pre-wrap; background: #f5f5f5; padding: 3mm; border-radius: 2mm; }
blockquote { border-left: 2px solid #999; margin-left: 0; padding-left: 4mm; color: #444; }
table { border-collapse: collapse; width: 100%; font-size: 9pt; }
th, td { border: 1px solid #ccc; padding: 2mm; vertical-align: top; }
.meta { margin: 0 0 12mm; padding: 4mm 0; border-top: 1px solid #bbb; border-bottom: 1px solid #bbb; font-size: 8.5pt; color: #555; }
.cover-note { font-size: 9pt; color: #555; margin-bottom: 8mm; }
a { color: inherit; text-decoration: none; }
"""

INDEX_CSS = """
body{font-family:system-ui,-apple-system,sans-serif;max-width:900px;margin:48px auto;padding:0 20px;color:#171717;line-height:1.5}h1{font-size:32px}a{color:#111}.report{padding:18px 0;border-top:1px solid #ddd}.meta{font-size:13px;color:#666}.top{margin-bottom:32px}
"""

def title_from_md(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else fallback

def render_markdown(md_text: str) -> str:
    import markdown
    return markdown.markdown(md_text, extensions=["extra", "tables", "fenced_code"])

def main() -> None:
    from weasyprint import HTML

    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {"schema": "valo.reht.public-report-manifest.v1", "version": VERSION, "source_commit": SOURCE_COMMIT, "reports": []}

    for src in sorted(REPORTS.glob("*.md")):
        if src.name == "README.md":
            continue
        md = src.read_text(encoding="utf-8")
        title = title_from_md(md, src.stem)
        source_sha = hashlib.sha256(md.encode("utf-8")).hexdigest()
        pdf_name = f"{src.stem}--{VERSION}.pdf"
        pdf_path = OUT / pdf_name
        body = render_markdown(md)
        meta = (
            f"<div class='meta'>REHT publication version: {html.escape(VERSION)} · "
            f"Published: {PUBLISHED} · Source commit: {html.escape(SOURCE_COMMIT[:12])} · "
            f"Source SHA-256: {source_sha}</div>"
        )
        doc = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{meta}{body}</body></html>"
        HTML(string=doc, base_url=str(ROOT)).write_pdf(str(pdf_path))
        pdf_sha = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
        manifest["reports"].append({
            "title": title,
            "source": str(src.relative_to(ROOT)),
            "source_sha256": source_sha,
            "pdf": f"reports/{pdf_name}",
            "pdf_sha256": pdf_sha,
            "reht_version": VERSION,
            "published": PUBLISHED,
        })

    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    cards = []
    for r in manifest["reports"]:
        cards.append(
            f"<div class='report'><div><a href='{html.escape(Path(r['pdf']).name)}'>{html.escape(r['title'])}</a></div>"
            f"<div class='meta'>{html.escape(VERSION)} · {r['published']} · SHA-256 {r['pdf_sha256'][:16]}…</div></div>"
        )
    index = (
        "<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>VALO Research — Public Reports</title><style>{INDEX_CSS}</style></head><body>"
        "<div class='top'><h1>VALO Research — Public Reports</h1>"
        "<p>Stable PDF publications generated from canonical Markdown sources. Each document carries its REHT publication version, source commit and SHA-256 provenance.</p>"
        "<p><a href='manifest.json'>Machine-readable manifest</a></p></div>" + "".join(cards) + "</body></html>"
    )
    (OUT / "index.html").write_text(index, encoding="utf-8")

if __name__ == "__main__":
    main()
