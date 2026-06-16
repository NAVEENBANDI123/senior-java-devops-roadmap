#!/usr/bin/env python3
"""Combine the roadmap Markdown files into a single Markdown file and a
self-contained, print-ready HTML file (open in a browser -> Save as PDF).

Pure standard library: no external dependencies, works offline.
Handles the Markdown subset used in these docs: headings, pipe tables,
fenced code blocks, ordered/unordered lists, blockquotes, horizontal rules,
bold, italics, inline code and links. Emojis pass through as UTF-8.
"""
import html
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
FILES = [
    "README.md",
    "docs/01-skill-assessment.md",
    "docs/02-roadmap.md",
    "docs/03-resources.md",
    "docs/04-platforms.md",
    "docs/05-projects.md",
    "docs/06-mega-project.md",
    "docs/07-execution-plan.md",
    "docs/08-interview-prep.md",
    "docs/09-readiness-checklist.md",
]

# ---------- inline formatting ----------
_CODE_TOKEN = "\u0000CODE{}\u0000"


def inline(text):
    # protect inline code spans first
    codes = []

    def stash(m):
        codes.append(html.escape(m.group(1)))
        return _CODE_TOKEN.format(len(codes) - 1)

    text = re.sub(r"`([^`]+)`", stash, text)
    # escape the rest
    text = html.escape(text)
    # links [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  r'<a href="\2">\1</a>', text)
    # bold then italic
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\s)([^*]+?)\*(?!\*)", r"<em>\1</em>", text)
    # restore code spans
    text = re.sub(_CODE_TOKEN.replace("{}", r"(\d+)"),
                  lambda m: "<code>" + codes[int(m.group(1))] + "</code>", text)
    return text


