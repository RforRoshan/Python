import unittest
import Naive_algo

class test_Naive_Algo(unittest.TestCase):
    def test_1(self):
        txt="AEIOUANDIONANDU"
        pat="AND"
        self.assertEqual(Naive_algo.Naive_Algorithm(txt,pat),[5,11],"Should be [5,11]")

    def test_2(self):
        txt="FFDFKAJKLJFSFSDFFDFFFSDOIRKFFDSLKDDFFFJAABAACAADAABAAABAAGFFDKFFFD"
        pat="FFD"
        self.assertEqual(Naive_algo.Naive_Algorithm(txt,pat),[0, 15, 27, 58, 63],"Should be [0, 15, 27, 58, 63]")

    def test_3(self):
        txt="FFDFKAJKLJFSFSDFFDFFFSDOIRKFFDSLKDDFFFJAABAACAADAABAAABAAGFFDKFFFD"
        pat="AABA"
        self.assertEqual(Naive_algo.Naive_Algorithm(txt,pat),[39, 48, 52],"Should be [39, 48, 52]")

    def test_4(self):
        txt="AAAABADGJJGFNNNNNSDMHGFDSDDSFDSDFDSDGJHGSDFSDFG"
        pat="SDF"
        self.assertEqual(Naive_algo.Naive_Algorithm(txt,pat),[30,40,43],"Should be 0, [30,40,43]")

    def test_5(self):
        txt="FIRST SECONDFIRST FIRST FIVEFIRST"
        pat="FIRST"
        self.assertEqual(Naive_algo.Naive_Algorithm(txt,pat),[0,12,18,28],"Should be [0,12,18,28]")

    def test_6(self):
        txt="1235451321321ARDG65FHGF55HFHF15H1F5HF5H45454F54HF545FH4FHFHNFGGFGFHG1GFNG5GFH15HFBFGJGFFGFGJGHFDNGFGFBXFFCGNGNGFVCBVCCVGGGFH454456789"
        pat="15H"
        self.assertEqual(Naive_algo.Naive_Algorithm(txt,pat),[29,77],"Should be [29,77]")

    def test_7(self):
        txt="ZZZZZZAAZZZZZZZZZZZZZAAZZZZZZZZAAZZZZZZZZAZAZZZZZZAZZZZZZAAZZZAZZZZZZAZZZZZAAZZAAAAZZZZZZAZZZZZAAAZZZZZZZZZZAZAZ"
        pat="ZZZZAAZ"
        self.assertEqual(Naive_algo.Naive_Algorithm(txt,pat),[2,17,27,53,71],"Should be [2,17,27,53,71]")


if __name__=="__main__":
    unittest.main()