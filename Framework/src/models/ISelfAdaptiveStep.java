package models;

public interface ISelfAdaptiveStep{

    void registerNextStep(ISelfAdaptiveStep selfAdaptiveStep);
    void notifyNextStep();

    


}