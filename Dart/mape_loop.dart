import 'models/NFRAbsModel.dart';

class mape_loop {
  var nfr_list = {};

  get getList {
    return nfr_list;
  }

  void set nfr(NFRAbsModel nfrImplemented) {
    nfr_list.addAll(nfrImplemented as Map);
  }
}
