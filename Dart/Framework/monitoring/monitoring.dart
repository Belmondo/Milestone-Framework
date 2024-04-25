import '../models/ISelfAdaptiveStep.dart';

class Monitoring implements ISelfAdaptiveStep {
  static List<ISelfAdaptiveStep> listOfAnalyzes = [];

  static void updateNFRMeasurements(String NFRName, var updateValue) {
    // Implementação da atualização de medições para int
  }

  static void unwatchNFR() {
    // Implementação para interromper monitoramento de NFR
  }

  @override
  void notifyNextStep() {
    // Implementação do método de notificação de próximo passo
    throw UnimplementedError("Unimplemented method 'notifyNextStep'");
  }

  @override
  void registerNextStep(ISelfAdaptiveStep selfAdaptiveStep) {
    listOfAnalyzes.add(selfAdaptiveStep);
  }
}
