# from fastapi import FastAPI, HTTPException
# from uuid import uuid4
# from pydantic import BaseModel, Field
# from typing import Optional

# # ====== ML / NN deps ======
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.utils import class_weight
# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# from tensorflow.keras.callbacks import EarlyStopping
# from tensorflow.keras.utils import to_categorical

# # ------------------------------------------------------------------
# # FASTAPI APP
# # ------------------------------------------------------------------
# app = FastAPI()

# class InstanceIDResponse(BaseModel):
#     instance_id: str

# class Neural_Network_Response(BaseModel):
#     comando: str

# class Data(BaseModel):
#     # 3 entradas (floats) exigidas pelo monitoramento
#     time_behaviour: Optional[float] = Field(None, description="Time behaviour (e.g., response time)")
#     resource:       Optional[float] = Field(None, description="Resource utilization")
#     capacity:       Optional[float] = Field(None, description="Capacity")

# # ------------------------------------------------------------------
# # KNOWLEDGE (base de conhecimento)
# # ------------------------------------------------------------------
# knowledge_base = {
#     "history": [],
#     "thresholds": {
#         "estado": {0: "Bom", 1: "Ruim"}
#     }
# }

# # ------------------------------------------------------------------
# # TREINAMENTO DA REDE NEURAL (estado: Bom/Ruim) — usando 2 FEATURES
# # ------------------------------------------------------------------
# # dados_treino: [feat1, feat2, label]
# dados_treino = np.array([
#     [1.73, 0.95, 1.0],
#     [1.56, 0.78, 0.0],
#     [0.26, 0.78, 0.0],
#     [1.02, 0.57, 0.0],
#     [1.40, 0.90, 1.0],
#     [0.60, 0.30, 0.0],
#     [1.10, 0.85, 1.0],
#     [0.80, 0.50, 0.0]
# ], dtype=float)

# X_state = dados_treino[:, :2]  # 2 features
# y_state = dados_treino[:, 2]   # label (0/1)

# X_state_train, X_state_test, y_state_train, y_state_test = train_test_split(
#     X_state, y_state, test_size=0.3, random_state=42
# )

# scaler_state = StandardScaler()
# X_state_train = scaler_state.fit_transform(X_state_train)
# X_state_test  = scaler_state.transform(X_state_test)

# weights_state = class_weight.compute_class_weight(
#     class_weight="balanced", classes=np.unique(y_state_train), y=y_state_train
# )
# class_weights_state = dict(enumerate(weights_state))

# state_model = Sequential([
#     Dense(32, activation='relu', input_shape=(X_state_train.shape[1],)),
#     Dense(16, activation='relu'),
#     Dense(1, activation='sigmoid')
# ])
# state_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# early_stopping_state = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
# state_model.fit(
#     X_state_train, y_state_train,
#     epochs=80,
#     batch_size=8,
#     validation_split=0.2,
#     class_weight=class_weights_state,
#     callbacks=[early_stopping_state],
#     verbose=0
# )

# # ------------------------------------------------------------------
# # PLANEJAMENTO INTELIGENTE (POLICY NETWORK)
# # Mapeia (time_behaviour, resource, capacity, prob_ruim) -> ação
# # Ações: 0="Nenhuma ação", 1="Monitorar", 2="Redistribuir"
# # Treino com dados sintéticos coerentes com políticas heurísticas.
# # ------------------------------------------------------------------
# ACTIONS = ["Nenhuma ação necessária.", "Monitorar atentamente a carga.", "Redistribuir tarefas e alocar recursos."]

# # gera dataset sintético para a política
# rng = np.random.default_rng(42)
# N = 600
# synthetic_tb = rng.uniform(0.1, 2.5, size=N)      # time_behaviour
# synthetic_rc = rng.uniform(0.0, 1.0, size=N)      # resource
# synthetic_cp = rng.uniform(0.0, 1.0, size=N)      # capacity

# # usando o modelo de estado para obter probabilidade de "Ruim"
# state_inputs = np.column_stack([synthetic_tb, synthetic_rc])
# state_inputs_scaled = scaler_state.transform(state_inputs)
# prob_ruim = state_model.predict(state_inputs_scaled, verbose=0).ravel()

# Xp = np.column_stack([synthetic_tb, synthetic_rc, synthetic_cp, prob_ruim])

# # rótulos de ação guiados por heurística
# # regra: se prob_ruim alta OU tb alto OU recurso alto -> agir forte (2)
# # senão se sinais moderados -> monitorar (1), caso contrário -> nenhuma (0)
# y_policy = np.zeros(N, dtype=int)
# for i in range(N):
#     tb, rc, cp, p = Xp[i]
#     if p > 0.7 or tb > 1.2 or rc > 0.85:
#         y_policy[i] = 2
#     elif p > 0.45 or tb > 0.9 or rc > 0.6:
#         y_policy[i] = 1
#     else:
#         y_policy[i] = 0

# # treina policy network
# Xp_train, Xp_test, yp_train, yp_test = train_test_split(Xp, y_policy, test_size=0.2, random_state=42)
# scaler_policy = StandardScaler()
# Xp_train = scaler_policy.fit_transform(Xp_train)
# Xp_test  = scaler_policy.transform(Xp_test)

