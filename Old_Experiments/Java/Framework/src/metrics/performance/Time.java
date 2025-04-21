package metrics.performance;

abstract class Time {
    protected long start;
    protected long finish;

    public void startTimer(){
        start = System.currentTimeMillis();
    }
    public void endTimer(){
        finish = System.currentTimeMillis();
    }

    public long getResponseTime(){
        return finish - start;
    }
}
