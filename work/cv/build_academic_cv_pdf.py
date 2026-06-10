from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


OUT = Path("work/cv/Jie_Hu_Academic_CV.pdf")
NAVY = colors.HexColor("#1F4D78")
DARK = colors.HexColor("#1C272C")
MUTED = colors.HexColor("#5C676C")
ACCENT = colors.HexColor("#B85842")
LIGHT = colors.HexColor("#E8EEF5")
LINE = colors.HexColor("#D7DEE4")

styles = getSampleStyleSheet()
body = ParagraphStyle("BodyCV", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.8, leading=10.8, textColor=DARK, spaceAfter=3)
small = ParagraphStyle("SmallCV", parent=body, fontSize=8.1, leading=9.6, textColor=MUTED)
entry_title = ParagraphStyle("EntryTitle", parent=body, fontName="Helvetica-Bold", fontSize=9.1, leading=10.6, spaceAfter=1)
pub_style = ParagraphStyle("Publication", parent=body, leftIndent=10, firstLineIndent=-10, fontSize=8.25, leading=9.7, spaceAfter=3)
section_style = ParagraphStyle("Section", parent=body, fontName="Helvetica-Bold", fontSize=11, leading=13, textColor=NAVY, spaceBefore=8, spaceAfter=4, borderPadding=(0, 0, 3, 0), borderWidth=0, borderColor=LINE)
title_style = ParagraphStyle("Title", parent=body, fontName="Helvetica-Bold", fontSize=23, leading=25, textColor=DARK, spaceAfter=1)
subtitle_style = ParagraphStyle("Subtitle", parent=body, fontName="Helvetica-Oblique", fontSize=10.2, leading=12, textColor=NAVY, spaceAfter=5)
contact_style = ParagraphStyle("Contact", parent=body, fontSize=8.4, leading=10, textColor=MUTED, spaceAfter=6)
footer_style = ParagraphStyle("Footer", parent=small, alignment=TA_CENTER, fontSize=7.4)


def section(text):
    return [
        Spacer(1, 2),
        Paragraph(text.upper(), section_style),
        Table([[""]], colWidths=[7.02 * inch], rowHeights=[0.6], style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), LINE)])),
        Spacer(1, 3),
    ]


def entry(title, meta="", detail="", bullets=None):
    items = [Paragraph(f"<b>{title}</b>{('  |  <i>'+meta+'</i>') if meta else ''}", entry_title)]
    if detail:
        items.append(Paragraph(detail, small))
    for b in bullets or []:
        items.append(Paragraph(f"<font color='#B85842'>•</font> {b}", ParagraphStyle("bullet", parent=body, leftIndent=11, firstLineIndent=-8, fontSize=8.35, leading=9.8, spaceAfter=1.5)))
    items.append(Spacer(1, 2))
    return KeepTogether(items)


