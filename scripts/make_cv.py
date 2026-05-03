from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "documents" / "CV.pdf"


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#d7dee8"))
    canvas.line(doc.leftMargin, 0.55 * inch, LETTER[0] - doc.rightMargin, 0.55 * inch)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#657084"))
    canvas.drawString(doc.leftMargin, 0.35 * inch, "Zhihao Zhu")
    canvas.drawRightString(LETTER[0] - doc.rightMargin, 0.35 * inch, f"Page {doc.page}")
    canvas.restoreState()


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "name",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=21,
            leading=25,
            textColor=colors.HexColor("#172033"),
            spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=12,
            textColor=colors.HexColor("#4c5667"),
            alignment=TA_LEFT,
        ),
        "section": ParagraphStyle(
            "section",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=11.5,
            leading=15,
            textColor=colors.HexColor("#2457a6"),
            spaceBefore=12,
            spaceAfter=5,
            borderPadding=(0, 0, 3, 0),
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=12.2,
            textColor=colors.HexColor("#172033"),
            spaceAfter=4,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.6,
            leading=11.5,
            textColor=colors.HexColor("#4c5667"),
        ),
        "right": ParagraphStyle(
            "right",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.6,
            leading=11.5,
            textColor=colors.HexColor("#4c5667"),
            alignment=TA_RIGHT,
        ),
        "pub": ParagraphStyle(
            "pub",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=11.7,
            textColor=colors.HexColor("#172033"),
            spaceAfter=5,
        ),
    }


def p(text, style):
    return Paragraph(text, style)


def section(title, s):
    return [
        Spacer(1, 4),
        p(title.upper(), s["section"]),
        Table([[""]], colWidths=[7.0 * inch], style=TableStyle([
            ("LINEABOVE", (0, 0), (-1, -1), 0.7, colors.HexColor("#d7dee8")),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ])),
    ]


def dated_item(left, right, detail, s):
    table = Table(
        [[p(left, s["body"]), p(right, s["right"])], [p(detail, s["small"]), ""]],
        colWidths=[5.45 * inch, 1.55 * inch],
        hAlign="LEFT",
    )
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    return table


def bullet(text, s):
    return p(f"&bull; {text}", s["pub"])


