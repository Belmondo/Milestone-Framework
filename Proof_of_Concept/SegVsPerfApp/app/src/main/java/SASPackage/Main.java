package SASPackage;


import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

import SASPackage.Implementation.SecurityNFR;

public class Main {

    public static void main(String[] args) {

        SecurityNFR securityNFR = new SecurityNFR();
        securityNFR.increaseIndex(2);
        securityNFR.increaseIndex(3);


    }

}