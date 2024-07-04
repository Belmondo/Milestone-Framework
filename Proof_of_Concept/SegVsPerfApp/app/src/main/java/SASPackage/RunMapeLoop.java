package SASPackage;

import android.os.AsyncTask;
import android.widget.Toast;

import SASPackage.Implementation.PerformanceNFR;
import SASPackage.Implementation.SecurityNFR;
import SASPackage.models.NFRDefinition;
import SASPackage.models.Threshold;
import SASPackage.planning.ThreshholdBalance;
import doutorado.poc.segvsperfapp.MainActivity;

import java.util.ArrayList;
import java.util.List;

public class RunMapeLoop {


    List<NFRDefinition> NFRImplemented = new ArrayList<>();

    SecurityNFR securityNFR = new SecurityNFR();
    PerformanceNFR performanceNFR = new PerformanceNFR();
    ThreshholdBalance threshholdBalance = new ThreshholdBalance();



    public void addNFR(NFRDefinition nfr){
        NFRImplemented.add(nfr);
    }



    public void runMapeLoop(){
        threshholdBalance.startBalance();
        //MainActivity.changeValues("Entrou no run");
        threshholdBalance.selfBalance();

    }





}
