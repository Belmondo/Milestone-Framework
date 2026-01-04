from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from uuid import uuid4

from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html

from schemas.data_models import Data, InstanceIDResponse, Neural_Network_Response
from knowledge.base import get_knowledge_history
from core.mapek_loop import run_mapek_cycle


APP_TITLE = "MILESTONE: Framework para Monitoramento Contínuo de Desempenho em Sistemas Auto-Adaptativos."
APP_VERSION = "0.1.0"

# Dicionário de Traduções (I18N)
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
        "arch_text": "A arquitetura adotada é cliente–servidor, garantindo separação clara de responsabilidades: o cliente faz a interface de comunicação com o sistema gerenciado, enquanto o servidor (sistema gerenciador) processa solicitações e devolve respostas, favorecendo independência de plataforma e escalabilidade. O Milestone é inspirado no MAPE-K e cada etapa foi desenhada com responsabilidade única, interfaces bem definidas e desacoplamento, permitindo manutenção/testes por componente e reuso de módulos em diferentes contextos. A comunicação entre etapas segue o padrão Observer, com troca assíncrona de mensagens, e o framework prevê invocação agendada, por eventos ou em batches, facilitando incorporação em pipelines. Do ponto de vista de modularização, o texto descreve módulos alinhados às fases do ciclo (Monitoramento, Análise, Planejamento e Conhecimento), com responsabilidades bem definidas e possibilidade de extensão/substituição independente. ",
        "footer": "© {title} • v{version}",
        "tag_main": "Operações Principais",
        "author_description": "Programa de Mestrado e Doutorado em Ciências da Computação - Universidade Federal do Ceará",
        "PhD_advisor":  "(Orientadora) — Programa de Mestrado e Doutorado em Ciências da Computação - Universidade Federal do Ceará",
        "great": "Grupo de Redes de Computadores, Engenharia de Software e Sistemas - UFC"
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
        "arch_text": "Milestone adopts a client–server architecture: the client interfaces with the managed system, while the server (manager) processes requests and returns responses, supporting platform independence and scalability. Stages are inspired by MAPE-K and follow single-responsibility, decoupled interfaces, and modular reuse; stages communicate via the Observer pattern with asynchronous messaging, and the framework supports scheduled/event/batch invocation for pipeline integration. The implementation is organized into modules aligned with monitoring, analysis, planning, and knowledge responsibilities, enabling independent extension/substitution. ",
        "footer": "© {title} • v{version}",
        "tag_main": "Main Operations",
        "author_description": "Master’s and Doctoral Program in Computer Science — Federal University of Ceara",
        "PhD_advisor":  "(PhD advisor) — Master and Doctoral Program in Computer Science — Federal University of Ceara",
        "great": "Group of Computer Networks, Software Engineering and Systems"
    }
}

app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description=I18N["pt"]["description"],
    docs_url=None,   # desliga docs padrão
    redoc_url=None,  # desliga redoc padrão
    openapi_url=None # desliga openapi padrão para gerarmos dinamicamente
)

# Arquivos estáticos (CSS + logos)
app.mount("/static", StaticFiles(directory="static"), name="static")


# -----------------------
# OpenAPI Dinâmico (Suporte a PT/EN)
# -----------------------
@app.get("/openapi.json", include_in_schema=False)
def get_open_api_endpoint(lang: str = "pt"):
    if lang not in I18N: lang = "pt"
    texts = I18N[lang]

    schema = get_openapi(
        title=texts["title"],
        version=APP_VERSION,
        description=texts["description"],
        routes=app.routes,
    )

    # Logo do laboratório na spec (ReDoc exibe bem)
    schema["info"]["x-logo"] = {
        "url": "/static/lab-logo.png",
        "altText": "Laboratório"
    }

    # Tradução das Tags (se inglês)
    if lang == "en":
        pt_tag = I18N["pt"]["tag_main"]
        en_tag = I18N["en"]["tag_main"]
        for path, methods in schema.get("paths", {}).items():
            for method, details in methods.items():
                if "tags" in details:
                    # Troca a tag PT pela EN se encontrar
                    details["tags"] = [en_tag if t == pt_tag else t for t in details["tags"]]

    return schema


