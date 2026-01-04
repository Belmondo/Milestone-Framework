# streamlit_app.py
# ------------------------------------------------------------
# MILESTONE - Streamlit Single-File App
# - Preserva identidade visual (theme.css / swagger.css) se existirem em /static
# - Landing page em HTML (muito próximo ao seu FastAPI main)
# - Swagger UI e ReDoc embutidos via CDN, alimentados por OpenAPI gerado no app
# - Endpoints simulados (health/register/history/data) dentro do Streamlit
# - Imports pesados (MAPE-K + TensorFlow) só ao executar /data (lazy import)
# ------------------------------------------------------------

import base64
import json
from pathlib import Path
from uuid import uuid4
from typing import Any, Dict, Optional

import streamlit as st
import streamlit.components.v1 as components


# -----------------------
# Constantes
# -----------------------
APP_TITLE = "MILESTONE: Framework para Monitoramento Contínuo de Desempenho em Sistemas Auto-Adaptativos."
APP_VERSION = "0.1.0"

ROOT_DIR = Path(__file__).resolve().parent
STATIC_DIR = ROOT_DIR / "static"


# -----------------------
# I18N (igual ao seu main)
# -----------------------
I18N = {
    "pt": {
        "title": APP_TITLE,
        "subtitle": "Trabalho de Doutorado • Documentação unificada (Landing / Swagger / ReDoc)",
        "description": "Uma API baseada em **MAPE-K** (Monitor, Analyze, Plan, Execute, Knowledge) para monitoramento e gerenciamento autônomo com suporte de **Redes Neurais**.\n\nSubstitua esta descrição pela versão final do seu trabalho.",
        "nav_home": "Home",
        "nav_swagger": "Swagger (interativo)",
        "nav_redoc": "ReDoc (documentação)",
        "nav_json": "OpenAPI JSON",
        "hero_title": "Sobre a API",
        "hero_text": "Esta API materializa, em forma de serviço, a contribuição central da tese: o Milestone, um framework voltado ao monitoramento contínuo e à avaliação de desempenho em sistemas auto-adaptativos, integrando redes neurais para identificar anomalias de desempenho, avaliar possíveis soluções e indicar estratégias de adaptação de maneira contínua e autônoma.  A motivação parte da constatação de que ainda há carência de mecanismos que sustentem a engenharia contínua de desempenho em SAS, já que muitas soluções priorizam aspectos funcionais e negligenciam a avaliação de requisitos não funcionais, ou tratam apenas parte do requisito (sem considerar suas subcaracterísticas de forma integrada).  Nesse contexto, também se destaca a necessidade de mecanismos que aliem capacidade preditiva, adaptabilidade e integração ao MAPE-K para apoiar decisões baseadas em dados em tempo de execução. <br><br> Assim, o objetivo do doutorado é propor um framework que apoie o monitoramento e a avaliação contínuos do desempenho por meio da integração de um modelo baseado em redes neurais ao loop MAPE-K, buscando melhorar a precisão das decisões de adaptação com uma visão mais completa e contextualizada das subcaracterísticas de eficiência de desempenho.  A abordagem se ancora no MAPE-K como organização do ciclo adaptativo (Monitorar, Analisar, Planejar, Executar e Conhecimento). No uso prático, a API serve como “camada de supervisão”, acoplável a diferentes sistemas e plataformas, desde que seja possível coletar métricas em tempo de execução e, quando necessário, acionar comandos de reconfiguração. Ela permite: coletar métricas de desempenho, interpretar o estado do sistema em tempo real e apoiar a tomada de decisão adaptativa considerando subcaracterísticas de desempenho, limiares e ações disponíveis. O papel da rede neural é central na fase de análise, realizando a classificação do estado (por exemplo, “bom/ruim”) a partir das métricas monitoradas; na tese, a rede usada é uma MLP com camadas densas (32 e 16 neurônios com ReLU) e saída sigmoide, treinada para um problema binário com binary crossentropy e acurácia como métrica. <hr>",
        "endpoints_title": "Endpoints principais",
        "authors_title": "Autores",
        "citation_title": "Como citar / referência",
        "arch_title": "Arquitetura do Milestone",
        "arch_text": "A arquitetura adotada é cliente–servidor, garantindo separação clara de responsabilidades: o cliente faz a interface de comunicação com o sistema gerenciado, enquanto o servidor (sistema gerenciador) processa solicitações e devolve respostas, favorecendo independência de plataforma e escalabilidade. O Milestone é inspirado no MAPE-K e cada etapa foi desenhada com responsabilidade única, interfaces bem definidas e desacoplamento, permitindo manutenção/testes por componente e reuso de módulos em diferentes contextos. A comunicação entre etapas segue o padrão Observer, com troca assíncrona de mensagens, e o framework prevê invocação agendada, por eventos ou em batches, facilitando incorporação em pipelines. Do ponto de vista de modularização, o texto descreve módulos alinhados às fases do ciclo (Monitoramento, Análise, Planejamento e Conhecimento), com responsabilidades bem definidas e possibilidade de extensão/substituição independente.",
        "footer": "© {title} • v{version}",
        "tag_main": "Operações Principais",
        "author_description": "Programa de Mestrado e Doutorado em Ciências da Computação - Universidade Federal do Ceará",
        "PhD_advisor": "(Orientadora) — Programa de Mestrado e Doutorado em Ciências da Computação - Universidade Federal do Ceará",
        "great": "Grupo de Redes de Computadores, Engenharia de Software e Sistemas - UFC",
        "ui_title": "UI (Streamlit) — Documentação & Testes",
        "ui_hint": "Use a navegação ao lado para alternar entre Landing, Swagger, ReDoc, OpenAPI e testes de endpoints.",
        "page_home": "Landing",
        "page_swagger": "Swagger",
        "page_redoc": "ReDoc",
        "page_openapi": "OpenAPI JSON",
        "page_endpoints": "Endpoints",
        "run_data": "Executar /data (MAPE-K)",
        "payload": "Payload (JSON) para /data",
        "run": "Executar",
        "health": "Health",
        "register": "Register",
        "history": "History",
    },
    "en": {
        "title": "MILESTONE: A Framework for Continuous Performance Monitoring in Self-Adaptive Systems.",
        "subtitle": "PhD Research • Unified Documentation (Landing / Swagger / ReDoc)",
        "description": "An API based on **MAPE-K** (Monitor, Analyze, Plan, Execute, Knowledge) for autonomous monitoring and management supported by **Neural Networks**.\n\nReplace this description with the final version of your work.",
        "nav_home": "Home",
        "nav_swagger": "Swagger (interactive)",
        "nav_redoc": "ReDoc (documentation)",
        "nav_json": "OpenAPI JSON",
        "hero_title": "About the API",
        "hero_text": "This API operationalizes the thesis contribution as a service: Milestone, a framework for continuous performance monitoring and evaluation in self-adaptive systems, integrating neural networks to detect performance anomalies, evaluate candidate solutions, and indicate adaptation strategies continuously and autonomously. The motivation stems from the lack of mechanisms supporting continuous performance engineering in SAS: many approaches focus on functional adaptation while neglecting non-functional evaluation, or they only address partial aspects of performance rather than its sub-characteristics in an integrated way. The work also emphasizes the need for predictive, adaptable mechanisms integrated with MAPE-K to support data-driven runtime decisions. <br><br> The doctoral goal is to propose a framework that supports continuous monitoring and evaluation of performance by integrating a neural-network-based model into the MAPE-K loop, aiming to improve adaptation decision accuracy through a more contextualized view of performance-efficiency sub-characteristics. The approach is grounded in the MAPE-K cycle (Monitor, Analyze, Plan, Execute, Knowledge). In practice, the API acts as a supervision layer that can be attached to different systems/platforms as long as runtime metrics can be collected and reconfiguration commands can be executed when needed. It enables runtime metric collection, real-time state interpretation, and decision support based on sub-characteristics, thresholds, and available actions. Neural networks play a central role in the analysis stage by classifying system state (e.g., “good/bad”) from monitored metrics. The thesis reports an MLP (Dense 32/16 with ReLU, sigmoid output) trained for binary classification with binary crossentropy and accuracy.",
        "endpoints_title": "Main Endpoints",
        "authors_title": "Authors",
        "citation_title": "How to cite / reference",
        "arch_title": "MAPE-K Architecture",
        "arch_text": "Milestone adopts a client–server architecture: the client interfaces with the managed system, while the server (manager) processes requests and returns responses, supporting platform independence and scalability. Stages are inspired by MAPE-K and follow single-responsibility, decoupled interfaces, and modular reuse; stages communicate via the Observer pattern with asynchronous messaging, and the framework supports scheduled/event/batch invocation for pipeline integration. The implementation is organized into modules aligned with monitoring, analysis, planning, and knowledge responsibilities, enabling independent extension/substitution.",
        "footer": "© {title} • v{version}",
        "tag_main": "Main Operations",
        "author_description": "Master’s and Doctoral Program in Computer Science — Federal University of Ceara",
        "PhD_advisor": "(PhD advisor) — Master and Doctoral Program in Computer Science — Federal University of Ceara",
        "great": "Group of Computer Networks, Software Engineering and Systems",
        "ui_title": "UI (Streamlit) — Docs & Tests",
        "ui_hint": "Use the sidebar navigation to switch between Landing, Swagger, ReDoc, OpenAPI and endpoint tests.",
        "page_home": "Landing",
        "page_swagger": "Swagger",
        "page_redoc": "ReDoc",
        "page_openapi": "OpenAPI JSON",
        "page_endpoints": "Endpoints",
        "run_data": "Run /data (MAPE-K)",
        "payload": "Payload (JSON) for /data",
        "run": "Run",
        "health": "Health",
        "register": "Register",
        "history": "History",
    },
}


