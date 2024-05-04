import unittest
from PIL import Image
from app import import_and_predict


class TestApp(unittest.TestCase):

    def test_import_and_predict(self):
        image_data = Image.new('RGB', (100, 100))  # Mock image data
        caption = import_and_predict(image_data)  # Call the function
        self.assertIsInstance(caption, str)  # Check if caption is a string
        self.assertTrue(len(caption) > 0)  # Check if caption is not empty


if __name__ == '__main__':
    unittest.main()
