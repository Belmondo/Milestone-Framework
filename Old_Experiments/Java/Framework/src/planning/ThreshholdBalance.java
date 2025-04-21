package planning;

import models.NFRDefinition;

import java.util.List;

public class ThreshholdBalance {

    private static ThreshholdBalance threshholdBalance;
    private static List<NFRDefinition> listOfNFR;

    public void startBalance(){

        if(threshholdBalance == null){
            threshholdBalance = new ThreshholdBalance();
        }
    }

    public static ThreshholdBalance getBalance(){
        return threshholdBalance;
    }

    //sobrecarga para mudança de balanço baseado em dois NFRS
    public static void changeNFRBalance(String NFRName, int index, String SecondNFRName, int Secondindex){

    }

    //sobrecarca para mudança apenas com nome e índice
    public static void changeNFRBalance(String NFRName, int index){

    }

    //sobrecarga para mudança apenas com objeto e indice
    public static void changeNFRBalance(NFRDefinition NFR, int index){

    }
    //sobrecarga para mudança de índice com base na posição da lista recebida
    public static void changeNFRBalance(List<NFRDefinition> NFR){

    }




}
