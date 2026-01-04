# Base de conhecimento em memória (Singleton implícito do Python)
knowledge_base = {
    "history": [],
    "thresholds": {
        "estado": {0: "Bom", 1: "Ruim"}
    }
}

def update_knowledge(data_sample, estado_idx, acao, confianca):
    """Adiciona um novo registro ao histórico da base de conhecimento."""
    estado_str = knowledge_base["thresholds"]["estado"][estado_idx]
    
    registro = {
        "entrada": {
            "time_behaviour": data_sample[0],
            "resource": data_sample[1],
            "capacity": data_sample[2]
        },
        "estado_analisado": estado_str,
        "confianca_estado_ruim": float(round(confianca, 4)),
        "acao_planejada": acao
    }
    knowledge_base["history"].append(registro)
    print(f"[CONHECIMENTO] Novo registro adicionado: {registro}")

def get_knowledge_history():
    """Retorna o histórico completo."""
    return knowledge_base["history"]