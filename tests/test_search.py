import unittest

from context import ContextSdk, ContextSdkConfig


class TestYourClassName(unittest.TestCase):
    def setUp(self):
        self.sdk = ContextSdk(
            ContextSdkConfig(
                api_key="",
            )
        )

    def test_search(self):
        bot_id = "k7rB5_3JT"
        query = "How can I get started with Helius?"
        top_k = 1
        result = self.sdk.search(bot_id, query, top_k)

        # check the type of the result
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
