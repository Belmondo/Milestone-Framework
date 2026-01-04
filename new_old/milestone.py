# #import numpy as np
# #import time
# #from sklearn.model_selection import train_test_split
# #from sklearn.preprocessing import StandardScaler
# #from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix, ConfusionMatrixDisplay
# #from sklearn.utils import class_weight
# #import tensorflow as tf
# #from tensorflow.keras.models import Sequential
# #from tensorflow.keras.layers import Dense
# #from tensorflow.keras.callbacks import EarlyStopping
# #import matplotlib.pyplot as plt


# #import mape_k_phases.monitor_phase as monitor
# #import mape_k_phases.analyze_phase as analyse
# #import mape_k_phases.know_phase as knowledge
# #import mape_k_phases.exec_phase as execute
# #import mape_k_phases.planning_phase as planning

# from pydantic import BaseModel, Field
# from typing import Optional

# class Neural_Network_Response(BaseModel):
#     comando: str

# class Data(BaseModel):
#     #Time behaviour - Degree to which the response time and throughput rates of a product or system, when performing its functions, meet requirements.
#     time_behaviour: Optional[float] = Field(None, description="Optional value of time behaviour")
#     #Resource utilization - Degree to which the amounts and types of resources used by a product or system, when performing its functions, meet requirements.
#     resource: Optional[float] = Field(None, description="Optional value of resource utilization")
#     #Capacity - Degree to which the maximum limits of a product or system parameter meet requirements.
#     capacity: Optional[float] = Field(None, description="Optional value of capacity")




# async def start(dados: Data):
#     pass
# def analyse():
#     pass

# def knowledge():
#     pass

# def execute():
#     pass

# def planning():
#     pass