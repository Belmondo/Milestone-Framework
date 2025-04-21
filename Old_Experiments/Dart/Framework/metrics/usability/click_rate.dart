class ClicksRate {
  int numberOfClicks = 0;

  ClicksRate() {
    numberOfClicks = 0;
  }

  void registerClick() {
    numberOfClicks++;
  }

  int getNumberOfClicks() {
    return numberOfClicks;
  }
}