# -----------------------
# Landing page (/)
# -----------------------
@app.get("/", include_in_schema=False)
def root(lang: str = "pt"):
    if lang not in I18N: lang = "pt"
    t = I18N[lang]

    return HTMLResponse(f"""
<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{t['title']}</title>
  <link rel="stylesheet" href="/static/theme.css"/>
  <link rel="icon" href="/static/lab-logo.png"/>
</head>

<body>
  <header class="topbar">
    <div class="container topbar-inner">
      <div class="brand">
        <div class="logos">
          <img src="/static/lab-logo.png" alt="Logo do laboratório" class="logo logo-lab"/>
          <img src="/static/uni-logo.png" alt="Logo da universidade" class="logo logo-uni"/>
        </div>
        <div class="brand-text">
          <div class="badge">MAPE-K • Neural Control • FastAPI</div>
          <h1>{t['title']}</h1>
          <p class="subtitle">{t['subtitle']}</p>
        </div>
      </div>

      <nav class="nav">
        <a class="btn" href="/docs?lang={lang}">{t['nav_swagger']}</a>
        <a class="btn" href="/redoc?lang={lang}">{t['nav_redoc']}</a>
        <a class="btn btn-ghost" href="/openapi.json?lang={lang}">{t['nav_json']}</a>
        
        <!-- Language Switcher -->
        <div style="margin-left: 15px; display: inline-flex; gap: 12px; align-items: center;">
            <a href="?lang=pt" title="Português">
                <img src="https://flagcdn.com/24x18/br.png" alt="PT" style="border-radius: 2px; opacity: {'1' if lang=='pt' else '0.4'}; transition: opacity .2s;">
            </a>
            <a href="?lang=en" title="English">
                <img src="https://flagcdn.com/24x18/gb.png" alt="EN" style="border-radius: 2px; opacity: {'1' if lang=='en' else '0.4'}; transition: opacity .2s;">
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
          <!-- ✅ ESPAÇO PARA VOCÊ INSERIR O TEXTO -->
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
          <img src="/static/lab-logo.png" alt="Selo do laboratório" class="seal-logo"/>
          <div class="seal-text">
            <div class="seal-title">GREat</div>
            <div class="seal-sub">{t['great']}</div>
          </div>
        </div>

        <div class="card inner">
          <h3>{t['authors_title']}</h3>
          <p class="muted" style="text-align: justify !important;">
            <!-- ESPAÇO PARA VOCÊ INSERIR OS AUTORES -->
            👨‍🎓 <strong>Belmondo Rodrigues Aragão Junior</strong> — {t['author_description']}<br/><br/>
            👩🏻‍🏫 <strong>Profa. Dra. Rossana M. C. Andrade</strong> {t['PhD_advisor']}
          </p>
        <!-- 
          <h3 class="mt">{t['citation_title']}</h3>
          <p class="muted">
            <!-- ✅ ESPAÇO PARA VOCÊ INSERIR COMO CITAR 
            [Inserir referência ABNT/IEEE e link do repositório/publicação]
          </p>
          -->
        </div>
      </div>
    </section>

    <section class="card mt">
      <h2>{t['arch_title']}</h2>
      <p class="muted" style="text-align: justify !important;">
        <!-- ✅ ESPAÇO PARA VOCÊ INSERIR A EXPLICAÇÃO -->
        {t['arch_text']}
      </p>
    </section>

    <footer class="footer">
      <div class="muted">{t['footer'].format(title=t['title'], version=APP_VERSION)}</div>
    </footer>
  </main>
</body>
</html>
""")


