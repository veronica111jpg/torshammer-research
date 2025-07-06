import unittest
import torshammer

class TestTorshammer(unittest.TestCase):
    
    def test_useragents_not_empty(self):
        self.assertTrue(len(torshammer.useragents) > 0, "User-Agent list should not be empty")

    def test_httpPost_class_exists(self):
        self.assertTrue(hasattr(torshammer, 'httpPost'), "httpPost class must exist")

if __name__ == '__main__':
    unittest.main()
