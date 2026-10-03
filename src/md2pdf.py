# -*- coding: utf-8 -*-
"""
Mini moteur Markdown -> PDF (reportlab) pour le rapport d'audit.

Sous-ensemble Markdown supporté : front-matter (--- clé: valeur ---), titres #/##/###,
paragraphes, listes à puces (-) et numérotées (1.), citations (>), tableaux à barres |,
images ![légende](chemin){width=12cm}, **gras**, *italique*, `code`, saut de page
<!-- pagebreak -->. Les autres commentaires HTML sont ignorés.
Page de titre, sommaire automatique (2 niveaux), en-tête/pied de page numérotés.
"""
import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, Image, KeepTogether, ListFlowable, ListItem,
                                PageBreak, PageTemplate, Paragraph, Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

NAVY = colors.HexColor("#1F3A5F")
ACCENT = colors.HexColor("#2a78d6")
INK = colors.HexColor("#1b1b1b")
MUTED = colors.HexColor("#5a5955")
ROW_ALT = colors.HexColor("#f3f5f8")
RULE = colors.HexColor("#c9ced6")
NOTE_BG = colors.HexColor("#eef4fb")


# ------------------------------------------------------------------ fonts
def _register_fonts():
    """DejaVu (livrée avec matplotlib) pour les accents et symboles ✔ ✘ ◐ → ; repli Helvetica."""
    try:
        import matplotlib
        d = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")
        fonts = {"Body": "DejaVuSans.ttf", "Body-Bold": "DejaVuSans-Bold.ttf",
                 "Body-Italic": "DejaVuSans-Oblique.ttf", "Body-BoldItalic": "DejaVuSans-BoldOblique.ttf",
                 "Mono": "DejaVuSansMono.ttf"}
        for name, fn in fonts.items():
            pdfmetrics.registerFont(TTFont(name, os.path.join(d, fn)))
        pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold",
                                      italic="Body-Italic", boldItalic="Body-BoldItalic")
        return "Body", "Body-Bold", "Mono"
    except Exception:  # pragma: no cover
        return "Helvetica", "Helvetica-Bold", "Courier"


BODY, BOLD, MONO = _register_fonts()

S = {
    "body": ParagraphStyle("body", fontName=BODY, fontSize=9.6, leading=13.6, textColor=INK, spaceAfter=5),
    "h1": ParagraphStyle("h1", fontName=BOLD, fontSize=16, leading=20, textColor=NAVY, spaceBefore=4, spaceAfter=10),
    "h2": ParagraphStyle("h2", fontName=BOLD, fontSize=12, leading=15, textColor=NAVY, spaceBefore=10, spaceAfter=5),
    "h3": ParagraphStyle("h3", fontName=BOLD, fontSize=10.5, leading=13, textColor=INK, spaceBefore=8, spaceAfter=4),
    "cell": ParagraphStyle("cell", fontName=BODY, fontSize=7.8, leading=9.8, textColor=INK),
    "cellh": ParagraphStyle("cellh", fontName=BOLD, fontSize=7.8, leading=9.8, textColor=colors.white),
    "note": ParagraphStyle("note", fontName=BODY, fontSize=9, leading=12.5, textColor=INK),
    "caption": ParagraphStyle("caption", fontName=BODY, fontSize=8, leading=10, textColor=MUTED,
                              alignment=TA_CENTER, spaceAfter=8),
    "toc1": ParagraphStyle("toc1", fontName=BOLD, fontSize=10, leading=14, leftIndent=0),
    "toc2": ParagraphStyle("toc2", fontName=BODY, fontSize=9, leading=11.5, leftIndent=16, textColor=MUTED),
}


# ------------------------------------------------------------------ inline markup
def inline(text):
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"`([^`]+)`", rf'<font name="{MONO}" size="8.5">\1</font>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", text)
    return text


