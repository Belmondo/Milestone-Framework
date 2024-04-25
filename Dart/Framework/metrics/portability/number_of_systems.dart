import 'dart:io';

class NumberOfSystems {
  late String actualOS;
  int desiredNumberOfOS = 0;
  int totalOfCoverage = 0;

  NumberOfSystems() {
    actualOS = Platform.operatingSystem.toLowerCase();
  }

  String getActualOS() {
    return actualOS;
  }

  void setDesiredNumberOfOS(int desiredNumberOfOS) {
    this.desiredNumberOfOS = desiredNumberOfOS;
  }

  void OSCounter() {
    // Implementação do contador de sistemas operacionais
  }

  void OSRate(List<String> operationalSystems) {
    totalOfCoverage = operationalSystems.length;
  }

  double getOSRate() {
    return totalOfCoverage / desiredNumberOfOS;
  }
}
