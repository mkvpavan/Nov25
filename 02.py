"""
Determine the row index with minimum number of ones.
The given 2D matrix has only zeroes and ones and also the matrix is sorted row wise. 
If two or more rows have same number of 1's than print the row with smallest index.

input:
size of matrix: 3 3
0 0 0 0 0 0 0 0 0
output:  -1

size of matrix: 4 4
0 0 0 1 0 1 1 1 0 0 1 1 0 0 1 1
output: 0
"""

import unittest

def min_row(m,n,l):
    r=[]
    for i in range(0,m*n,m):
        r.append(l[i:i+m])
    
    if(len(l)!=m*n):
        n=len(r)-1   
    re=[]
    for i in range(n):
        s=0
        for j in range(m):
            s=s+r[i][j]
        re.append(s)
        
    
    min=re[0]
    for i in range(len(re)):
        if(re[i]<min):
            min=re[i]


    c=1
    if (c not in l):
        return -1
    else:
        return re.index(min)

# DO NOT TOUCH THE BELOW CODE
class TestCommonWords(unittest.TestCase):

    def test_01(self):
        l=[0,0,0,0,0,0,0,0,0]
        output = -1
        self.assertEqual(min_row(3,3,l), output)

    def test_02(self):
        l=[0,0,0,1,0,1,1,1,0,0,1,1,0,0,1,1]
        output = 0
        self.assertEqual(min_row(4,4,l), output)

    def test_03(self):
        l=[0,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0]
        output = 3
        self.assertEqual(min_row(4,4,l), output)

    def test_04(self):
        l=[0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,0]
        output = 0
        self.assertEqual(min_row(5,5,l), output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
