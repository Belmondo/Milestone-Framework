package metrics.portability;

public class NumberOfSystems {

    //É NECESSÁRIO INSERIR ISSO NA FASE DE ANÁLISE E INTELIGÊNCIA
    //COM UMA CONEXÃO COM BANCO DE DADOS POR SISTEMA PARA GARANTIR A
    // ATUALIZAÇÃO DA QUANTIDADE DE SISTEMAS OPERACIONAIS RODANDO COM O SISTEMA


    String actual_OS;
    int desiredNumberOfOS = 0;

    int totalOfCoverage = 0;

    NumberOfSystems(){
        actual_OS = System.getProperties().getProperty("os.name").toString().toLowerCase();
    }

    public String getActual_OS(){
        return actual_OS;
    }

    public void setDesiredNumberOfOS(int desiredNumberOfOS){
        this.desiredNumberOfOS = desiredNumberOfOS;
    }

    public void OSCounter(){}
    public void OSRate(String [] OperationalSystems){
        this.totalOfCoverage = OperationalSystems.length;
    }
    public double getOSRate(){
        return totalOfCoverage/desiredNumberOfOS;
    }
}
