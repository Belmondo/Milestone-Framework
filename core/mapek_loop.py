from schemas.data_models import Data
from core.monitor import monitor_data
from core.analyze import analyze_state
from core.plan import plan_action
from core.execute import execute_action
from knowledge.base import update_knowledge

def run_mapek_cycle(dados: Data):
    """
    Ponto de interação que executa o ciclo MAPE-K completo.
    """
    # 1. Monitor
    sample = monitor_data(dados)
    
    # 2. Analyze
    estado, p_bad = analyze_state(sample)
    
    # 3. Plan
    acao = plan_action(sample, p_bad)
    
    # 4. Update Knowledge Base
    update_knowledge(sample, estado, acao, p_bad)
    
    # 5. Execute
    return execute_action(acao)