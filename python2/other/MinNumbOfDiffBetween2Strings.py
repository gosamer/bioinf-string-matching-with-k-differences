# author Mauro Baresic
# email: mauro.baresic@outlook.com

import sys
import numpy as np

class MinDifference():
    Cch = 1
    Cde = 1
    Cin = 1
    m = 0
    n = 0
    R = ''
    B = ''
    D = None
    
    def __init__(self,R,B):
        self.R = R
        self.B = B
        self.m = len(R)
        self.n = len(B)
        self.D = np.zeros((self.m+1,self.n+1),dtype = np.int)

    def calculate(self):
        #self.D[(0,0)] = 0
        for j in xrange(1,self.n+1):
            self.D[(0,j)] = j
        for i in xrange(1,self.m+1):
            self.D[(i,0)] = i
        for i in xrange(1,self.m+1):
            for j in xrange(1,self.n+1):
                self.D[(i,j)] = min((self.D[i-1,j] + self.Cde, self.D[(i,j-1)] + self.Cin, self.D[(i-1,j-1)] + self.compare(i-1,j-1)))

    def compare(self, i, j):
        if (i<0 or i> self.m or j<0 or j> self.n):
            return
        if (i>len(self.R)-1 or j>len(self.B)-1):
            return
        if (self.R[i] == self.B[j]):
            return 0
        else:
            return self.Cch
        
    def outputScreen(self):
        if (self.D is None):
            return
        for i in xrange(self.m+1):
            row = ''
            for j in xrange(self.n+1):
                row += str(self.D[i,j]) + '\t'
            sys.stdout.write(row + '\n')

    def outputFile(self, path):
        if (self.D is None):
            return
        f = open(path,'w')
        for i in xrange(self.m+1):
            row = ''
            for j in xrange(self.n+1):
                row += str(self.D[i,j]) + '\t'
            f.write(row + '\n')
        f.close()

    def reconstructMinPath(self):
        pass

if __name__ == "__main__":
    #path = sys.argv[1]
    path = "podaci.txt"
    f = open(path,'r')
    rows = [row.strip() for row in f.readlines()]
    f.close()

    if (len(rows) != 2):
        print "Use!"
        sys.exit()

    R = rows[0]
    B = rows[1]

    md = MinDifference(R,B)
    md.calculate()
    md.outputScreen()



