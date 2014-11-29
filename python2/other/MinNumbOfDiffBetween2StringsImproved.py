# author Mauro Baresic
# email: mauro.baresic@outlook.com

import sys

class MinDifferenceImproved():
    R = ''
    B = ''
    m = 0
    n = 0
    k = 0
    L = None
    
    def __init__(self,R,B,k):
        self.R = R
        self.B = B
        self.k = k
        self.m = len(R)
        self.n = len(B)
        self.L = dict()

    def calculate(self):
        #1
        for d in xrange(-(self.k + 1), (self.k + 1) + 1):
            self.L[(d,abs(d)-2)] = - float("inf")
            if (d < 0):
                self.L[(d,abs(d)-1)] = abs(d) - 1
            else:
                self.L[(d,abs(d)-1)] = -1
        #2
        for e in xrange(self.k + 1):
            for d in xrange(- e, e +1):
                #3
                row = max((self.L[(d,e-1)] +1,self.L[(d-1,e-1)],self.L[(d+1,e-1)] +1))
                #4
                while (row < self.m and self.R[row] == self.B[row + d]):
                    row += 1
                #5
                self.L[(d,e)] = row
                #6
                if (row == self.m):
                    print "YES"
                    return 0
                
    def outputScreen(self):
        for i in xrange(- self.k, self.k +1):
            row = ''
            for j in xrange(- self.k, self.k +1):
                if self.L.has_key((i,j)):
                    row += "L(" + str(i) + ', '+ str(j) + ')=' + str(self.L[(i,j)]) + '\t'
            sys.stdout.write(row + '\n')

    def outputFile(self, path):
        f = open(path,'w')
        for i in xrange(- self.k, self.k +1):
            row = ''
            for j in xrange(- self.k, self.k +1):
                if self.L.has_key((i,j)):
                    row += "L(" + str(i) + ', '+ str(j) + ')=' + str(self.L[(i,j)]) + '\t'
            f.write(row + '\n')
        f.close()

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

    mdi = MinDifferenceImproved(R,B,3)
    mdi.calculate()