def is_table_sep(line):
    s = line.strip()
    if "|" not in s and not set(s) <= set("-:| "):
        return False
    cells = [c.strip() for c in s.strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{1,}:?", c) for c in cells)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


# ---------- block parsing ----------
def convert(md):
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        # fenced code block
        if stripped.startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1  # skip closing fence
            out.append("<pre><code>" + html.escape("\n".join(buf)) + "</code></pre>")
            continue

        # blank line
        if stripped == "":
            i += 1
            continue

        # horizontal rule
        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):
            out.append("<hr/>")
            i += 1
            continue

        # heading
        m = re.match(r"(#{1,6})\s+(.*)", line)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2).strip())}</h{level}>")
            i += 1
            continue

        # table: current line has '|' and next line is a separator
        if "|" in line and i + 1 < n and is_table_sep(lines[i + 1]):
            header = split_row(line)
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(split_row(lines[i]))
                i += 1
            t = ["<table>", "<thead><tr>"]
            t += [f"<th>{inline(c)}</th>" for c in header]
            t.append("</tr></thead><tbody>")
            for r in rows:
                # pad/truncate to header width
                r = (r + [""] * len(header))[:len(header)]
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue

        # blockquote
        if stripped.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append("<blockquote>" + inline(" ".join(buf)) + "</blockquote>")
            continue

        # unordered list
        if re.match(r"\s*[-*+]\s+", line):
            buf = []
            while i < n and re.match(r"\s*[-*+]\s+", lines[i]):
                item = re.sub(r"^\s*[-*+]\s+", "", lines[i])
                buf.append(f"<li>{inline(item)}</li>")
                i += 1
            out.append("<ul>" + "".join(buf) + "</ul>")
            continue

        # ordered list
        if re.match(r"\s*\d+\.\s+", line):
            buf = []
            while i < n and re.match(r"\s*\d+\.\s+", lines[i]):
                item = re.sub(r"^\s*\d+\.\s+", "", lines[i])
                buf.append(f"<li>{inline(item)}</li>")
                i += 1
            out.append("<ol>" + "".join(buf) + "</ol>")
            continue

        # paragraph (gather consecutive plain lines)
        buf = [line]
        i += 1
        while i < n and lines[i].strip() and not re.match(
            r"(#{1,6}\s|\s*[-*+]\s|\s*\d+\.\s|>|```)", lines[i]
        ) and not (re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", lines[i].strip())):
            # stop if it looks like a table start
            if "|" in lines[i] and i + 1 < n and is_table_sep(lines[i + 1]):
                break
            buf.append(lines[i])
            i += 1
        out.append("<p>" + inline(" ".join(b.strip() for b in buf)) + "</p>")
    return "\n".join(out)


CSS = """
:root { --fg:#1f2328; --muted:#57606a; --border:#d0d7de; --accent:#0969da;
        --code-bg:#f6f8fa; --th-bg:#f0f3f6; }
* { box-sizing: border-box; }
body { font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial,
       "Apple Color Emoji","Segoe UI Emoji", sans-serif;
       color: var(--fg); line-height: 1.6; max-width: 960px; margin: 0 auto;
       padding: 40px 48px; font-size: 15px; }
h1,h2,h3,h4,h5,h6 { line-height:1.25; margin:1.4em 0 .5em; font-weight:700; }
h1 { font-size:2em; border-bottom:2px solid var(--border); padding-bottom:.3em; }
h2 { font-size:1.5em; border-bottom:1px solid var(--border); padding-bottom:.3em; }
h3 { font-size:1.25em; } h4 { font-size:1.05em; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
code { background: var(--code-bg); padding:.15em .35em; border-radius:6px;
       font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
       font-size:.88em; }
pre { background: var(--code-bg); padding:14px 16px; border-radius:8px;
      overflow:auto; border:1px solid var(--border); }
pre code { background:none; padding:0; font-size:.82em; line-height:1.45;
           white-space:pre; }
table { border-collapse: collapse; width:100%; margin:1em 0; font-size:.92em;
        display:table; }
th,td { border:1px solid var(--border); padding:7px 11px; text-align:left;
        vertical-align:top; }
th { background: var(--th-bg); font-weight:700; }
tr:nth-child(even) td { background:#fafbfc; }
blockquote { margin:1em 0; padding:.4em 1em; color:var(--muted);
             border-left:4px solid var(--border); background:#fafbfc; }
hr { border:none; border-top:1px solid var(--border); margin:2em 0; }
ul,ol { padding-left:1.6em; }
li { margin:.2em 0; }
.doc-break { page-break-before: always; }
.cover { text-align:center; padding:80px 0 40px; }
.cover h1 { border:none; font-size:2.4em; }
.cover p { color:var(--muted); font-size:1.1em; }
.toc { background:#fafbfc; border:1px solid var(--border); border-radius:8px;
       padding:18px 26px; margin:24px 0; }
@media print {
  body { max-width:none; padding:0 8mm; font-size:11pt; }
  a { color: var(--fg); }
  pre, table, blockquote, img { page-break-inside: avoid; }
  h1,h2,h3 { page-break-after: avoid; }
  .doc-break { page-break-before: always; }
  @page { margin: 16mm 12mm; }
}
"""


def build():
    combined_md = []
    sections_html = []
    for idx, rel in enumerate(FILES):
        text = (REPO / rel).read_text(encoding="utf-8")
        combined_md.append(text)
        cls = "doc-break" if idx > 0 else ""
        sections_html.append(f'<section class="{cls}">\n{convert(text)}\n</section>')

    # combined markdown
    (REPO / "ROADMAP-COMPLETE.md").write_text(
        ("\n\n---\n\n").join(combined_md), encoding="utf-8")

    cover = (
        '<div class="cover">'
        "<h1>The Ultimate Java + Spring Boot + DevOps Career Roadmap</h1>"
        "<p>From Mid-Level Java Developer to Senior Java Backend + DevOps/Cloud "
        "Engineer in 12 Months</p>"
        "<p>A production-grade, job-focused learning system</p>"
        "</div>"
    )
    body = cover + "\n".join(sections_html)
    doc = (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\"/>\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>\n"
        "<title>Senior Java + DevOps Roadmap</title>\n"
        f"<style>{CSS}</style>\n</head>\n<body>\n{body}\n</body>\n</html>\n"
    )
    (REPO / "roadmap-complete.html").write_text(doc, encoding="utf-8")
    print("Wrote ROADMAP-COMPLETE.md and roadmap-complete.html")


if __name__ == "__main__":
    build()
