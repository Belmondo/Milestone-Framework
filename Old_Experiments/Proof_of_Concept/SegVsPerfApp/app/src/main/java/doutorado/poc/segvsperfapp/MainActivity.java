package doutorado.poc.segvsperfapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import SASPackage.RunMapeLoop;

public class MainActivity extends AppCompatActivity {

    static TextView textViewValoresAtuais;
    static LinearLayout layout;

    RunMapeLoop rmp = new RunMapeLoop();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textViewValoresAtuais = (TextView) findViewById(R.id.tvValoresAtuais);
        layout = findViewById(R.id.linear);


    }


    public void startSelfAdaptation(View view){
        //é necessário criar, dentro do RunMapeLoop, método que receba qual o objetivo do run
        //seja threshold ou apenas monitoramento dos requisitos não funcionais
        //exemplo: runMapeLoop.setObjective("threshold")
        //runMapeLoop.setObjective("monitoring")

        rmp.runMapeLoop();
    }


    /*void workOnThread(){
        MainActivity.this.runOnUiThread(new Runnable() {
            public void run() {
                Toast.makeText(MainActivity.this,"Iniciando Mape Loop", Toast.LENGTH_SHORT).show();

            }
        });
    }*/

    public static void changeValues(String valores){
        textViewValoresAtuais.setText("Valores Atuais: " + valores);
    }

    public static void changeBackgroundColor(int i){
        switch(i){
            case 1:
                layout.setBackgroundResource(R.color.green);
                changeMessage(1);
                break;
            case 2:
                layout.setBackgroundResource(R.color.cool);
                changeMessage(2);
                break;
            case 3:
                layout.setBackgroundResource(R.color.warm);
                changeMessage(3);
                break;
        }

    }

    public static void changeMessage(int i){
        switch(i){
            case 1:
                changeValues("Balanced Values");
                break;
            case 2:
                changeValues("Performance index 2 and Security index 1");
                break;
            case 3:
                changeValues("Performance index 1 and Security index 2");
                break;
        }

    }

    public static void changeMessageToPrint(int i){
        switch(i){
            case 1:
                Log.d("sas","Balanced Values");
                break;
            case 2:
                Log.d("sas","Performance index 2 e Security index 1");
                break;
            case 3:
                Log.d("sas","Performance index 1 e Security index 2");
                break;
        }

    }
}