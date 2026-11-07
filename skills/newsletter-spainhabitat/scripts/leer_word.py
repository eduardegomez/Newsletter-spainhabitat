"""Read DOCX editorial paragraphs and their actual links without changing the file."""
import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"


def paragraph_text(node):
    parts = []
    for child in node:
        if child.tag == W + "del":
            continue
        if child.tag == W + "t":
            parts.append(child.text or "")
        elif child.tag in (W + "br", W + "cr"):
            parts.append("\n")
        elif child.tag == W + "tab":
            parts.append("\t")
        else:
            parts.append(paragraph_text(child))
    return "".join(parts)


def extract(path):
    with ZipFile(path) as archive:
        rel_path = "word/_rels/document.xml.rels"
        rels = {}
        if rel_path in archive.namelist():
            rels = {r.get("Id"): r.get("Target")
                    for r in ET.fromstring(archive.read(rel_path))}
        root = ET.fromstring(archive.read("word/document.xml"))
        paragraphs = []
        for index, p in enumerate(root.iter(W + "p"), 1):
            text = paragraph_text(p)
            links = [{"text": paragraph_text(h),
                      "target": rels.get(h.get(R + "id")),
                      "anchor": h.get(W + "anchor")}
                     for h in p.iter(W + "hyperlink")]
            fields = [n.text for n in p.iter(W + "instrText") if n.text]
            fields += [n.get(W + "instr") for n in p.iter(W + "fldSimple")]
            if text.strip() or links or fields:
                paragraphs.append({"paragraph": index, "text": text,
                                   "hyperlinks": links, "fields": fields})
        comments = []
        if "word/comments.xml" in archive.namelist():
            for c in ET.fromstring(archive.read("word/comments.xml")):
                comments.append({"id": c.get(W + "id"),
                                 "text": "\n".join(paragraph_text(p)
                                                    for p in c.iter(W + "p"))})
        return {"source": str(Path(path).resolve()), "paragraphs": paragraphs,
                "comments": comments,
                "has_tracked_changes": any(n.tag in (W + "ins", W + "del")
                                           for n in root.iter())}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(extract(args.docx), ensure_ascii=False, indent=2))