# -----------------------
# Helpers (CSS / imagens)
# -----------------------
def _read_text(path: Path) -> str:
    if path.exists() and path.is_file():
        return path.read_text(encoding="utf-8", errors="ignore")
    return ""


def _img_to_data_uri(path: Path) -> Optional[str]:
    if not path.exists() or not path.is_file():
        return None
    b = path.read_bytes()
    ext = path.suffix.lower().lstrip(".")
    mime = "image/png" if ext == "png" else "image/jpeg" if ext in ("jpg", "jpeg") else "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(b).decode('utf-8')}"


def inject_css():
    # Reutiliza seu theme.css se existir
    theme_css = _read_text(STATIC_DIR / "theme.css")
    if theme_css:
        st.markdown(f"<style>{theme_css}</style>", unsafe_allow_html=True)

    # Pequenos ajustes para remover padding padrão do Streamlit (mantém seu layout)
    st.markdown(
        """
        <style>
          /* reduz a “moldura” do Streamlit */
          .block-container { padding-top: 1rem; padding-bottom: 2rem; max-width: 1200px; }
          header[data-testid="stHeader"] { height: 0; }
          div[data-testid="stToolbar"] { visibility: hidden; height: 0; position: fixed; }
        </style>
        """,
        unsafe_allow_html=True,
    )


