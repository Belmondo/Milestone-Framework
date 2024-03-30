import Implementation.SecurityModule;
import Implementation.SecurityNFR;

import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

public class Main {

    public static void main(String[] args) {

        SecurityNFR securityNFR = new SecurityNFR();
        securityNFR.increaseIndex(2);
        securityNFR.increaseIndex(3);


    }

}