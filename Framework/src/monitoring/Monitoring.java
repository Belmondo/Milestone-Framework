package monitoring;


import java.util.List;

import models.ISelfAdaptiveStep;

public class Monitoring implements ISelfAdaptiveStep {

    private static List<ISelfAdaptiveStep> lisftOfAnalyzes;


    public static void updateNFRMeasurements(String NFRName, int updateValue){

    }

    public static void updateNFRMeasurements(String NFRName, double updateValue){

    }


    public static void unwatchNFR(){

    }

    @Override
    public void notifyNextStep() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'notifyNextStep'");
    }

    @Override
    public void registerNextStep(ISelfAdaptiveStep selfAdaptiveStep) {
        lisftOfAnalyzes.add(selfAdaptiveStep);
    }


}
