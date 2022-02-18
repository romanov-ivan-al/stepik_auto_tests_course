import unittest
import registration_page

class TestPages(unittest.TestCase):
    def test_page1(self):
        self.assertEqual( registration_page.chek_page("http://suninjuly.github.io/registration1.html") , "Congratulations! You have successfully registered!")
    def test_page2(self):
        self.assertEqual( registration_page.chek_page("http://suninjuly.github.io/registration2.html") , "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()