# ------------------------------------------------------------------ doc template
class ReportDoc(BaseDocTemplate):
    def __init__(self, path, meta, **kw):
        super().__init__(path, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                         topMargin=2.2 * cm, bottomMargin=2 * cm,
                         title=meta.get("title", "Rapport"), author=meta.get("author", ""),
                         subject=meta.get("client", ""), **kw)
        self.meta = meta
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="f")
        self.addPageTemplates([PageTemplate("cover", [frame], onPage=self._cover),
                               PageTemplate("normal", [frame], onPage=self._decor)])
        self._h_seq = 0

    def _cover(self, c, doc):
        w, h = A4
        c.saveState()
        c.setFillColor(NAVY)
        c.rect(0, h - 9.5 * cm, w, 9.5 * cm, fill=1, stroke=0)
        c.setFillColor(ACCENT)
        c.rect(0, h - 9.8 * cm, w, 0.3 * cm, fill=1, stroke=0)
        c.restoreState()

    def _decor(self, c, doc):
        w, h = A4
        c.saveState()
        c.setStrokeColor(RULE)
        c.setLineWidth(0.5)
        c.line(2 * cm, h - 1.5 * cm, w - 2 * cm, h - 1.5 * cm)
        c.line(2 * cm, 1.4 * cm, w - 2 * cm, 1.4 * cm)
        c.setFont(BODY, 7.5)
        c.setFillColor(MUTED)
        c.drawString(2 * cm, h - 1.3 * cm, "AgriSouss SARL (cas fictif) - Mini-audit de sécurité de l'information")
        c.drawRightString(w - 2 * cm, h - 1.3 * cm, "CONFIDENTIEL")
        c.drawString(2 * cm, 0.95 * cm, "Étude de cas fictive - cadre académique - "
                     + self.meta.get("author", "").split(" - ")[0])
        c.drawRightString(w - 2 * cm, 0.95 * cm, f"Page {doc.page}")
        c.restoreState()

    def afterFlowable(self, fl):
        if isinstance(fl, Paragraph) and getattr(fl, "_toc_level", None) is not None:
            key = getattr(fl, "_bm", None)
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(fl.getPlainText(), key, level=fl._toc_level, closed=fl._toc_level > 0)
            self.notify("TOCEntry", (fl._toc_level, fl.getPlainText(), self.page, key))


# ------------------------------------------------------------------ parsing
def parse_front_matter(text):
    meta = {}
    if text.startswith("---"):
        end = text.index("\n---", 3)
        for line in text[3:end].strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        text = text[end + 4:]
    return meta, text


def _col_widths(rows, avail):
    ncol = len(rows[0])
    lens = []
    for j in range(ncol):
        L = [len(re.sub(r"[*`]", "", r[j])) if j < len(r) else 0 for r in rows]
        mx = max(L)
        avg = sum(L) / len(L)
        lens.append(max(4.0, min(60.0, 0.5 * mx + 0.8 * avg)))
    tot = sum(lens)
    w = [avail * x / tot for x in lens]
    # largeur minimale par colonne = mot le plus long (pas de coupure en milieu de mot)
    mins = []
    for j in range(ncol):
        words = [wd for r in rows for wd in re.sub(r"[*`]", "", r[j]).split()] or [""]
        longest = max(pdfmetrics.stringWidth(wd, BOLD, 7.8) for wd in words)
        mins.append(max(1.0 * cm, longest + 10))
    for _ in range(5):
        short = [i for i in range(ncol) if w[i] < mins[i]]
        if not short:
            break
        deficit = sum(mins[i] - w[i] for i in short)
        for i in short:
            w[i] = mins[i]
        others = [i for i in range(ncol) if i not in short and w[i] > mins[i]]
        room = sum(w[i] - mins[i] for i in others)
        if room <= 0:
            break
        for i in others:
            w[i] -= deficit * (w[i] - mins[i]) / room
    return w


def make_table(lines, avail):
    rows = []
    for ln in lines:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells if c):
            continue
        rows.append(cells)
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    widths = _col_widths(rows, avail)
    data = [[Paragraph(inline(c), S["cellh"] if i == 0 else S["cell"]) for c in r] for i, r in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    style = [("BACKGROUND", (0, 0), (-1, 0), NAVY),
             ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LINEBELOW", (0, 0), (-1, -1), 0.3, RULE),
             ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
             ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4)]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))
    t.setStyle(TableStyle(style))
    return t


def make_image(path, caption, width, base):
    p = path if os.path.isabs(path) else os.path.join(base, path)
    if not os.path.exists(p):
        return [Paragraph(inline(f"[Image manquante : {path}]"), S["caption"])]
    iw, ih = ImageReader(p).getSize()
    w = width
    h = w * ih / iw
    return [KeepTogether([Image(p, width=w, height=h), Paragraph(inline(caption), S["caption"])])]


def _len_to_pt(s):
    m = re.fullmatch(r"([\d.]+)\s*(cm|mm|pt)?", s.strip())
    if not m:
        return 15 * cm
    v, u = float(m.group(1)), m.group(2) or "pt"
    return v * {"cm": cm, "mm": cm / 10, "pt": 1}[u]


