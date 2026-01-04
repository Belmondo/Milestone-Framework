from fastapi import HTTPException
from schemas.data_models import Data

def monitor_data(dados: Data):
    """Valida e extrai os dados de entrada."""
    if dados.time_behaviour is None or dados.resource is None or dados.capacity is None:
        raise HTTPException(status_code=400, detail="Forneça time_behaviour, resource e capacity (3 floats).")
    try:
        tb = float(dados.time_behaviour)
        rc = float(dados.resource)
        cp = float(dados.capacity)
    except (TypeError, ValueError):
        raise HTTPException(status_code=400, detail="Entradas devem ser numéricas (floats).")
    
    print(f"[MONITOR] Dados recebidos: time_behaviour={tb}, resource={rc}, capacity={cp}")
    return [tb, rc, cp]