package Implementation;

import models.NFRDefinition;

public class PerformanceNFR extends NFRDefinition {

    String name = "Performance";
    int index = 0;

    @Override
    public void increaseIndex(int index){
        switch (index){
            case 1:
                //mudanças de tela com velocidade
                break;
            case 2:
                //mudanças mais lentas
                break;
            case 3:
                //mudanças lentíssimas
                break;
        }
    }

}
