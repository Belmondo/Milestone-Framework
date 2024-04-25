import '../models/NFRDefinition.dart';
import 'dart:collection';

class ThreshholdBalance {
  static ThreshholdBalance? _threshholdBalance;
  static List<NFRDefinition>? _listOfNFR;

  void startBalance() {
    if (_threshholdBalance == null) {
      _threshholdBalance = ThreshholdBalance();
    }
  }

  static ThreshholdBalance? getBalance() {
    return _threshholdBalance;
  }

  // Sobrecarga para mudança de balanço baseado em dois NFRs
  static void changeNFRBalance(
      String NFRName, int index, String SecondNFRName, int Secondindex) {
    // Implementação para mudança de balanço baseado em dois NFRs
  }

  // Sobrecarga para mudança apenas com nome e índice
  static void changeNFRBalanceWithNameIndex(String NFRName, int index) {
    // Implementação para mudança apenas com nome e índice
  }

  // Sobrecarga para mudança apenas com objeto e índice
  static void changeNFRBalanceWithObjectIndex(NFRDefinition NFR, int index) {
    // Implementação para mudança apenas com objeto e índice
  }

  // Sobrecarga para mudança de índice com base na posição da lista recebida
  static void changeNFRBalanceWithList(List<NFRDefinition> NFR) {
    // Implementação para mudança de índice com base na posição da lista recebida
  }
}
