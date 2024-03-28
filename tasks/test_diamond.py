import unittest
import diamond

class TestDiamond(unittest.TestCase):

    '''
 A
    '''

    def test_A(self):
        assert diamond.makeDiamond("A") == "A"

    '''
 A
B B
 A
    '''

    def test_B(self):
        b = diamond.makeDiamond("B")
        bs = b.split('\n')
        assert b[1] == "A"
        assert len(bs) == 3
        assert bs[1][0] == "B"
        assert bs[1][2] == "B"
        assert bs[2][1] == "A" 
 
    '''
  A
 B B
C   C
 B B
  A
    '''    

    def test_C(self):
        c = diamond.makeDiamond("C")
        cs = c.split('\n')
        assert len(c.split('\n')) == 5
        assert c[2] == "A"
        assert cs[1][1] == "B"
        assert cs[2][0] == "C"