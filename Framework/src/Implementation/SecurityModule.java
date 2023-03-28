package Implementation;

import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

public class SecurityModule {

    static String IV = "AAAAAAAAAAAAAAAA";
    static String textopuro = "Exemplo de texto puro";
    static String chaveencriptacao = "0123456789abcdef";
    public void implementCriptography(String criptoMethod){
        switch(criptoMethod){
            case "DES":
                doDES();
                break;
            case "AES":
                doAES();
                break;
            default:
                break;
        }
    }

    public void doDES(){
        long start = System.currentTimeMillis();
        try{

            KeyGenerator keygenerator = KeyGenerator.getInstance("DES");
            SecretKey chaveDES = keygenerator.generateKey();

            Cipher cifraDES;

            // Cria a cifra
            cifraDES = Cipher.getInstance("DES/ECB/PKCS5Padding");

            // Inicializa a cifra para o processo de encriptação
            cifraDES.init(Cipher.ENCRYPT_MODE, chaveDES);

            // Texto puro
            byte[] textoPuro = "Exemplo de texto puro".getBytes();

            System.out.println("Texto [Formato de Byte] : " + textoPuro);
            System.out.println("Texto Puro : " + new String(textoPuro));

            // Texto encriptado
            byte[] textoEncriptado = cifraDES.doFinal(textoPuro);

            System.out.println("Texto Encriptado : " + textoEncriptado);

            // Inicializa a cifra também para o processo de decriptação
            cifraDES.init(Cipher.DECRYPT_MODE, chaveDES);

            // Decriptografa o texto
            byte[] textoDecriptografado = cifraDES.doFinal(textoEncriptado);

            System.out.println("Texto Decriptografado : " + new String(textoDecriptografado));

            long finish = System.currentTimeMillis();

            System.out.println("Tempo: "+ (finish - start));

        }catch(NoSuchAlgorithmException e){
            e.printStackTrace();
        }catch(NoSuchPaddingException e){
            e.printStackTrace();
        }catch(InvalidKeyException e){
            e.printStackTrace();
        }catch(IllegalBlockSizeException e){
            e.printStackTrace();
        }catch(BadPaddingException e){
            e.printStackTrace();
        }
    }

    public void doAES(){
        long start = System.currentTimeMillis();
        try {

            System.out.println("Texto Puro: " + textopuro);

            byte[] textoencriptado = encrypt(textopuro, chaveencriptacao);

            System.out.print("Texto Encriptado: ");

            for (int i=0; i<textoencriptado.length; i++)
                System.out.print(new Integer(textoencriptado[i])+" ");

            System.out.println("");

            String textodecriptado = decrypt(textoencriptado, chaveencriptacao);

            System.out.println("Texto Decriptado: " + textodecriptado);

            long finish = System.currentTimeMillis();

            System.out.println("Tempo aes: " + (finish - start));

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static byte[] encrypt(String textopuro, String chaveencriptacao) throws Exception {
        Cipher encripta = Cipher.getInstance("AES/CBC/PKCS5Padding", "SunJCE");
        SecretKeySpec key = new SecretKeySpec(chaveencriptacao.getBytes("UTF-8"), "AES");
        encripta.init(Cipher.ENCRYPT_MODE, key,new IvParameterSpec(IV.getBytes("UTF-8")));
        return encripta.doFinal(textopuro.getBytes("UTF-8"));
    }

    public static String decrypt(byte[] textoencriptado, String chaveencriptacao) throws Exception{
        Cipher decripta = Cipher.getInstance("AES/CBC/PKCS5Padding", "SunJCE");
        SecretKeySpec key = new SecretKeySpec(chaveencriptacao.getBytes("UTF-8"), "AES");
        decripta.init(Cipher.DECRYPT_MODE, key,new IvParameterSpec(IV.getBytes("UTF-8")));
        return new String(decripta.doFinal(textoencriptado),"UTF-8");
    }

    public void setText(String text){
        this.textopuro = text;
    }
}
