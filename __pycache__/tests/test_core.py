# tests/test_core.py

import unittest
from torshammer.core import send_http_get_request

class TestTorshammerCore(unittest.TestCase):

    def test_send_http_get_request_localhost(self):
        """
        This test checks if the function executes without exceptions.
        No actual server is required for this dry test.
        """
        try:
            send_http_get_request("127.0.0.1", 80, "UnitTestAgent/1.0")
        except Exception as e:
            self.fail(f"send_http_get_request raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
