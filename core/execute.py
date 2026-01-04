from schemas.data_models import Neural_Network_Response

def execute_action(action: str):
    """Executa a ação planejada."""
    msg = f"[EXECUTE] {action}"
    print(msg)
    # Em um sistema real, aqui você executaria comandos, chamaria outras APIs, etc.
    return Neural_Network_Response(comando=msg)