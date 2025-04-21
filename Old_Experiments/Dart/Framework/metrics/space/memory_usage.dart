class MemoryUsage {
  int getTotalMemory() {
    return _getRuntime().totalMemory;
  }

  int getFreeMemory() {
    return _getRuntime().freeMemory;
  }

  int getMemoryUsage() {
    return _getRuntime().totalMemory - _getRuntime().freeMemory;
  }

  Runtime _getRuntime() {
    return Runtime();
  }
}

class Runtime {
  final int totalMemory;
  final int freeMemory;

  Runtime({this.totalMemory = 0, this.freeMemory = 0});
}
