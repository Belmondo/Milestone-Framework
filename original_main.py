from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from uuid import uuid4

from schemas.data_models import Data, InstanceIDResponse, Neural_Network_Response
from knowledge.base import get_knowledge_history
from core.mapek_loop import run_mapek_cycle

app = FastAPI(
    title="Sistema Autônomo com MAPE-K",
    description="Uma API que utiliza Redes Neurais para monitorar e gerenciar um sistema."
)

@app.get("/", include_in_schema=False)
#def root():
#    return {"message": "Bem-vindo ao Sistema Autônomo MAPE-K"}
def root():
    return HTMLResponse("""
<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Sistema Autônomo com MAPE-K</title>
  <style>
    body{margin:0;font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;
         background: radial-gradient(1200px 600px at 20% 10%, #1f3bff22, transparent),
                     radial-gradient(900px 500px at 80% 30%, #00d4ff1f, transparent),
                     #0b1020; color:#e8ecff;}
    .wrap{max-width:980px;margin:0 auto;padding:64px 24px;}
    .card{background:#0f1733cc;border:1px solid #2a3b7a66;border-radius:18px;padding:28px;
          box-shadow: 0 10px 40px #00000055;}
    .badge{display:inline-block;padding:6px 10px;border-radius:999px;background:#1b2a5f;border:1px solid #2a3b7a;
           font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#b8c6ff;}
    h1{margin:14px 0 10px;font-size:34px;line-height:1.1;}
    p{margin:0 0 18px;color:#cfd7ff;line-height:1.6;}
    .grid{display:grid;grid-template-columns:1fr;gap:12px;margin-top:18px}
    @media (min-width:720px){.grid{grid-template-columns:1fr 1fr}}
    a.btn{display:block;text-decoration:none;padding:14px 16px;border-radius:14px;border:1px solid #2a3b7a;
          background:#121c3f;color:#e8ecff;font-weight:600}
    a.btn:hover{transform:translateY(-1px);background:#162451}
    .muted{margin-top:14px;font-size:13px;color:#97a6e8}
    code{background:#0b1020;border:1px solid #2a3b7a66;border-radius:8px;padding:2px 6px}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <span class="badge">MAPE-K • Neural Control • FastAPI</span>
      <h1>Sistema Autônomo com MAPE-K</h1>
      <p>
        API para monitoramento, análise, planejamento e execução de adaptações com suporte de redes neurais.
        Use a documentação para testar endpoints e entender o esquema OpenAPI.
      </p>
      <div class="grid">
        <a class="btn" href="/docs">Abrir Swagger UI (Docs interativa)</a>
        <a class="btn" href="/redoc">Abrir ReDoc (Documentação limpa)</a>
      </div>
      <div class="muted">
        Dica: verifique o estado da API em <code>/health</code> e o OpenAPI em <code>/openapi.json</code>.
      </div>
    </div>
  </div>
</body>
</html>
""")

@app.get("/register", response_model=InstanceIDResponse)
def register_instance():
    unique_id = str(uuid4())
    return InstanceIDResponse(instance_id=unique_id)

@app.get("/database/history")
def get_base():
    return {"history": get_knowledge_history()}

@app.post("/data", response_model=Neural_Network_Response)
def process_data(dados: Data):
    """
    Endpoint principal para receber dados de monitoramento e iniciar o ciclo MAPE-K.
    """
    return run_mapek_cycle(dados)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)