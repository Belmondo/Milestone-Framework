import numpy as np
from ml.models import POLICY_MODEL, SCALER_POLICY
from config import ACTIONS

def plan_action(data_sample: list, p_bad: float):
    """Usa o modelo de planejamento para escolher uma ação."""
    v = np.asarray(data_sample, dtype=float).ravel()
    x_policy = np.array([v[0], v[1], v[2], p_bad], dtype=float).reshape(1, -1)
    x_policy_scaled = SCALER_POLICY.transform(x_policy)
    
    probs = POLICY_MODEL.predict(x_policy_scaled, verbose=0)[0]
    action_idx = int(np.argmax(probs))
    
    action = ACTIONS[action_idx]
    print(f"[PLAN] Ação planejada: '{action}' com confiança {np.max(probs):.4f}")
    return action