import os
from utils import *
class embedding:

    def __init__(self, name, GW_metadata, resolution):
        self.GW_meta_data = GW_metadata
        self.name = name
        self.resolution = resolution

    def make_embedding_file(self, graphFile, order, samples):
        outFile = ('%s_order_3_samples_%dM.embedding'
                   % (graphFile.split(".")[0], samples))
        print(outFile)
        if not os.path.exists(outFile):
            embedding_files = run_LINE(graphFile, samples, order)
        oF = open(outFile)
        outFile2 = ('indexed_%s_order_3_samples_%dM.embedding'
                   % (graphFile.split(".")[0], samples))
        oF2 = open(outFile2, "a")
        oF = open(outFile)
        oF.readline()
        for line in oF.readlines():
            l = line.strip().split()
            node_num = l[0]
            emb_vec = l[1:]
            chr, start, end = self.GW_meta_data[int(node_num)]
            end = int(int(end)/self.resolution)
            oF2.write("%s\t%d\t" % (chr, end))
            for emb in emb_vec:
                oF2.write(str(emb) + "\t")
            oF2.write("\n")
        oF2.close()