# -----------------------
# OpenAPI (gerado no Streamlit)
# -----------------------
def _pyd_schema(model: Any) -> Dict[str, Any]:
    """
    Compatível com Pydantic v1/v2.
    """
    if model is None:
        return {"type": "object"}
    if hasattr(model, "model_json_schema"):  # Pydantic v2
        return model.model_json_schema()
    if hasattr(model, "schema"):  # Pydantic v1
        return model.schema()
    return {"type": "object"}


def build_openapi(lang: str, lab_logo_data_uri: Optional[str]) -> Dict[str, Any]:
    if lang not in I18N:
        lang = "pt"
    t = I18N[lang]

    # Tenta usar seus modelos reais (se existirem no repo).
    # Se falhar, continua com schemas genéricos (deploy não quebra).
    Data = InstanceIDResponse = Neural_Network_Response = None
    try:
        from schemas.data_models import Data as _Data, InstanceIDResponse as _InstanceIDResponse, Neural_Network_Response as _NNResp  # type: ignore
        Data, InstanceIDResponse, Neural_Network_Response = _Data, _InstanceIDResponse, _NNResp
    except Exception:
        pass

    schema_data = _pyd_schema(Data)
    schema_reg = _pyd_schema(InstanceIDResponse)
    schema_nn = _pyd_schema(Neural_Network_Response)

    spec: Dict[str, Any] = {
        "openapi": "3.0.3",
        "info": {
            "title": t["title"],
            "version": APP_VERSION,
            "description": t["description"],
        },
        "paths": {
            "/health": {
                "get": {
                    "tags": [t["tag_main"]],
                    "summary": "Health check",
                    "responses": {
                        "200": {
                            "description": "OK",
                            "content": {"application/json": {"schema": {"type": "object"}}},
                        }
                    },
                }
            },
            "/register": {
                "get": {
                    "tags": [t["tag_main"]],
                    "summary": "Register instance",
                    "responses": {
                        "200": {
                            "description": "Instance registered",
                            "content": {"application/json": {"schema": schema_reg}},
                        }
                    },
                }
            },
            "/database/history": {
                "get": {
                    "tags": [t["tag_main"]],
                    "summary": "Get knowledge history",
                    "responses": {
                        "200": {
                            "description": "History list",
                            "content": {"application/json": {"schema": {"type": "object"}}},
                        }
                    },
                }
            },
            "/data": {
                "post": {
                    "tags": [t["tag_main"]],
                    "summary": "Run MAPE-K cycle",
                    "requestBody": {
                        "required": True,
                        "content": {"application/json": {"schema": schema_data}},
                    },
                    "responses": {
                        "200": {
                            "description": "MAPE-K result",
                            "content": {"application/json": {"schema": schema_nn}},
                        }
                    },
                }
            },
        },
    }

    # Logo (ReDoc exibe muito bem)
    if lab_logo_data_uri:
        spec["info"]["x-logo"] = {"url": lab_logo_data_uri, "altText": "Laboratório"}

    return spec


