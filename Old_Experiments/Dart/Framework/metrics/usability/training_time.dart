class TrainingTime {
  late int start;
  late int finish;

  void startTraining() {
    start = DateTime.now().millisecondsSinceEpoch;
  }

  void endTraining() {
    finish = DateTime.now().millisecondsSinceEpoch;
  }

  int getTrainingTime() {
    return finish - start;
  }
}
