import numpy as np
from ml.models import STATE_MODEL, SCALER_STATE

def analyze_state(data_sample: list):
    """Usa o modelo de estado para determinar a condição do sistema."""
    v = np.asarray(data_sample, dtype=float).ravel()
    x_state = v[:2].reshape(1, -1)  # Modelo de estado usa as 2 primeiras features
    x_state_scaled = SCALER_STATE.transform(x_state)
    
    p_bad = float(STATE_MODEL.predict(x_state_scaled, verbose=0)[0][0])
    estado_idx = int(p_bad >= 0.5)  # 1=Ruim, 0=Bom
    
    print(f"[ANALYZE] Probabilidade de estado 'Ruim': {p_bad:.4f}. Estado classificado como: {estado_idx}")
    return estado_idx, p_bad