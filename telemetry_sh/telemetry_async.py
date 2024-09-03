import aiohttp
from typing import Union, List


class TelemetryAsync:
    def __init__(self):
        self.api_key = None
        self.base_url = "https://api.telemetry.sh"

    def init(self, api_key: str):
        self.api_key = api_key
        
    async def check_and_return(self, response: aiohttp.ClientResponse) -> dict:
        respose_json = await response.json()
        if respose_json.get("status", "error") == "error":
            raise Exception(respose_json.get("message", "Unknown error"))
        return respose_json

    async def log(self, table: str, data: Union[dict, List[dict]]) -> dict:
        if not self.api_key:
            raise ValueError(
                "API key is not initialized. Please call init() with your API key."
            )

        headers = {"Content-Type": "application/json", "Authorization": self.api_key}

        body = {"data": data, "table": table}

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/log", headers=headers, json=body
            ) as response:
                return await self.check_and_return(response)

    async def query(self, query: str) -> dict:
        if not self.api_key:
            raise ValueError(
                "API key is not initialized. Please call init() with your API key."
            )

        headers = {"Content-Type": "application/json", "Authorization": self.api_key}

        body = {"query": query, "realtime": True, "json": True}

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/query", headers=headers, json=body
            ) as response:
                return await self.check_and_return(response)
