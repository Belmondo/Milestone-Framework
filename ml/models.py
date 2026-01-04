import joblib
from tensorflow.keras.models import load_model

# Carrega os modelos e scalers do disco uma única vez quando o módulo é importado
try:
    STATE_MODEL = load_model("saved_models/state_model.keras")
    SCALER_STATE = joblib.load("saved_models/scaler_state.pkl")

    POLICY_MODEL = load_model("saved_models/policy_model.keras")
    SCALER_POLICY = joblib.load("saved_models/scaler_policy.pkl")
    
    print("Modelos de ML carregados com sucesso.")
except Exception as e:
    print(f"Erro ao carregar os modelos: {e}")
    print("Certifique-se de executar o script 'training.py' primeiro.")
    STATE_MODEL, SCALER_STATE, POLICY_MODEL, SCALER_POLICY = None, None, None, None