# -----------------------
# Landing HTML (muito próximo ao seu)
# -----------------------
def build_landing_html(lang: str, t: Dict[str, str], lab_logo_uri: str, uni_logo_uri: str) -> str:
    # Links internos por query params (funciona no Streamlit):
    home_href = f"?page=home&lang={lang}"
    swagger_href = f"?page=swagger&lang={lang}"
    redoc_href = f"?page=redoc&lang={lang}"
    json_href = f"?page=openapi&lang={lang}"

    # Bandeiras externas (igual ao seu main)
    br_flag = "https://flagcdn.com/24x18/br.png"
    gb_flag = "https://flagcdn.com/24x18/gb.png"

    return f"""
<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{t['title']}</title>

  <!-- Se houver theme.css em /static, ele já foi injetado via st.markdown -->
  <!-- Fallback mínimo caso não exista -->
  <style>
    :root {{
      --bg: #070A12;
      --card: #0B1020;
      --border: rgba(255,255,255,.08);
      --text: #E8ECFF;
      --muted: #CFD7FF;
    }}
    body {{ background: var(--bg); color: var(--text); margin: 0; font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; }}
    a {{ color: inherit; text-decoration: none; }}
    code {{ background: rgba(255,255,255,.06); padding: 2px 6px; border-radius: 6px; }}
    .container {{ max-width: 1100px; margin: 0 auto; padding: 18px; }}
    .topbar {{ border-bottom: 1px solid var(--border); background: rgba(11,16,32,.7); backdrop-filter: blur(12px); }}
    .topbar-inner {{ display: flex; justify-content: space-between; gap: 16px; align-items: center; }}
    .brand {{ display: flex; gap: 14px; align-items: center; }}
    .logos {{ display: flex; gap: 10px; align-items: center; }}
    .logo {{ width: 44px; height: 44px; border-radius: 12px; border: 1px solid var(--border); background: rgba(255,255,255,.04); object-fit: cover; }}
    .badge {{ display: inline-block; font-size: 12px; color: var(--muted); opacity: .9; }}
    h1 {{ font-size: 18px; margin: 4px 0 0; }}
    .subtitle {{ margin: 4px 0 0; color: var(--muted); font-size: 13px; opacity: .9; }}
    .nav {{ display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }}
    .btn {{ border: 1px solid var(--border); background: rgba(255,255,255,.04); padding: 8px 12px; border-radius: 12px; }}
    .btn-ghost {{ background: transparent; }}
    .card {{ border: 1px solid var(--border); border-radius: 18px; background: var(--card); padding: 18px; box-shadow: 0 10px 40px rgba(0,0,0,.35); }}
    .mt {{ margin-top: 16px; }}
    .hero {{ display: grid; grid-template-columns: 1.35fr .85fr; gap: 16px; }}
    @media (max-width: 980px) {{ .hero {{ grid-template-columns: 1fr; }} }}
    .muted {{ color: var(--muted); opacity: .95; }}
    .callout {{ border: 1px solid var(--border); border-radius: 16px; padding: 14px; background: rgba(255,255,255,.03); }}
    .callout-title {{ font-weight: 700; margin-bottom: 8px; }}
    .k {{ color: var(--muted); width: 120px; display: inline-block; }}
    .seal {{ display: flex; gap: 12px; align-items: center; padding: 14px; border: 1px solid var(--border); border-radius: 18px; background: rgba(255,255,255,.03); }}
    .seal-logo {{ width: 56px; height: 56px; border-radius: 16px; border: 1px solid var(--border); }}
    .seal-title {{ font-weight: 800; letter-spacing: .04em; }}
    .inner {{ margin-top: 14px; }}
    .footer {{ padding: 22px 0 10px; text-align: center; opacity: .85; }}
  </style>
</head>

<body>
  <header class="topbar">
    <div class="container topbar-inner">
      <div class="brand">
        <div class="logos">
          <img src="{lab_logo_uri}" alt="Logo do laboratório" class="logo logo-lab"/>
          <img src="{uni_logo_uri}" alt="Logo da universidade" class="logo logo-uni"/>
        </div>
        <div class="brand-text">
          <div class="badge">MAPE-K • Neural Control • Streamlit</div>
          <h1>{t['title']}</h1>
          <p class="subtitle">{t['subtitle']}</p>
        </div>
      </div>

      <nav class="nav">
        <a class="btn" href="{swagger_href}">{t['nav_swagger']}</a>
        <a class="btn" href="{redoc_href}">{t['nav_redoc']}</a>
        <a class="btn btn-ghost" href="{json_href}">{t['nav_json']}</a>

        <div style="margin-left: 15px; display: inline-flex; gap: 12px; align-items: center;">
            <a href="?page=home&lang=pt" title="Português">
                <img src="{br_flag}" alt="PT" style="border-radius: 2px; opacity: {"1" if lang=="pt" else "0.4"}; transition: opacity .2s;">
            </a>
            <a href="?page=home&lang=en" title="English">
                <img src="{gb_flag}" alt="EN" style="border-radius: 2px; opacity: {"1" if lang=="en" else "0.4"}; transition: opacity .2s;">
            </a>
        </div>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero card">
      <div class="hero-left">
        <h2>{t['hero_title']}</h2>
        <p class="muted" style="text-align: justify !important;">
          {t['hero_text']}
        </p>

        <div class="callout">
          <div class="callout-title">{t['endpoints_title']}</div>
          <div class="callout-body">
            <div><span class="k">Health:</span> <code>/health</code></div>
            <div><span class="k">Registro:</span> <code>/register</code></div>
            <div><span class="k">Histórico:</span> <code>/database/history</code></div>
            <div><span class="k">Ciclo MAPE-K:</span> <code>/data</code></div>
          </div>
        </div>
      </div>

      <div class="hero-right">
        <div class="seal">
          <img src="{lab_logo_uri}" alt="Selo do laboratório" class="seal-logo"/>
          <div class="seal-text">
            <div class="seal-title">GREat</div>
            <div class="seal-sub">{t['great']}</div>
          </div>
        </div>

        <div class="card inner">
          <h3>{t['authors_title']}</h3>
          <p class="muted" style="text-align: justify !important;">
            👨‍🎓 <strong>Belmondo Rodrigues Aragão Junior</strong> — {t['author_description']}<br/><br/>
            👩🏻‍🏫 <strong>Profa. Dra. Rossana M. C. Andrade</strong> {t['PhD_advisor']}
          </p>
        </div>
      </div>
    </section>

    <section class="card mt">
      <h2>{t['arch_title']}</h2>
      <p class="muted" style="text-align: justify !important;">
        {t['arch_text']}
      </p>
    </section>

    <footer class="footer">
      <div class="muted">{t['footer'].format(title=t['title'], version=APP_VERSION)}</div>
      <div class="muted" style="margin-top: 6px;">
        <a href="?page=endpoints&lang={lang}" class="btn" style="display:inline-block;margin-top:8px;">Abrir testes de endpoints</a>
      </div>
    </footer>
  </main>
</body>
</html>
"""


