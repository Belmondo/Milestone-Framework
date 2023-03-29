package Implementation;

import models.NFRDefinition;

public class SecurityNFR extends NFRDefinition {

    String name = "Security";
    int index = 0;

    SecurityModule securityModule = new SecurityModule();

    @Override
    public void increaseIndex(int index){

        switch (index){
            case 1:
                //sem criptografia
                break;
            case 2:
                securityModule.implementCriptography("AES");
                break;
            case 3:
                securityModule.implementCriptography("DES");
                break;
        }
    }

}