def pub(text, status, link=None):
    suffix = f" <font color='#B85842'><b>[{status}]</b></font>"
    if link:
        suffix += f"  <link href='{link}' color='#B85842'><u>Link</u></link>"
    return Paragraph(f"<font color='#B85842'>•</font> {text}{suffix}", pub_style)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(0.74 * inch, 0.45 * inch, 7.76 * inch, 0.45 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawCentredString(4.25 * inch, 0.28 * inch, f"Jie Hu · Academic Curriculum Vitae · June 2026 · {doc.page}")
    canvas.restoreState()


doc = BaseDocTemplate(
    str(OUT),
    pagesize=letter,
    leftMargin=0.74 * inch,
    rightMargin=0.74 * inch,
    topMargin=0.55 * inch,
    bottomMargin=0.58 * inch,
    title="Jie Hu Academic Curriculum Vitae",
    author="Jie Hu",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
doc.addPageTemplates(PageTemplate(id="academic_cv", frames=frame, onPage=footer))
story = []

story += [
    Paragraph("JIE HU", title_style),
    Paragraph("Researcher in Generative AI, Computer Graphics, HCI, and Digital Heritage", subtitle_style),
    Paragraph(
        "Shanghai, China  |  122089111@qq.com  |  "
        "<link href='https://scholar.google.com/citations?user=OY2L2fIAAAAJ&amp;hl=en' color='#B85842'><u>Google Scholar</u></link>  |  "
        "<link href='https://doi.org/10.1038/s40494-026-02649-7' color='#B85842'><u>npj Heritage Science DOI</u></link>",
        contact_style,
    ),
]
story += section("Research Profile")
story.append(Paragraph(
    "Interdisciplinary researcher and technical artist investigating how generative AI, computer graphics, and interactive systems can support visual storytelling, creative production, and the interpretation of cultural heritage. Current work spans multimodal co-creative agents, 3D Gaussian Splatting, world-model artworks, visual analytics, and AI-assisted game asset pipelines.",
    body,
))
profile_table = Table(
    [
        [Paragraph("<b>Research Interests</b>", small), Paragraph("Generative AI · Human–Computer Interaction · Computer Graphics · Digital Heritage · Game Design", small)],
        [Paragraph("<b>Methods & Tools</b>", small), Paragraph("Multimodal LLMs · Diffusion Models · 3D Gaussian Splatting · Unity/Unreal Engine · Shader Development · Visual Analytics", small)],
    ],
    colWidths=[1.4 * inch, 5.62 * inch],
)
profile_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LIGHT), ("GRID", (0, 0), (-1, -1), 0.35, LINE),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story += [Spacer(1, 4), profile_table]
story += section("Education")
story += [
    entry("Research Exchange Student, Digital Art Laboratory", "Fudan University · Dec 2025–Present", "Advanced research in digital media art, interactive systems, and AI-enabled creative practice."),
    entry("M.A. in Digital Media (Game Design)", "Shanghai University of Engineering Science · Sep 2023–Jun 2026", "GPA: Top 5%; First- and Second-Class Graduate Academic Scholarships. Thesis: Research on the Application of Maqiao Culture in Adventure Puzzle Games."),
    entry("B.A. in Digital Media Art", "Shanghai Jian Qiao University · Sep 2019–Jun 2023", "GPA: Top 10%; consecutive university scholarships; Outstanding Graduation Thesis/Design Award."),
]
story += section("Selected Research Contributions")
story += [
    entry("Digital Heritage Reconstruction and Interpretation", bullets=[
        "Developed UAV-photogrammetry and 3D Gaussian Splatting workflows for reconstructing historical buildings and metaverse environments.",
        "Designed immersive and participatory systems that expose uncertainty rather than presenting machine-generated heritage as unquestioned fact.",
    ]),
    entry("AI-Assisted Visual Creation", bullets=[
        "Built multimodal frameworks for visual narratives, comics, storyboards, and semantically guided 2D-to-3D game asset generation.",
        "Explored controllable synthesis through co-creative agents, retrieval augmentation, and neuro-symbolic systems.",
    ]),
]

story.append(PageBreak())
story += section("Publications and Manuscripts")
papers = [
    ("<b>Jie Hu</b>, Zhaoli Jiang, and Yingfang Zhang. “Digital Regeneration of Historical Buildings Using UAV Photogrammetry and 3D Gaussian Splatting for Metaverse Environments.” <i>npj Heritage Science</i>, 2026.", "Published", "https://doi.org/10.1038/s40494-026-02649-7"),
    ("<b>Jie Hu</b>, Jinyu Li, Zixia Wang, Zhixian Li, Kachun Chan, Zhaoli Jiang, and Yingfang Zhang. “From Pixel to Mesh: Accelerating Game Asset Creation via a Semantically-Guided 2D-to-3D Generative Pipeline.” AHFE 2026.", "Accepted", None),
    ("<b>Jie Hu</b>, Yingfang Zhang, and Zhaoli Jiang. “Innovative Application of AIGC Technology in Digital Game Design.” ICDI 2024.", "Published", None),
    ("<b>Jie Hu</b>, Zhaoli Jiang, and Yingfang Zhang. “Parametric Design Mechanism of Cultural Products Driven by AIGC.” <i>Shoes Technology and Design</i>, 2026.", "Published", None),
    ("Zhaoli Jiang, Xiaoxian Ye, and <b>Jie Hu</b>. “Research on the Application of Generative AI in the Digital Design of Miao Totem Symbols.” <i>Package &amp; Design</i>, 2025.", "Published", None),
    ("<b>Jie Hu</b>, Zhaoli Jiang, and Yingfang Zhang. “Unweaving the Machine Scroll: A Participatory World-Model Artwork for Inspecting Historical Uncertainty in Qingming Shanghe Tu.” SIGGRAPH Asia 2026 Art Papers.", "Under Review", None),
    ("<b>Jie Hu</b>, Zhaoli Jiang, and Yingfang Zhang. “DualDraft: Enabling Zero-Experience Users to Create Consistent Visual Narratives via a Dual-Mode Co-Creative Agent.” UIST 2026.", "Under Review", None),
    ("<b>Jie Hu</b>, Zhaoli Jiang, and Yingfang Zhang. “Palimpsest of Maqiao: An Immersive VR Visual Analytics Framework through Stylized 3D Gaussian Splatting.” IEEE TVCG.", "Under Review", None),
    ("<b>Jie Hu</b>, Zhaoli Jiang, and Yingfang Zhang. “KomixFlow: A Retrieval-Augmented Multimodal Framework for Long-Horizon Visual Narrative Generation.” IEEE Transactions on Multimedia.", "Under Review", None),
    ("<b>Jie Hu</b>, Zhaoli Jiang, and Yingfang Zhang. “StoryNode: A Node-Based Visual Orchestration Framework for Automated Comic and Storyboard Generation.” International Journal of Human–Computer Interaction.", "Under Review", None),
    ("<b>Jie Hu</b>, Zhaoli Jiang, and Yingfang Zhang. “A Neuro-Symbolic Expert System for Controllable LLM-Driven Multimodal Content Synthesis.” Expert Systems with Applications.", "Under Review", None),
    ("<b>Jie Hu</b>, Zhaoli Jiang, and Yingfang Zhang. “Exploration of Revitalizing ‘Cold Heritage’ Empowered by Generative AI: A Case Study of Maqiao Pottery Particle System.” Journal of Graphics.", "Under Review", None),
]
story += [pub(*p) for p in papers]
story += section("Academic Service")
story += [
    entry("Reviewer", "ACM UIST 2026", "Reviewed submissions for the ACM Symposium on User Interface Software and Technology."),
    entry("Reviewer", "ACM ICMR 2026", "Reviewed submissions for the ACM International Conference on Multimedia Retrieval."),
]
story += section("Selected Honors and Awards")
for t, m in [
    ("National Third Prize", "11th Future Designer National College Digital Art & Design Awards · 2023"),
    ("Second Prize and Two Third Prizes", "9th Huichuang Youth Shanghai College Students Cultural and Creative Works Exhibition · 2024"),
    ("Regional First Prizes", "10th and 11th Future Designer NCDA, Shanghai · 2022–2023"),
    ("Outstanding Graduation Thesis/Design Award", "Shanghai Jian Qiao University · 2023"),
    ("Graduate Academic Scholarships", "First- and Second-Class Awards · 2023–2024"),
]:
    story.append(entry(t, m))

story.append(PageBreak())
story += section("Research-Relevant Professional Experience")
story += [
    entry("Technical Artist", "NetEase Games · Dec 2025–Present", bullets=[
        "Develop AI agents and multimodal video workflows for game production and provide rendering support for high-fidelity FPS projects.",
        "Optimize realistic materials, shaders, and scene-rendering workflows by integrating generative AI with conventional graphics pipelines.",
    ]),
    entry("Art Project Manager, Infinity Nikki", "Papergames · Sep 2025–Dec 2025", bullets=[
        "Managed cross-platform VFX production for a large-scale open-world title across PC, mobile, and PS5.",
        "Coordinated art, engineering, design, and external production teams to improve asset delivery and pipeline reliability.",
    ]),
    entry("R&D Project Manager and Technical Artist, DreamStar", "Tencent TiMi Studio · Mar 2025–Aug 2025", bullets=[
        "Established client-module testing standards and defect-analysis workflows for open-world gameplay, rendering, physics, and AI.",
        "Collaborated with engineering and art teams to resolve rendering anomalies, terrain-material issues, and development risks.",
    ]),
    entry("Marketing and Publishing Project Manager", "Lilith Games · Oct 2024–Mar 2025", bullets=[
        "Led China-region creative production and coordinated development, publishing, and external teams for campaign delivery.",
        "Used performance data and market feedback to support publishing decisions and resource allocation.",
    ]),
]
story += section("Selected Projects")
story += [
    entry("Unweaving the Machine Scroll", "Participatory World-Model Artwork · 2026", "Transforms Qingming Shanghe Tu into an inspectable machine-generated environment, enabling visitors to distinguish evidence, inferred continuity, and algorithmic speculation."),
    entry("Maqiao Cultural Journey", "Master’s Thesis and Interactive Game · 2026", "A 3D adventure-puzzle game integrating archaeological and cultural elements to support the digital revitalization of Maqiao heritage."),
    entry("Lost Ruins – Akrosa", "3D Environment Design · 2023", "End-to-end Unreal Engine 5 environment production using a complete PBR workflow; received the Outstanding Graduation Thesis/Design Award."),
]
story += section("Technical Skills")
skills = [
    ("AI and Research", "Multimodal LLMs, diffusion models, LoRA, ControlNet, ComfyUI, co-creative agents, retrieval-augmented generation"),
    ("Graphics and Engines", "Unreal Engine 5, Unity, 3D Gaussian Splatting, PBR workflows, shader development, procedural modeling"),
    ("Programming", "Python, C#, C++ fundamentals, GLSL/HLSL"),
    ("Design and DCC", "Blender, Maya, 3ds Max, Substance Painter, Adobe Creative Suite"),
    ("Languages", "Chinese (native), English (research and professional working proficiency), Korean (TOPIK Level 2)"),
]
skill_table = Table([[Paragraph(f"<b>{a}</b>", small), Paragraph(b, small)] for a, b in skills], colWidths=[1.35 * inch, 5.67 * inch])
skill_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LIGHT), ("GRID", (0, 0), (-1, -1), 0.35, LINE),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]))
story.append(skill_table)

OUT.parent.mkdir(parents=True, exist_ok=True)
doc.build(story)
print(OUT)