# -----------------------
# Swagger UI embutido
# -----------------------
def render_swagger_ui(openapi_spec: Dict[str, Any], lang: str, t: Dict[str, str]):
    swagger_css = _read_text(STATIC_DIR / "swagger.css")
    # Usa swagger-ui via CDN
    html = f"""
<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{t['title']} • Swagger</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css" />
  <style>
    body {{ margin: 0; background: #070A12; }}
    .top {{ padding: 14px 16px; border-bottom: 1px solid rgba(255,255,255,.08); color: #E8ECFF; font-family: ui-sans-serif, system-ui; }}
    .top a {{ color: #E8ECFF; text-decoration: none; margin-right: 10px; }}
    {swagger_css}
  </style>
</head>
<body>
  <div class="top">
    <a href="?page=home&lang={lang}">← {t['nav_home']}</a>
    <a href="?page=redoc&lang={lang}">{t['nav_redoc']}</a>
    <a href="?page=openapi&lang={lang}">{t['nav_json']}</a>
  </div>
  <div id="swagger-ui"></div>

  <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    const spec = {json.dumps(openapi_spec)};
    window.ui = SwaggerUIBundle({{
      spec,
      dom_id: '#swagger-ui',
      deepLinking: true,
      docExpansion: 'list',
      defaultModelsExpandDepth: -1,
      displayRequestDuration: true
    }});
  </script>
</body>
</html>
"""
    components.html(html, height=900, scrolling=True)


