package metrics.usability;

public class TrainingTime {
    private long start;
    private long finish;
    public void startTraining(){
        start = System.currentTimeMillis();
    }
    public void endTraining(){
        finish = System.currentTimeMillis();
    }
    public long getTrainingTime(){
        return finish - start;
    }
}
