abstract class ISelfAdaptiveStep {
  void registerNextStep(ISelfAdaptiveStep selfAdaptiveStep);
  void notifyNextStep();
}