# -----------------------
# ReDoc embutido
# -----------------------
def render_redoc(openapi_spec: Dict[str, Any], lang: str, t: Dict[str, str]):
    html = f"""
<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{t['title']} • ReDoc</title>
  <style>
    body {{ margin: 0; background: #070A12; font-family: ui-sans-serif, system-ui; color: #E8ECFF; }}
    .top {{ padding: 14px 16px; border-bottom: 1px solid rgba(255,255,255,.08); }}
    .top a {{ color: #E8ECFF; text-decoration: none; margin-right: 10px; }}
    .wrap {{ padding: 16px; }}
    .redoc-wrap {{
      border: 1px solid rgba(255,255,255,.08);
      border-radius: 18px;
      overflow: hidden;
      background: #0B1020;
      box-shadow: 0 10px 40px rgba(0,0,0,.35);
    }}
    #redoc-container {{ height: 820px; }}
  </style>
</head>
<body>
  <div class="top">
    <a href="?page=home&lang={lang}">← {t['nav_home']}</a>
    <a href="?page=swagger&lang={lang}">{t['nav_swagger']}</a>
    <a href="?page=openapi&lang={lang}">{t['nav_json']}</a>
  </div>

  <div class="wrap">
    <div class="redoc-wrap">
      <div id="redoc-container"></div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js"></script>
  <script>
    const spec = {json.dumps(openapi_spec)};
    Redoc.init(spec, {{
      theme: {{
        colors: {{
          primary: {{ main: "#115482" }},
          success: {{ main: "#3C7CAA" }},
          error: {{ main: "#E39749" }},
          text: {{ primary: "#E8ECFF", secondary: "#CFD7FF" }},
          http: {{
            get: "#3C7CAA",
            post: "#E39749",
            put: "#3C7CAA",
            delete: "#E39749"
          }}
        }},
        typography: {{
          fontFamily: "ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial",
          headings: {{ fontFamily: "ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial" }}
        }},
        sidebar: {{
          backgroundColor: "#0B1020",
          textColor: "#CFD7FF"
        }},
        rightPanel: {{
          backgroundColor: "#0B1020",
          textColor: "#E8ECFF"
        }}
      }}
    }}, document.getElementById("redoc-container"));
  </script>
</body>
</html>
"""
    components.html(html, height=900, scrolling=True)


# -----------------------
# Lazy imports (pesado só quando precisa)
# -----------------------
@st.cache_resource
def get_knowledge_history_func():
    # Import leve na maioria dos casos (se knowledge/base.py for simples)
    from knowledge.base import get_knowledge_history  # type: ignore
    return get_knowledge_history


def run_mapek_cycle_safe(payload: Dict[str, Any]) -> Any:
    """
    Importa run_mapek_cycle apenas quando o usuário executa /data.
    Isso evita startup lento por causa de TensorFlow.
    """
    # Import pesado só aqui
    from core.mapek_loop import run_mapek_cycle  # type: ignore

    # Tenta usar seu modelo Pydantic Data (se existir)
    try:
        from schemas.data_models import Data  # type: ignore
        obj = Data(**payload)
        return run_mapek_cycle(obj)
    except Exception:
        # Fallback: passa dict se sua função aceitar; caso não aceite, o erro aparece para ajuste.
        return run_mapek_cycle(payload)  # type: ignore


# -----------------------
# App Streamlit
# -----------------------
st.set_page_config(page_title="MILESTONE", layout="wide")
inject_css()

# Query params
qp = st.query_params
lang = qp.get("lang", "pt")
page = qp.get("page", "home")
if lang not in I18N:
    lang = "pt"
t = I18N[lang]

