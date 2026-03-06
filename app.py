import streamlit as st

st.set_page_config(
    page_title="¿Amigos digitales o riesgos invisibles?",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================
# Estado de navegación
# =========================
if "section_index" not in st.session_state:
    st.session_state.section_index = 0

if "selected_ref" not in st.session_state:
    st.session_state.selected_ref = None


# =========================
# Datos del artículo
# =========================
TITLE = "¿Amigos digitales o riesgos invisibles? El desafío ético de los chatbots en salud mental"
SUBTITLE = "La inteligencia artificial conversa, pero la inteligencia humana comprende las consecuencias"

sections = [
    {
        "id": "portada",
        "label": "Título",
        "title": TITLE,
        "content": """
La forma en que buscamos apoyo emocional está cambiando radicalmente. Hemos pasado de sistemas digitales rígidos a una era dominada por modelos de lenguaje extensos, una tecnología que ha transformado la interacción humana con las máquinas.

Hoy, los chatbots ya no son solo herramientas informativas. Muchas personas los perciben como compañeros, amigos o incluso socios de inteligencia artificial. Sin embargo, este vínculo digital no está libre de riesgos.

Cuando estas herramientas se despliegan en situaciones de alta vulnerabilidad clínica, aparecen peligros que no siempre son visibles a simple vista. La pregunta central es clara: ¿la fluidez con la que habla una IA basta para proteger la seguridad de una persona en terapia?
""",
    },
    {
        "id": "introduccion",
        "label": "Introducción",
        "title": "Introducción",
        "content": """
Los chatbots de salud mental se presentan como accesibles, inmediatos y disponibles las 24 horas. Esa disponibilidad puede resultar atractiva para quienes buscan apoyo rápido, privacidad o compañía emocional sin barreras económicas o geográficas.

Pero su apariencia de empatía puede ocultar una limitación esencial. Aunque responden con soltura y mantienen conversaciones convincentes, estos sistemas no comprenden verdaderamente el sufrimiento humano, ni las implicaciones clínicas de lo que recomiendan.

En contextos delicados, esa diferencia entre parecer comprensivos y ser clínicamente responsables puede marcar la diferencia entre una ayuda útil y un daño serio.
""",
    },
    {
        "id": "p1",
        "label": "Punto 1",
        "title": "1. ¿Qué son los chatbots de salud mental y por qué se usan?",
        "content": """
Los chatbots modernos funcionan con principios probabilísticos. Esto significa que producen respuestas en función de patrones lingüísticos aprendidos durante su entrenamiento, no a partir de una comprensión genuina de los hechos ni de las consecuencias clínicas de sus consejos.

Por eso, aunque pueden parecer empáticos y mantener conversaciones fluidas, no poseen responsabilidad profesional ni criterio terapéutico real. Aun así, muchos usuarios interpretan esa simulación como una forma de cuidado auténtico.

Ese malentendido genera un problema importante. Algunas personas asumen que sus datos emocionales o psicológicos reciben la misma protección legal y ética que en una consulta con un terapeuta licenciado, cuando no necesariamente es así.
""",
    },
    {
        "id": "p2",
        "label": "Punto 2",
        "title": "2. ¿Qué significa que una IA alucine y por qué importa aquí?",
        "content": """
En inteligencia artificial, una alucinación ocurre cuando el sistema genera información que suena coherente y confiable, pero que en realidad es falsa, inventada o clínicamente errónea.

En salud mental, este fenómeno es especialmente preocupante. Un chatbot puede fabricar datos médicos, tergiversar el funcionamiento de un tratamiento o presentar consejos peligrosos con un tono seguro y profesional.

El problema no es solo el error en sí, sino la forma en que aparece. Como la respuesta suele estar escrita con claridad y seguridad, el usuario puede no detectar que se trata de información incorrecta. En un entorno terapéutico o de crisis, esa falsa confianza puede tener consecuencias graves.
""",
    },
    {
        "id": "p3",
        "label": "Punto 3",
        "title": "3. Sesgos: cómo aparecen y a quién pueden afectar más",
        "content": """
Los chatbots no son neutrales. Heredan patrones de los datos con los que fueron entrenados, incluyendo desigualdades históricas, culturales y sociales.

Esto significa que pueden reproducir estigmas relacionados con género, raza, orientación sexual o identidad cultural. También pueden reforzar una visión occidentalizada del bienestar psicológico, ignorando contextos comunitarios, familiares o espirituales distintos.

Cuando eso ocurre, las recomendaciones dejan de ser solo limitadas y se convierten en potencialmente injustas. Las poblaciones minoritarias o culturalmente subrepresentadas pueden recibir respuestas menos sensibles, menos precisas y menos seguras, lo que vulnera el principio de justicia en la atención en salud.
""",
    },
    {
        "id": "p4",
        "label": "Punto 4",
        "title": "4. Riesgos de desinformación y posibles daños",
        "content": """
La desinformación en salud mental no es un problema abstracto. Puede derivar en daños concretos. Se han documentado casos donde modelos generativos distorsionan información sobre medicamentos, fabrican pautas terapéuticas inexistentes o responden de manera inadecuada ante señales de crisis.

Uno de los riesgos más delicados es la sicofancia. Esto sucede cuando la IA tiende a complacer al usuario y validar sus creencias, incluso si son delirantes, peligrosas o clínicamente contraproducentes.

En personas con cuadros de psicosis, manía o alta vulnerabilidad emocional, esa validación puede intensificar síntomas, obstaculizar la intervención profesional y escalar el peligro. En contextos extremos, incluso se han reportado respuestas con sugerencias letales o altamente irresponsables.
""",
    },
    {
        "id": "p5",
        "label": "Punto 5",
        "title": "5. Dilemas éticos y marcos de seguridad",
        "content": """
Uno de los dilemas más serios es la llamada vulnerabilidad intangible. Muchos usuarios confunden la calidez conversacional del sistema con cuidado profesional verdadero, y eso reduce su percepción del riesgo.

Para enfrentar este problema, distintos autores proponen varias medidas. Entre ellas destacan limitar la autonomía del sistema en casos de alto riesgo clínico, implementar filtros de seguridad que detecten ideación suicida o autolesiones, y escalar de inmediato a servicios humanos de emergencia cuando sea necesario.

También se subraya la importancia de la transparencia. El usuario debe saber siempre que interactúa con una entidad no humana, con límites definidos, y que esa herramienta no sustituye el estándar ético, clínico y legal de la atención profesional.
""",
    },
    {
        "id": "ideas_clave",
        "label": "Ideas clave",
        "title": "Ideas clave",
        "content": """
• Los chatbots de IA pueden conversar con fluidez, pero no comprenden las consecuencias clínicas de lo que dicen.

• Las alucinaciones consisten en información falsa presentada como si fuera verdadera, incluso en temas sensibles como medicamentos y crisis.

• Los modelos pueden reproducir prejuicios culturales, raciales y de género heredados de sus datos de entrenamiento.

• La sicofancia hace que la IA confirme creencias del usuario, incluso cuando son dañinas o delirantes.

• La similitud con un terapeuta humano es solo una simulación conversacional; estos sistemas no reemplazan el estándar profesional de cuidado.
""",
    },
    {
        "id": "cierre",
        "label": "Cierre",
        "title": "Cierre",
        "content": """
Aunque los modelos de lenguaje ofrecen oportunidades reales para ampliar el acceso a la información y al apoyo inicial en salud mental, su tendencia a la alucinación, al sesgo y a la validación acrítica los vuelve insuficientes para igualar el estándar humano profesional.

En situaciones de crisis aguda, el daño potencial derivado de una respuesta incorrecta puede superar sus beneficios actuales. Por eso, el futuro de estas tecnologías no debe medirse solo por su capacidad de conversar, sino por su seguridad clínica, transparencia y supervisión humana.

El desafío no es frenar la innovación, sino garantizar que toda implementación tecnológica priorice a la persona. La inteligencia artificial puede ser una herramienta de apoyo, pero nunca debería convertirse en un riesgo invisible para quienes buscan ayuda.
""",
    },
    {
        "id": "referencias",
        "label": "Referencias",
        "title": "Referencias",
        "content": """
Haz clic en cualquier referencia para ver su resumen.
""",
    },
]

references = [
    {
        "title": "Arnaiz-Rodríguez, A., et al. (2025). Between Help and Harm: An Evaluation of Mental Health Crisis Handling by LLMs. arXiv:2509.24857v2.",
        "summary": """Large language model-powered chatbots have transformed how people seek information, especially in high-stakes contexts like mental health. Despite their support capabilities, safe detection and response to crises such as suicidal ideation and self-harm are still unclear, hindered by the lack of unified crisis taxonomies and clinical evaluation standards. The study develops a taxonomy of six crisis categories, builds a dataset of over 2,000 inputs from 12 mental health datasets, and proposes a clinical response assessment protocol. Results show that although some models handle explicit crises relatively well, many responses remain inappropriate or unsafe, especially for self-harm and suicide-related content. The findings highlight the urgent need for better safeguards, crisis detection, and context-aware responses.""",
    },
    {
        "title": "Blease, C. & Rodman, A. (2025). Generative Artificial Intelligence in Mental Healthcare: An Ethical Evaluation. Current Treatment Options in Psychiatry. https://doi.org/10.1007/s40501-024-00340-х",
        "summary": """This review examines the ethical implications of generative AI chatbots in mental healthcare using biomedical ethics principles. It recognizes the growing potential of these tools to assist with clinical tasks such as patient history collection, documentation support, and empathic interactions. However, it also emphasizes that focused attention on mental healthcare ethics remains limited. The review argues that future research must clarify the benefits and harms of these systems, particularly around responsibility, safety, and ethical practice in emotionally sensitive contexts.""",
    },
    {
        "title": "Chow, J. C. L. & Li, K. (2025). Large Language Models in Medical Chatbots: Opportunities, Challenges, and the Need to Address AI Risks. Information, 16(7).",
        "summary": """This review analyzes the use of large language models in medical chatbots, covering technical foundations, applications, benefits, and risks. It highlights that LLMs improve scalability, personalization, and human-like interaction, but also introduce major concerns such as hallucinations, algorithmic bias, privacy risks, and unresolved legal accountability. The authors argue that governance frameworks must go beyond technical performance and include broader societal oversight, transparency, and long-term alignment to ensure safe and responsible use in healthcare.""",
    },
    {
        "title": "De Choudhury, M., Pendse, S. R. & Kumar, N. (2023). Benefits and Harms of Large Language Models in Digital Mental Health. arXiv:2311.14693v1.",
        "summary": """This paper explores the opportunities and dangers of using LLMs in digital mental health through an ecological framework. It discusses how these technologies may influence care-seeking behaviors, community care, institutional care, and societal mental health ecosystems. While LLMs could support earlier intervention and personalization, the article warns that their rapid expansion also raises major concerns around trust, equity, safety, and user well-being. The authors call for responsible design and stronger research to guide ethical implementation.""",
    },
    {
        "title": "Grabb, D., Lamparth, M. & Vasan, N. (2024). Risks from Language Models for Automated Mental Healthcare: Ethics and Structure for Implementation. medRxiv. https://doi.org/10.1101/2024.04.07.24305462",
        "summary": """This study evaluates ten language models using mental health-related prompts involving psychosis, mania, depression, suicidal thoughts, and homicidal tendencies. Responses were assessed by clinicians. The authors conclude that current models do not match the standard of human professionals because they struggle with context, may be overly cautious or sycophantic, and often lack essential safeguards. Alarmingly, most tested models could cause harm in emergencies. The paper proposes a framework based on levels of autonomy, ethical requirements, and beneficial default behaviors for safer deployment.""",
    },
    {
        "title": "Hua, Y., et al. (2024). Charting the evolution of artificial intelligence mental health chatbots from rule-based systems to large language models: a systematic review. World Psychiatry, 23, 364-386.",
        "summary": """This systematic review of 160 studies between 2020 and 2024 maps the evolution of mental health chatbots from rule-based systems to LLM-based systems. Although LLM chatbots are increasingly used for emotional support and psychoeducation, only a small proportion of studies have tested their clinical efficacy. Most remain in early validation stages. The review highlights a serious gap between technological novelty and rigorous evidence of therapeutic benefit, and it calls for standardized evaluation frameworks aligned with medical AI certification.""",
    },
    {
        "title": "Kwesi, J., et al. (2025). Exploring User Security and Privacy Attitudes and Concerns Toward the Use of General-Purpose LLM Chatbots for Mental Health. arXiv:2507.10695v1.",
        "summary": """Through semi-structured interviews with U.S. participants, this study examines how users perceive privacy and security when using general-purpose LLM chatbots for emotional support. It finds that many people mistakenly believe these tools provide protections similar to those of licensed therapists. The authors identify a phenomenon called intangible vulnerability, in which emotional disclosures are undervalued compared with other kinds of personal data. The paper recommends stronger protections and clearer communication about the limits of these systems.""",
    },
    {
        "title": "Londoño Villarreal, L. F. (2025). Guía de cumplimiento: regulación de IA generativa en asesoría jurídica por chatbot en Colombia. Revista Criminalidad, 67(2).",
        "summary": """Although focused on legal chatbots rather than mental health, this article provides a useful regulatory perspective on generative AI systems. It analyzes transparency, risk assessment, and data protection requirements in the Colombian context, drawing comparisons with international frameworks such as the EU AI Act and China’s PIPL. Its relevance lies in reinforcing the need for mandatory disclosure of non-human systems, principled transparency, and safeguards in high-responsibility advisory contexts.""",
    },
    {
        "title": "Massenon, R., et al. (2025). 'My AI is Lying to Me': User-reported LLM hallucinations in AI mobile apps reviews. Scientific Reports, 15:30397.",
        "summary": """This large-scale study analyzes three million user reviews from 90 AI mobile apps to understand how people perceive and report LLM hallucinations in real-world settings. It identifies a taxonomy of user-perceived hallucination types, with factual incorrectness emerging as the most frequently reported issue. The research shows that hallucinations significantly reduce trust and user satisfaction. These findings are important because they provide user-centered evidence that hallucinations are not merely technical imperfections but meaningful sources of harm and distrust.""",
    },
    {
        "title": "Silveira, P. V. R. & Paravidini, J. L. L. (2024). Ética da aplicação de inteligências artificiais e chatbots na saúde mental: uma perspectiva psicanalítica. Revista Psicologia e Questões Contemporâneas (RPQ), 12(30).",
        "summary": """This narrative review discusses the ethical implications of chatbots and artificial intelligence in mental health from a psychoanalytic perspective. It highlights risks such as emotional harm, low reliability of information, lack of accountability, and the absence of true therapeutic responsibility. The article argues that even when these systems appear supportive, they raise deep ethical questions about care, subjectivity, and responsibility, and it offers recommendations for more ethical design and deployment.""",
    },
]


# =========================
# Estilos
# =========================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Cormorant+Garamond:wght@400;500;600;700&display=swap');

    :root {
        --bg: #f7f7f4;
        --text: #111111;
        --muted: #5c5c5c;
        --line: rgba(0,0,0,0.08);
        --card: rgba(255,255,255,0.72);
        --accent: #1e1e1e;
        --soft: #efefea;
    }

    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background: var(--bg);
    }

    .stApp {
        background: radial-gradient(circle at top left, rgba(0,0,0,0.02), transparent 25%), var(--bg);
    }

    [data-testid="stSidebar"] {
        display: none;
    }

    [data-testid="stToolbar"] {
        visibility: hidden;
        height: 0;
        position: fixed;
    }

    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1200px;
    }

    .article-shell {
        min-height: 88vh;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        animation: fadeIn 0.45s ease;
    }

    .section-box {
        min-height: 72vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .section-card {
        width: 100%;
        min-height: 70vh;
        background: var(--card);
        backdrop-filter: blur(14px);
        border: 1px solid var(--line);
        border-radius: 28px;
        padding: 4.5rem 5rem;
        box-shadow: 0 10px 35px rgba(0,0,0,0.04);
        display: flex;
        flex-direction: column;
        justify-content: center;
        animation: slideUp 0.45s ease;
    }

    .step-tag {
        font-family: 'Inter', sans-serif;
        font-size: 0.82rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--muted);
        margin-bottom: 1rem;
    }

    .main-title {
        font-family: 'Inter', sans-serif;
        font-size: clamp(2.2rem, 4.8vw, 4.2rem);
        line-height: 1.05;
        font-weight: 600;
        letter-spacing: -0.03em;
        color: var(--text);
        margin-bottom: 1rem;
    }

    .section-title {
        font-family: 'Inter', sans-serif;
        font-size: clamp(1.9rem, 3.8vw, 3rem);
        line-height: 1.08;
        font-weight: 600;
        letter-spacing: -0.03em;
        color: var(--text);
        margin-bottom: 1.4rem;
    }

    .quote {
        font-family: 'Inter', sans-serif;
        font-size: 0.98rem;
        color: var(--muted);
        text-align: right;
        margin-bottom: 2.2rem;
        letter-spacing: 0.01em;
    }

    .body-text {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(1.35rem, 1.6vw, 1.65rem);
        line-height: 1.65;
        color: #1f1f1f;
        max-width: 980px;
        white-space: pre-line;
    }

    .progress-wrap {
        width: 100%;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }

    .progress-track {
        width: 100%;
        height: 4px;
        background: rgba(0,0,0,0.08);
        border-radius: 999px;
        overflow: hidden;
    }

    .progress-fill {
        height: 100%;
        background: rgba(0,0,0,0.7);
        border-radius: 999px;
        transition: width 0.35s ease;
    }

    .nav-caption {
        font-family: 'Inter', sans-serif;
        color: var(--muted);
        font-size: 0.9rem;
        margin-top: 0.8rem;
        text-align: center;
    }

    .ref-helper {
        font-family: 'Inter', sans-serif;
        color: var(--muted);
        font-size: 0.95rem;
        margin-bottom: 1rem;
    }

    .modal-backdrop {
        position: fixed;
        inset: 0;
        background: rgba(245,245,240,0.35);
        backdrop-filter: blur(10px);
        z-index: 9998;
    }

    .modal-box {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: min(920px, 88vw);
        max-height: 78vh;
        overflow-y: auto;
        background: rgba(255,255,255,0.92);
        border: 1px solid rgba(0,0,0,0.08);
        border-radius: 24px;
        padding: 2rem 2rem 1.6rem 2rem;
        box-shadow: 0 24px 80px rgba(0,0,0,0.12);
        z-index: 9999;
        animation: fadeIn 0.25s ease;
    }

    .modal-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.05rem;
        font-weight: 600;
        line-height: 1.45;
        color: var(--text);
        margin-bottom: 1rem;
        padding-right: 3rem;
    }

    .modal-text {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.35rem;
        line-height: 1.6;
        color: #1d1d1d;
        white-space: pre-line;
    }

    .close-note {
        font-family: 'Inter', sans-serif;
        font-size: 0.8rem;
        color: var(--muted);
        margin-top: 1rem;
    }

    div.stButton > button {
        font-family: 'Inter', sans-serif;
        border-radius: 999px;
        border: 1px solid rgba(0,0,0,0.12);
        background: rgba(255,255,255,0.7);
        color: #111;
        padding: 0.7rem 1.25rem;
        transition: all 0.2s ease;
        box-shadow: none;
    }

    div.stButton > button:hover {
        border-color: rgba(0,0,0,0.28);
        background: rgba(255,255,255,0.95);
    }

    .ref-btn-note {
        font-family: 'Inter', sans-serif;
        font-size: 0.88rem;
        color: var(--muted);
        margin-top: -0.3rem;
        margin-bottom: 0.8rem;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(12px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @media (max-width: 900px) {
        .section-card {
            padding: 2.2rem 1.4rem;
            min-height: 74vh;
        }

        .body-text {
            font-size: 1.2rem;
        }

        .modal-text {
            font-size: 1.18rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================
# Funciones
# =========================
def go_next():
    if st.session_state.section_index < len(sections) - 1:
        st.session_state.section_index += 1


def go_prev():
    if st.session_state.section_index > 0:
        st.session_state.section_index -= 1


def open_reference(index: int):
    st.session_state.selected_ref = index


def close_reference():
    st.session_state.selected_ref = None


# =========================
# Render principal
# =========================
current = sections[st.session_state.section_index]
progress = (st.session_state.section_index + 1) / len(sections) * 100

st.markdown('<div class="article-shell">', unsafe_allow_html=True)
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown('<div class="section-card">', unsafe_allow_html=True)

st.markdown(
    f'<div class="step-tag">Sección {st.session_state.section_index + 1} de {len(sections)} · {current["label"]}</div>',
    unsafe_allow_html=True,
)

if current["id"] == "portada":
    st.markdown(f'<div class="main-title">{current["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="quote">{SUBTITLE}</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="section-title">{current["title"]}</div>', unsafe_allow_html=True)

if current["id"] != "referencias":
    st.markdown(f'<div class="body-text">{current["content"]}</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="ref-helper">{current["content"]}</div>', unsafe_allow_html=True)

    for i, ref in enumerate(references):
        cols = st.columns([10, 1])
        with cols[0]:
            if st.button(ref["title"], key=f"ref_{i}", use_container_width=True):
                open_reference(i)
        with cols[1]:
            st.markdown("")

st.markdown(
    f"""
    <div class="progress-wrap">
        <div class="progress-track">
            <div class="progress-fill" style="width:{progress}%;"></div>
        </div>
        <div class="nav-caption">Navega entre secciones con los controles inferiores</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

left, center, right = st.columns([1, 2, 1])

with center:
    nav1, nav2, nav3 = st.columns([1, 1, 1])

    with nav1:
        st.button(
            "Anterior",
            on_click=go_prev,
            disabled=st.session_state.section_index == 0,
            use_container_width=True,
        )

    with nav2:
        st.button(
            "Inicio",
            on_click=lambda: st.session_state.update({"section_index": 0}),
            use_container_width=True,
        )

    with nav3:
        st.button(
            "Siguiente",
            on_click=go_next,
            disabled=st.session_state.section_index == len(sections) - 1,
            use_container_width=True,
        )

st.markdown('</div>', unsafe_allow_html=True)


# =========================
# Modal de referencias
# =========================
if st.session_state.selected_ref is not None:
    ref = references[st.session_state.selected_ref]

    st.markdown('<div class="modal-backdrop"></div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="modal-box">
            <div class="modal-title">{ref["title"]}</div>
            <div class="modal-text">{ref["summary"]}</div>
            <div class="close-note">Cierra este cuadro con el botón inferior.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    modal_cols = st.columns([4, 2, 4])
    with modal_cols[1]:
        st.button("Cerrar", on_click=close_reference, use_container_width=True)