def build():
    s = styles()
    OUT.parent.mkdir(parents=True, exist_ok=True)

    doc = BaseDocTemplate(
        str(OUT),
        pagesize=LETTER,
        leftMargin=0.72 * inch,
        rightMargin=0.72 * inch,
        topMargin=0.62 * inch,
        bottomMargin=0.72 * inch,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=header_footer)])

    story = []
    story.append(p("Zhihao Zhu", s["name"]))
    story.append(p(
        "Postdoctoral Fellow, Hong Kong University of Science and Technology (HKUST)<br/>"
        "Email: zhihaozhu@ust.hk &nbsp; | &nbsp; Website: https://zzh9568.github.io &nbsp; | &nbsp; "
        "GitHub: zzh9568<br/>"
        "Google Scholar: https://scholar.google.com/citations?user=745H-yoAAAAJ &nbsp; | &nbsp; "
        "ORCID: 0000-0001-5814-1939",
        s["contact"],
    ))

    story += section("Research Interests", s)
    story.append(p(
        "Trustworthy AI; large language models; LLM privacy; training data detection; data revocation; "
        "membership inference; recommender systems; model stealing.",
        s["body"],
    ))

    story += section("Education", s)
    story.append(dated_item(
        "<b>Ph.D. in Computer Science</b>, University of Science and Technology of China",
        "2025",
        "Advisor: Prof. Defu Lian",
        s,
    ))
    story.append(dated_item(
        "<b>Bachelor's Degree</b>, Fuzhou University",
        "2020",
        "",
        s,
    ))

    story += section("Academic Appointment", s)
    story.append(dated_item(
        "<b>Postdoctoral Fellow</b>, Hong Kong University of Science and Technology",
        "2025-Present",
        "Advisor: Prof. Yi Yang",
        s,
    ))

    story += section("Selected Publications", s)
    publications = [
        "<b>Zhihao Zhu</b>, Yi Yang, Yangyang Fan, Defu Lian. "
        "<i>Forget Me If You Can: Auditing User Data Revocation in Recommendation Systems.</i> "
        "Information Systems Research, 2026.",
        "<b>Zhihao Zhu</b>, Yi Yang, Defu Lian. "
        "<i>TDDBench: A Benchmark for Training Data Detection.</i> "
        "International Conference on Learning Representations (ICLR), 2025.",
        "Hongyi Tang*, <b>Zhihao Zhu</b>*, Yi Yang. "
        "<i>Identifying Pre-training Data in LLMs: A Neuron Activation-Based Detection Framework.</i> "
        "Conference on Empirical Methods in Natural Language Processing (EMNLP), 2025. "
        "*Equal contribution.",
        "<b>Zhihao Zhu</b>, Chenwang Wu, Rui Fan, Defu Lian, Enhong Chen. "
        "<i>Membership Inference Attacks against Sequential Recommender Systems.</i> "
        "ACM Web Conference (WWW), 2023.",
        "<b>Zhihao Zhu</b>, Chenwang Wu, Min Zhou, Hao Liao, Defu Lian, Enhong Chen. "
        "<i>Resisting Graph Adversarial Attack via Cooperative Homophilous Augmentation.</i> "
        "ECML PKDD, 2022.",
        "Defu Lian, <b>Zhihao Zhu</b>, Kai Zheng, Yong Ge, Xing Xie, Enhong Chen. "
        "<i>Network Representation Lightening from Hashing to Quantization.</i> "
        "IEEE Transactions on Knowledge and Data Engineering, 2022.",
    ]
    for item in publications:
        story.append(bullet(item, s))

    story += section("Working Papers", s)
    working = [
        "<b>Zhihao Zhu</b>, Jiale Han, Yi Yang. "
        "<i>HoneyImage: Verifiable, Harmless, and Stealthy Dataset Ownership Verification for Image Models.</i> "
        "Under review at MISQ.",
        "<b>Zhihao Zhu</b>, Yi Yang, Chenwang Wu, Defu Lian. "
        "<i>GraphMSA: Stress Testing Graph Classification Services Against Model Stealing Attacks.</i> "
        "Under review at IJOC.",
        "<b>Zhihao Zhu</b>, Hongyi Tang, Yi Yang, Ahmed Abbasi. "
        "<i>Revealing Training Data Exposure in Vision-Language Large Models via Parameter Gradients.</i> "
        "Under review at Nature Communications.",
        "<b>Zhihao Zhu</b>, Rui Fan, Chenwang Wu, Yi Yang, Defu Lian, Enhong Chen. "
        "<i>Model Stealing Attacks against Recommender Systems.</i> "
        "Under review at IEEE Transactions on Dependable and Secure Computing.",
        "<b>Zhihao Zhu</b>, Yi Yang. "
        "<i>RecShield: Output-Level Attribute Unlearning in Recommender Systems.</i> "
        "Under review at Information Systems Research.",
        "<b>Zhihao Zhu</b>, Ninglu Shao, Defu Lian, Chenwang Wu, Zheng Liu, Yi Yang, Enhong Chen. "
        "<i>Understanding Privacy Risks of Embeddings Induced by Large Language Models.</i>",
    ]
    for item in working:
        story.append(bullet(item, s))

    story += section("Awards", s)
    story.append(bullet("<b>National Graduate Scholarship (China)</b>, 2022.", s))
    story.append(bullet("<b>KDD Cup 2023 \"Next Product Generation\" Challenge</b>, 2nd Place.", s))

    doc.build(story)
    print(OUT)


if __name__ == "__main__":
    build()