# Logos (embutidos como data URI para manter estilo em qualquer ambiente)
lab_logo_uri = _img_to_data_uri(STATIC_DIR / "lab-logo.png") or "data:image/png;base64,"
uni_logo_uri = _img_to_data_uri(STATIC_DIR / "uni-logo.png") or lab_logo_uri or "data:image/png;base64,"

openapi_spec = build_openapi(lang=lang, lab_logo_data_uri=lab_logo_uri if lab_logo_uri and lab_logo_uri != "data:image/png;base64," else None)

# Sidebar (navegação)
with st.sidebar:
    st.markdown(f"### {t['ui_title']}")
    st.caption(t["ui_hint"])

    lang_sel = st.selectbox("Language", ["pt", "en"], index=0 if lang == "pt" else 1)
    page_map = {
        "home": t["page_home"],
        "swagger": t["page_swagger"],
        "redoc": t["page_redoc"],
        "openapi": t["page_openapi"],
        "endpoints": t["page_endpoints"],
    }
    page_sel_label = st.radio("Navegação", list(page_map.values()), index=list(page_map.keys()).index(page) if page in page_map else 0)

    # Atualiza query params ao mudar
    inv_page_map = {v: k for k, v in page_map.items()}
    new_page = inv_page_map[page_sel_label]
    if new_page != page or lang_sel != lang:
        st.query_params.update({"page": new_page, "lang": lang_sel})
        st.rerun()

    st.divider()
    st.markdown("**Assets (opcional)**")
    st.code("static/theme.css\nstatic/swagger.css\nstatic/lab-logo.png\nstatic/uni-logo.png")


# Render das páginas
if page == "home":
    # Landing HTML preservada
    html = build_landing_html(lang=lang, t=t, lab_logo_uri=lab_logo_uri, uni_logo_uri=uni_logo_uri)
    components.html(html, height=1120, scrolling=True)

elif page == "swagger":
    render_swagger_ui(openapi_spec=openapi_spec, lang=lang, t=t)

elif page == "redoc":
    render_redoc(openapi_spec=openapi_spec, lang=lang, t=t)

elif page == "openapi":
    st.subheader(t["nav_json"])
    st.caption("Este JSON é gerado dentro do Streamlit para alimentar Swagger/ReDoc.")
    st.json(openapi_spec)
    st.download_button(
        label="Download openapi.json",
        data=json.dumps(openapi_spec, ensure_ascii=False, indent=2).encode("utf-8"),
        file_name="openapi.json",
        mime="application/json",
    )

elif page == "endpoints":
    st.subheader(t["page_endpoints"])
    st.caption("Aqui você testa os endpoints como funções dentro do Streamlit (sem servidor FastAPI).")

    colA, colB, colC = st.columns(3)

    with colA:
        st.markdown(f"### {t['health']}")
        if st.button("GET /health", use_container_width=True):
            st.json({"status": "ok", "name": APP_TITLE, "version": APP_VERSION})

    with colB:
        st.markdown(f"### {t['register']}")
        if st.button("GET /register", use_container_width=True):
            st.json({"instance_id": str(uuid4())})

    with colC:
        st.markdown(f"### {t['history']}")
        if st.button("GET /database/history", use_container_width=True):
            try:
                get_hist = get_knowledge_history_func()
                st.json({"history": get_hist()})
            except Exception as e:
                st.error("Falha ao carregar histórico.")
                st.exception(e)

    st.divider()
    st.markdown(f"### {t['run_data']}")

    default_payload = {
        "instance_id": "demo",
        "timestamp": "2026-01-04T00:00:00Z",
        "metrics": {"cpu": 0.50, "ram": 0.70, "latency": 120},
    }
    raw = st.text_area(t["payload"], value=json.dumps(default_payload, ensure_ascii=False, indent=2), height=220)

    if st.button(t["run"], type="primary"):
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as e:
            st.error(f"JSON inválido: {e}")
        else:
            with st.spinner("Executando ciclo MAPE-K... (imports pesados acontecem aqui)"):
                try:
                    result = run_mapek_cycle_safe(payload)
                    # Se retornar Pydantic/obj com model_dump, tenta serializar
                    if hasattr(result, "model_dump"):
                        st.json(result.model_dump())
                    elif hasattr(result, "dict"):
                        st.json(result.dict())
                    else:
                        st.json(result)
                except Exception as e:
                    st.error("Falha ao executar /data.")
                    st.exception(e)

else:
    st.error("Página inválida.")