def md_to_flowables(body, base, avail):
    flow = []
    lines = body.splitlines()
    i = 0
    para = []
    seq = [0]

    def flush():
        if para:
            flow.append(Paragraph(inline(" ".join(para)), S["body"]))
            para.clear()

    def heading(level, text):
        st = S[f"h{level}"]
        p = Paragraph(inline(text), st)
        if level <= 2:
            seq[0] += 1
            p._toc_level = level - 1
            p._bm = f"h{seq[0]}"
        return p

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if s.startswith("<!--"):
            flush()
            if "pagebreak" in s:
                flow.append(PageBreak())
            while "-->" not in lines[i]:
                i += 1
            i += 1
            continue
        if not s:
            flush()
            i += 1
            continue
        m = re.match(r"^(#{1,3})\s+(.*)", s)
        if m:
            flush()
            flow.append(heading(len(m.group(1)), m.group(2)))
            i += 1
            continue
        if s.startswith("|"):
            flush()
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            t = make_table(block, avail)
            nrows = len([b for b in block if not re.fullmatch(r"[|:\-\s]+", b.strip())])
            flow.append(KeepTogether([t]) if nrows <= 9 else t)
            flow.append(Spacer(1, 6))
            continue
        m = re.match(r"^!\[(.*?)\]\((.*?)\)(\{width=(.*?)\})?$", s)
        if m:
            flush()
            w = _len_to_pt(m.group(4)) if m.group(4) else avail
            flow += make_image(m.group(2), m.group(1), min(w, avail), base)
            i += 1
            continue
        if s.startswith(">"):
            flush()
            block = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                block.append(lines[i].strip()[1:].strip())
                i += 1
            t = Table([[Paragraph(inline(" ".join(block)), S["note"])]], colWidths=[avail])
            t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NOTE_BG),
                                   ("LINEBEFORE", (0, 0), (0, -1), 3, ACCENT),
                                   ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                                   ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
            flow += [t, Spacer(1, 8)]
            continue
        if re.match(r"^(-|\d+\.)\s+", s):
            flush()
            ordered = bool(re.match(r"^\d+\.", s))
            items = []
            while i < len(lines) and re.match(r"^(-|\d+\.)\s+", lines[i].strip()):
                txt = re.sub(r"^(-|\d+\.)\s+", "", lines[i].strip())
                i += 1
                while i < len(lines) and lines[i].startswith("  ") and lines[i].strip() \
                        and not re.match(r"^(-|\d+\.)\s+", lines[i].strip()):
                    txt += " " + lines[i].strip()
                    i += 1
                items.append(ListItem(Paragraph(inline(txt), S["body"]), leftIndent=14))
            kw = dict(bulletType="1", bulletFontName=BODY, bulletFontSize=9) if ordered else \
                dict(bulletType="bullet", start="•", bulletFontName=BODY, bulletFontSize=9)
            flow.append(ListFlowable(items, leftIndent=14, **kw))
            flow.append(Spacer(1, 3))
            continue
        para.append(s)
        i += 1
    flush()
    return flow


def cover(meta):
    title = ParagraphStyle("ct", fontName=BOLD, fontSize=24, leading=30, textColor=colors.white)
    sub = ParagraphStyle("cs", fontName=BODY, fontSize=13, leading=18, textColor=colors.HexColor("#dce6f2"))
    lab = ParagraphStyle("cl", fontName=BOLD, fontSize=9, leading=12, textColor=MUTED)
    val = ParagraphStyle("cv", fontName=BODY, fontSize=10.5, leading=14, textColor=INK, alignment=TA_LEFT)
    out = [Spacer(1, 1.2 * cm), Paragraph(inline(meta.get("title", "")), title), Spacer(1, 6),
           Paragraph("ISO/IEC 27001:2022 · EBIOS Risk Manager (allégée) · Loi 09-08", sub),
           Spacer(1, 6.2 * cm)]
    rows = [("CLIENT", meta.get("client", "")), ("AUTEUR", meta.get("author", "")),
            ("VERSION", meta.get("version", "")), ("DATE", meta.get("date", "")),
            ("CLASSIFICATION", meta.get("classification", ""))]
    t = Table([[Paragraph(k, lab), Paragraph(inline(v), val)] for k, v in rows], colWidths=[3.6 * cm, 13.4 * cm])
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.3, RULE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    out += [t, Spacer(1, 1.2 * cm)]
    warn = Table([[Paragraph(
        "<b>Avertissement.</b> Étude de cas <b>fictive</b> réalisée dans un <b>cadre académique</b> (entretiens et observations simulés). "
        "« AgriSouss SARL » est un nom fictif ; toute ressemblance avec une entreprise existante serait fortuite. "
        "Ce document ne constitue ni un audit de certification, ni un avis juridique.", S["note"])]],
        colWidths=[17 * cm])
    warn.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NOTE_BG), ("LINEBEFORE", (0, 0), (0, -1), 3, ACCENT),
                              ("LEFTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 7),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    out.append(warn)
    return out


def render(md_path, pdf_path):
    with open(md_path, encoding="utf-8") as f:
        meta, body = parse_front_matter(f.read())
    doc = ReportDoc(pdf_path, meta)
    from reportlab.platypus.doctemplate import NextPageTemplate
    toc = TableOfContents()
    toc.levelStyles = [S["toc1"], S["toc2"]]
    toc.dotsMinLevel = 0
    story = cover(meta)
    story += [NextPageTemplate("normal"), PageBreak(),
              Paragraph("Sommaire", S["h1"]), toc, PageBreak()]
    story += md_to_flowables(body, os.path.dirname(md_path), doc.width)
    doc.multiBuild(story)
    return pdf_path
