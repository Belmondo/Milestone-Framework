package metrics.space;

public class MemoryUsage {



    //MainMemory
    //AuxiliaryMemory
    //Cache


        public long getTotalMemory(){
            return Runtime.getRuntime().totalMemory();
        }
        public long getFreeMemory(){
            return Runtime.getRuntime().freeMemory();
        }
        public long getMemoryUsage(){
            return Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
        }
}


