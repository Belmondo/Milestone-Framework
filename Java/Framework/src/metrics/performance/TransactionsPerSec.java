package metrics.performance;

public class TransactionsPerSec extends Time{

    private int reqs = 0;

    public void setReq(){
        reqs++;
    }
    public int getReqNumber(){
        return reqs;
    }

    public double calculateRatio(){
        return reqs/(finish-start);
    }
}