# -----------------------
# Swagger (/docs) com a mesma identidade
# -----------------------
@app.get("/docs", include_in_schema=False)
def swagger_docs(lang: str = "pt"):
    if lang not in I18N: lang = "pt"
    t = I18N[lang]

    return get_swagger_ui_html(
        openapi_url=f"/openapi.json?lang={lang}",
        title=f"{t['title']} • Swagger",
        swagger_favicon_url="/static/lab-logo.png",
        swagger_css_url="/static/swagger.css",
        swagger_ui_parameters={
            "docExpansion": "list",
            "defaultModelsExpandDepth": -1,
            "displayRequestDuration": True,
            "filter": False,
        },
    )





# -----------------------
# ReDoc (/redoc) com header igual + tema alinhado
# -----------------------
@app.get("/redoc", include_in_schema=False)
def redoc_docs(lang: str = "pt"):
    if lang not in I18N: lang = "pt"
    t = I18N[lang]

    return HTMLResponse(f"""
<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{t['title']} • ReDoc</title>
  <link rel="stylesheet" href="/static/theme.css"/>
  <link rel="icon" href="/static/lab-logo.png"/>
  <style>
    .redoc-wrap {{
      margin-top: 18px;
      border: 1px solid var(--border);
      border-radius: 18px;
      overflow: hidden;
      background: var(--card);
      box-shadow: 0 10px 40px rgba(0,0,0,.35);
    }}
    #redoc-container {{
      height: calc(100vh - 140px);
    }}
  </style>
</head>

<body>
  <header class="topbar">
    <div class="container topbar-inner">
      <div class="brand">
        <div class="logos">
          <img src="/static/lab-logo.png" alt="Logo do laboratório" class="logo logo-lab"/>
          <img src="/static/uni-logo.png" alt="Logo da universidade" class="logo logo-uni"/>
        </div>
        <div class="brand-text">
          <div class="badge">MAPE-K • Neural Control • FastAPI</div>
          <h1>{t['title']}</h1>
          <p class="subtitle">{t['nav_redoc']}</p>
        </div>
      </div>

      <nav class="nav">
        <a class="btn" href="/?lang={lang}">{t['nav_home']}</a>
        <a class="btn" href="/docs?lang={lang}">{t['nav_swagger']}</a>
        <a class="btn btn-ghost" href="/openapi.json?lang={lang}">{t['nav_json']}</a>
        
        <div style="margin-left: 15px; display: inline-flex; gap: 12px; align-items: center;">
            <a href="?lang=pt" title="Português">
                <img src="https://flagcdn.com/24x18/br.png" alt="PT" style="border-radius: 2px; opacity: {'1' if lang=='pt' else '0.4'}; transition: opacity .2s;">
            </a>
            <a href="?lang=en" title="English">
                <img src="https://flagcdn.com/24x18/gb.png" alt="EN" style="border-radius: 2px; opacity: {'1' if lang=='en' else '0.4'}; transition: opacity .2s;">
            </a>
        </div>
      </nav>
    </div>
  </header>

  <main class="container">
    <div class="redoc-wrap">
      <div id="redoc-container"></div>
    </div>
  </main>

  <script src="https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js"></script>
  <script>
    Redoc.init(
      "/openapi.json?lang={lang}",
      {{
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
      }},
      document.getElementById("redoc-container")
    );
  </script>
</body>
</html>

""")


# -----------------------
# Endpoints (os seus)
# -----------------------
@app.get("/health", include_in_schema=False)
def health():
    return {"status": "ok", "name": APP_TITLE, "version": APP_VERSION}

#@app.get("/register", response_model=InstanceIDResponse)
@app.get("/register", response_model=InstanceIDResponse, tags=["Operações Principais"])
def register_instance():
    unique_id = str(uuid4())
    return InstanceIDResponse(instance_id=unique_id)

#@app.get("/database/history")
@app.get("/database/history", tags=["Operações Principais"])
def get_base():
    return {"history": get_knowledge_history()}

#@app.post("/data", response_model=Neural_Network_Response)
@app.post("/data", response_model=Neural_Network_Response, tags=["Operações Principais"])
def process_data(dados: Data):
    """
    Endpoint principal para receber dados de monitoramento e iniciar o ciclo MAPE-K.
    """
    return run_mapek_cycle(dados)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

    