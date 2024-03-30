import 'NFRAbsModel.dart';

class NFRDefinition implements NFRAbsModel {
  late String _name;
  late int _index;

  void starNFRExecution() {}

  String getName() {
    return this._name;
  }

  int getIndex() {
    return this._index;
  }

  void setName(String name) {
    this._name = name;
  }

  void setIndex(int index) {
    this._index = index;
  }

  @override
  void notifyMonitor() {
    // TODO: implement notifyMonitor
  }
}
