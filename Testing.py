import unittest
import random


def generate_nums():
    mylist = []
    while len(mylist) < 6:
        mynumber = random.randint(1, 49)
        if mynumber not in mylist:
            mylist.append(mynumber)
            print(mylist)


class RandomNums(unittest.TestCase):
    def test(self):
        self.a = 1
        self.b = 49


def test_nums(self):
    generate_nums()
    self.assertTrue(self.a >= 1 and self.b <= 20)


if __name__ == '__main__':
    unittest.main()
