package models;

public class NFRDefinition extends NFRAbsModel {

    //criar duas classes, uma pra segurança e outra pra desempenho
    //mudar os thresholdsbalance de cada um
    //enviar os dados do acelerometro de maneira criptografada para o servidor e esperar um ack do servidor para
    //mudar a cor da aplicação

    private String name;
    private int index;

    public void starNFRExecution(){

    }

    public String getName(){
        return this.name;
    }

    public int getIndex(){
        return this.index;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setIndex(int index){
        this.index = index;
    }


}
