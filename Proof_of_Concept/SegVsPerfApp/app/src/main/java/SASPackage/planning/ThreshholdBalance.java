package SASPackage.planning;

import SASPackage.Implementation.PerformanceNFR;
import SASPackage.models.NFRDefinition;
import doutorado.poc.segvsperfapp.MainActivity;


import java.util.List;

public class ThreshholdBalance {

    int max = 3;
    int min = 1;
    int range = max - min + 1;

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

    public static void addNFR(NFRDefinition nfr){
        listOfNFR.add(nfr);
    }

    public void selfBalance(){
        while (true){
            balancing(generateRandomRules());
        }
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

    public int generateRandomRules(){
        return (int)(Math.random() * range) + min;
    }

    public void balancing(int numberOfRules){
        MainActivity.changeMessageToPrint(numberOfRules);
    }





}
