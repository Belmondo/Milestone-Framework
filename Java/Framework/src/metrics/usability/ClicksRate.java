package metrics.usability;

public class ClicksRate {

    private int numberOfClicks;

    ClicksRate(){
        numberOfClicks = 0;
    }

    public void registerClick(){
        numberOfClicks ++;
    }

    public int getNumberOfClicks(){
        return numberOfClicks;
    }

}
