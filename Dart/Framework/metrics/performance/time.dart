abstract class Time {
  late int start;
  late int finish;

  void startTimer() {
    start = DateTime.now().millisecondsSinceEpoch;
  }

  void endTimer() {
    finish = DateTime.now().millisecondsSinceEpoch;
  }

  int getResponseTime() {
    return finish - start;
  }
}
