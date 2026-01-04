import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import class_weight
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical
import os

# Garante que o diretório para salvar os modelos exista
os.makedirs("saved_models", exist_ok=True)

# ------------------------------------------------------------------
# 1. TREINAMENTO DO MODELO DE ESTADO (Bom/Ruim)
# ------------------------------------------------------------------
print("Iniciando treinamento do Modelo de Estado...")
dados_treino = np.array([
    [1.73, 0.95, 1.0], [1.56, 0.78, 0.0], [0.26, 0.78, 0.0],
    [1.02, 0.57, 0.0], [1.40, 0.90, 1.0], [0.60, 0.30, 0.0],
    [1.10, 0.85, 1.0], [0.80, 0.50, 0.0]
], dtype=float)

X_state = dados_treino[:, :2]
y_state = dados_treino[:, 2]

X_state_train, _, y_state_train, _ = train_test_split(
    X_state, y_state, test_size=0.3, random_state=42
)

scaler_state = StandardScaler()
X_state_train = scaler_state.fit_transform(X_state_train)

weights_state = class_weight.compute_class_weight(
    class_weight="balanced", classes=np.unique(y_state_train), y=y_state_train
)
class_weights_state = dict(enumerate(weights_state))

state_model = Sequential([
    Dense(32, activation='relu', input_shape=(X_state_train.shape[1],)),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])
state_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
early_stopping_state = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Treinando com todos os dados disponíveis para o modelo final
full_X_state_scaled = scaler_state.fit_transform(X_state)
state_model.fit(
    full_X_state_scaled, y_state,
    epochs=80, batch_size=8, validation_split=0.2,
    class_weight=class_weights_state, callbacks=[early_stopping_state], verbose=1
)

# Salvar o modelo e o scaler
state_model.save("saved_models/state_model.keras")
joblib.dump(scaler_state, "saved_models/scaler_state.pkl")
print("Modelo de Estado e scaler salvos com sucesso!")

# ------------------------------------------------------------------
# 2. TREINAMENTO DO MODELO DE PLANEJAMENTO (POLICY NETWORK)
# ------------------------------------------------------------------
print("\nIniciando treinamento do Modelo de Planejamento...")
rng = np.random.default_rng(42)
N = 600
synthetic_tb = rng.uniform(0.1, 2.5, size=N)
synthetic_rc = rng.uniform(0.0, 1.0, size=N)
synthetic_cp = rng.uniform(0.0, 1.0, size=N)

state_inputs = np.column_stack([synthetic_tb, synthetic_rc])
state_inputs_scaled = scaler_state.transform(state_inputs)
prob_ruim = state_model.predict(state_inputs_scaled, verbose=0).ravel()

Xp = np.column_stack([synthetic_tb, synthetic_rc, synthetic_cp, prob_ruim])

y_policy = np.zeros(N, dtype=int)
for i in range(N):
    tb, rc, cp, p = Xp[i]
    if p > 0.7 or tb > 1.2 or rc > 0.85: y_policy[i] = 2
    elif p > 0.45 or tb > 0.9 or rc > 0.6: y_policy[i] = 1
    else: y_policy[i] = 0

scaler_policy = StandardScaler()
Xp_scaled = scaler_policy.fit_transform(Xp)

policy_model = Sequential([
    Dense(32, activation='relu', input_shape=(Xp_scaled.shape[1],)),
    Dense(16, activation='relu'),
    Dense(3, activation='softmax')
])
policy_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
early_stopping_policy = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

policy_model.fit(
    Xp_scaled, to_categorical(y_policy, num_classes=3),
    epochs=80, batch_size=16, validation_split=0.2,
    callbacks=[early_stopping_policy], verbose=1
)

# Salvar o modelo e o scaler
policy_model.save("saved_models/policy_model.keras")
joblib.dump(scaler_policy, "saved_models/scaler_policy.pkl")
print("Modelo de Planejamento e scaler salvos com sucesso!")