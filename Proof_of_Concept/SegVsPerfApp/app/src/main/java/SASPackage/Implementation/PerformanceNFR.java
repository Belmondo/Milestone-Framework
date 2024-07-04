package SASPackage.Implementation;

import SASPackage.Main;
import SASPackage.models.NFRDefinition;
import doutorado.poc.segvsperfapp.MainActivity;


public class PerformanceNFR extends NFRDefinition {

    String name = "Performance";
    int index = 0;

    public void increaseIndex(int index){
        switch (index){
            case 1:
                MainActivity.changeBackgroundColor(1);
                break;
            case 2:
                MainActivity.changeBackgroundColor(2);
                break;
            case 3:
                MainActivity.changeBackgroundColor(3);
                break;
        }
    }

}
