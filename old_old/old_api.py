from fastapi import FastAPI, HTTPException
from uuid import uuid4
from pydantic import BaseModel, Field
from typing import Optional

#Milestone
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.utils import class_weight
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt


#instância da FASTAPI
app = FastAPI()

class InstanceIDResponse(BaseModel):
    instance_id: str

class Neural_Network_Response(BaseModel):
    comando: str

class Data(BaseModel):
    #Time behaviour - Degree to which the response time and throughput rates of a product or system, when performing its functions, meet requirements.
    time_behaviour: Optional[float] = Field(None, description="Optional value of time behaviour")
    #Resource utilization - Degree to which the amounts and types of resources used by a product or system, when performing its functions, meet requirements.
    resource: Optional[float] = Field(None, description="Optional value of resource utilization")
    #Capacity - Degree to which the maximum limits of a product or system parameter meet requirements.
    capacity: Optional[float] = Field(None, description="Optional value of capacity")

# ===================== Fase de Conhecimento (Modelo e Histórico) =====================
knowledge_base = {
        "history": [],
        "thresholds": {
        "estado": {
        0: "Bom",
        1: "Ruim"
        }
    }
}

# ===================== Treinamento da Rede Neural =====================
#dados_treino = np.array([[1.73, 0.95, 1.0], [1.56, 0.78, 0.0], [0.26, 0.78, 0.0], [1.02, 0.57, 0.0]])
dados_treino = np.array([[1.73, 0.95, 1.0], [1.56, 0.78, 0.0], [0.26, 0.78, 0.0], [1.02, 0.57, 0.0]])
X = dados_treino[:, :-1]
y = dados_treino[:, -1]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


weights = class_weight.compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weights = dict(enumerate(weights))


model = Sequential([
Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
Dense(16, activation='relu'),
Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
model.fit(X_train, y_train, epochs=50, batch_size=8, validation_split=0.2, class_weight=class_weights, callbacks=[early_stopping], verbose=0)

class Milestone():
    def update_knowledge(data, estado, acao, confianca):
        registro = {
        "entrada": data,
        "estado": knowledge_base["thresholds"]["estado"][estado],
        "confianca": round(confianca, 2),
        "acao": acao
        }
        knowledge_base["history"].append(registro)
        print(f"[CONHECIMENTO] {registro}")

    def monitor(dados: Data):
        time_behaviour, resource, capacidade = dados.time_behaviour, dados.resource, dados.capacity
        data_list = [float(time_behaviour), float(resource), float(capacidade)]
        return data_list
    



    #return [
     #   [0.5, 0.3, 0.6],
      #  [1.2, 0.8, 0.9],
       # [0.6, 0.4, 0.5],
        #[1.1, 0.9, 0.95],
        #[0.3, 0.2, 0.3]
        #]
        # #se possui apenas time_behaviour
        # if time_behaviour is not None and resource is None and capacity is None:
        #     comando = f"COMANDO_X valor={x:.2f}"
        # #se possui time_behaviour e resource
        # elif time_behaviour is not None and resource is not None and capacity is None:
        #     resultado = time_behaviour + resource
        #     comando = f"COMANDO_XY soma={resultado:.2f}"
        # #se possui os três parâmetros
        # elif time_behaviour is not None and resource is not None and capacity is not None:
        #     media = (time_behaviour + resource + capacity) / 3
        #     comando = f"COMANDO_XYZ media={media:.2f}"
        # #se não possui nenhum parâmetro
        # else:
        #     raise HTTPException(status_code=400, detail="Parâmetros inválidos")
        # return Neural_Network_Response(comando=comando)

    def analyze(data):
        #print([data[:2]])
        #print(data)
        #data_scaled = scaler.transform([data[:2]]) # Apenas tempo_resposta e uso_cpu são usados no treino
        #print(data_scaled)
        data = np.array(data).reshape(1, -1)   # força formato 2D
        data_scaled = scaler.transform(data[:, :2])  # pega apenas as duas features usadas no treino
        prediction = model.predict(data_scaled, verbose=0)[0][0]
        estado = 1 if prediction >= 0.5 else 0
        return estado, prediction
    def knowledge(self):
        pass
    def execute(acao):
        str = f"[EXECUTANDO] {acao}"
        print(f"[EXECUTANDO] {acao}")
        return Neural_Network_Response(comando=str)
    def planning(estado, cpu):
        if estado == 1:
            if cpu > 0.8:
                return "Redistribuir tarefas e alocar recursos."
            else:
                return "Monitorar atentamente a carga."
        return "Nenhuma ação necessária."
    
    def start(dados: Data):
        data_list = Milestone.monitor(dados=dados)
        print(data_list)
        for dado in data_list:
            estado, confianca = Milestone.analyze(dado) # Análise
            acao = Milestone.planning(estado, dado[1]) # Planejamento
            Milestone.update_knowledge(dado, estado, acao, confianca) # Conhecimento
            return Milestone.execute(acao) # Execução
            
    

#decorador de rota
@app.get("/")
def root():
    return {"message": "Hello World"}

#é preciso validar a chave
@app.get("/register", response_model=InstanceIDResponse)
def register_instance():
    unique_id = str(uuid4())
    return InstanceIDResponse(instance_id=unique_id)

@app.post("/database")
def update_base():
    pass

@app.post("/database")
def get_base():
    pass

@app.post("/data")
def send_data(dados: Data):
    return Milestone.start(dados=dados)



   




