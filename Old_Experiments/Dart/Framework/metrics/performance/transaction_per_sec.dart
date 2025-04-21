import 'time.dart';

class TransactionsPerSec extends Time {
  int reqs = 0;

  void setReq() {
    reqs++;
  }

  int getReqNumber() {
    return reqs;
  }

  double calculateRatio() {
    if (finish == null || start == null || start >= finish) {
      // Se o tempo de início ou término não estiverem definidos, ou se o tempo de início for maior ou igual ao tempo de término
      // retorna 0 para evitar divisão por zero
      return 0;
    }
    // Calcula a taxa de transações por segundo (reqs por milissegundo)
    return reqs / (finish - start);
  }
}
