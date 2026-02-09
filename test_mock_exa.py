import unittest
from mock_exa import MockExaClient

class TestMockExaClient(unittest.TestCase):
    def setUp(self):
        self.client = MockExaClient()

    def test_search_generic(self):
        # Test generic search
        res = self.client.search_and_contents("mRNA")
        self.assertGreater(len(res["results"]), 0)
        self.assertIn("autopromptString", res)

    def test_search_specific_vendor_type(self):
        # Test searching for CDMO specifically
        res = self.client.search_and_contents("manufacturing", type="CDMO")
        self.assertGreater(len(res["results"]), 0)
        # Check if results are relevant (simple check)
        # Note: Mock logic might return mixed results based on text match, but score should be high
        first_result = res["results"][0]
        self.assertIn("score", first_result)

    def test_search_no_results(self):
        # Test a query that likely has no results in our small mock DB
        res = self.client.search_and_contents("Xylophone Repair Shop")
        # Depending on logic, it might return 0 or low score results.
        # My logic returns all if query doesn't match? No, "if score > 0 or query == '*'".
        # So "Xylophone" should return empty if no match.
        self.assertEqual(len(res["results"]), 0)

    def test_structure(self):
        res = self.client.search_and_contents("BioVector")
        if res["results"]:
            item = res["results"][0]
            self.assertIn("custom_metadata", item)
            self.assertIn("vendor_name", item["custom_metadata"])
            self.assertIn("url", item)
            self.assertIn("highlights", item)

if __name__ == '__main__':
    unittest.main()