# policy_model = Sequential([
#     Dense(32, activation='relu', input_shape=(Xp_train.shape[1],)),
#     Dense(16, activation='relu'),
#     Dense(3, activation='softmax')
# ])
# policy_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# early_stopping_policy = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
# policy_model.fit(
#     Xp_train, to_categorical(yp_train, num_classes=3),
#     epochs=80, batch_size=16, validation_split=0.2,
#     callbacks=[early_stopping_policy], verbose=0
# )

# # ------------------------------------------------------------------
# # MAPE-K IMPLEMENTAÇÃO
# # ------------------------------------------------------------------
# class Milestone:
#     @staticmethod
#     def update_knowledge(data_sample, estado, acao, confianca):
#         registro = {
#             "entrada": {
#                 "time_behaviour": data_sample[0],
#                 "resource": data_sample[1],
#                 "capacity": data_sample[2]
#             },
#             "estado": knowledge_base["thresholds"]["estado"][estado],
#             "confianca": float(round(confianca, 4)),
#             "acao": acao
#         }
#         knowledge_base["history"].append(registro)
#         print(f"[CONHECIMENTO] {registro}")

#     # ---------------- MONITOR ----------------
#     @staticmethod
#     def monitor(dados: Data):
#         if dados.time_behaviour is None or dados.resource is None or dados.capacity is None:
#             raise HTTPException(status_code=400, detail="Forneça time_behaviour, resource e capacity (3 floats).")
#         try:
#             tb = float(dados.time_behaviour)
#             rc = float(dados.resource)
#             cp = float(dados.capacity)
#         except (TypeError, ValueError):
#             raise HTTPException(status_code=400, detail="Entradas devem ser numéricas (floats).")
#         return [tb, rc, cp]

#     # ---------------- ANALYZE (NN) ----------------
#     @staticmethod
#     def analyze(data_sample):
#         v = np.asarray(data_sample, dtype=float).ravel()     # [tb, rc, cp]
#         x_state = v[:2].reshape(1, -1)                       # usa 2 features
#         x_state_scaled = scaler_state.transform(x_state)
#         p_bad = float(state_model.predict(x_state_scaled, verbose=0)[0][0])
#         estado = int(p_bad >= 0.5)                           # 1=Ruim, 0=Bom
#         return estado, p_bad

#     # ---------------- PLAN (NN) ----------------
#     @staticmethod
#     def planning(data_sample, p_bad: float):
#         v = np.asarray(data_sample, dtype=float).ravel()  # [tb, rc, cp]
#         x_policy = np.array([v[0], v[1], v[2], p_bad], dtype=float).reshape(1, -1)
#         x_policy_scaled = scaler_policy.transform(x_policy)
#         probs = policy_model.predict(x_policy_scaled, verbose=0)[0]
#         action_idx = int(np.argmax(probs))
#         return ACTIONS[action_idx]

#     # ---------------- EXECUTE ----------------
#     @staticmethod
#     def execute(acao):
#         msg = f"[EXECUTANDO] {acao}"
#         print(msg)
#         return Neural_Network_Response(comando=msg)

#     # ---------------- LOOP ----------------
#     @staticmethod
#     def start(dados: Data):
#         # Monitor
#         sample = Milestone.monitor(dados)
#         # Analyze → (estado, probabilidade de ruim)
#         estado, p_bad = Milestone.analyze(sample)
#         # Plan (policy network usa 3 features + p_bad)
#         acao = Milestone.planning(sample, p_bad)
#         # Knowledge
#         Milestone.update_knowledge(sample, estado, acao, p_bad)
#         # Execute
#         return Milestone.execute(acao)

# # ------------------------------------------------------------------
# # FASTAPI ROUTES
# # ------------------------------------------------------------------
# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/register", response_model=InstanceIDResponse)
# def register_instance():
#     unique_id = str(uuid4())
#     return InstanceIDResponse(instance_id=unique_id)

# @app.post("/database/update")
# def update_base():
#     return {"status": "ok"}

# @app.post("/database/get")
# def get_base():
#     return {"history": knowledge_base["history"]}

# @app.post("/data", response_model=Neural_Network_Response)
# def send_data(dados: Data):
#     return Milestone.start(dados)

# # ------------------------------------------------------------------
# # NOTAS
# # - O modelo de estado usa 2 features (time_behaviour, resource).
# # - O modelo de planejamento (policy) usa 3 features + p_bad.
# # - Para treinar tudo com 3 features no estado, re-treine state_model/scaler_state com 3 colunas.
# # - Você pode futuramente realimentar a policy com rótulos observados (sucesso/fracasso da ação),
# #   aproximando um contextual bandit ou RL leve.
# # ------------------------------------------------------------------


# #Justificar e explicar a linguagem
# #citar as APIs (Java, dart, python)
# #Falar sobre o FastAPI

# #SEAMS 2026
# #Verificar o Deadline

# #verificar a tese da rainara
# #medidas para validar a capacidade de adaptação

# #verificar cronograma
# #esboço do artigo do seams