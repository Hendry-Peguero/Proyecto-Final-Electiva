import unittest

class TestWebPage(unittest.TestCase):
    def test_title(self):
        with open("index.html", "r") as file:
            content = file.read()
        self.assertIn("<title>Hola Mundo</title>", content)

    def test_heading(self):
        with open("index.html", "r") as file:
            content = file.read()
        self.assertIn("<h1>¡Hola Mundo!</h1>", content)

if __name__ == "__main__":
    unittest.main()
