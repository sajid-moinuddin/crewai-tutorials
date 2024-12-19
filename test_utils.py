import unittest
from utils import get_openai_api_key

class TestIntegrationUtils(unittest.TestCase):

    def test_get_openai_api_key(self):
        # Arrange
        expected_api_key = "test_openai_api_key"

        # Act
        api_key = get_openai_api_key()

        # Assert
        self.assertEqual(api_key, expected_api_key)

if __name__ == '__main__':
    unittest.main()