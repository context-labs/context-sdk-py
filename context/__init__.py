from dataclasses import dataclass
from urllib import request

import json


CONTEXT_BASE_URL = "https://portal.usecontext.io"


@dataclass
class ContextSdkConfig:
    """
    Context SDK configuration
    """

    api_key: str
    origin: str = ""
    api_host: str = CONTEXT_BASE_URL


class ContextSdk:
    """
    Context SDK
    """

    config: ContextSdkConfig

    def __init__(self, config):
        """
        Constructor
        """
        self.config = config

    def search(self, bot_id: str, query: str, top_k: int = 20):
        """
        Search documents

        :param bot_id: Bot ID
        :param query: The query string to search for
        :param top_k: The number of documents to return

        """
        fetch_bot_response = self.post_request("/api/bot", {"botId": bot_id})

        if fetch_bot_response.status != 200:
            raise Exception("Error fetching bot.")

        bot = json.loads(fetch_bot_response.read())

        params = {
            "botId": bot_id,
            "sourceIds": bot["sourceIds"],
            "query": query,
            "distinctId": "",
            "topK": top_k,
            "origin": self.config.origin,
        }

        response = self.post_request("/api/search-snippets", params)

        if response.status != 200:
            raise Exception(response.reason)

        result = json.loads(response.read().decode("utf-8"))
        snippets = result["snippets"]

        return snippets

    def post_request(self, path: str, data: dict):
        path = f"{self.config.api_host}{path}"
        data_str = json.dumps(data)
        conn = request.Request(
            path,
            data=data_str.encode(),
            headers={
                "Content-Type": "application/json",
                "X-API-Key": self.config.api_key,
            },
            method="POST",
        )
        return request.urlopen(conn)
