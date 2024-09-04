import requests
import json
from typing import Union, List

class Telemetry:
    def __init__(self):
        self.api_key = None
        self.base_url = "https://api.telemetry.sh"

    def init(self, api_key: str):
        self.api_key = api_key
        
    def check_and_return(self, response: requests.Response) -> dict:
        response_json = response.json()
        if response_json.get("status", "error") == "error":
            raise Exception(response_json.get("message", "Unknown error"))
        return response_json

    def log(self, table: str, data: Union[dict, List[dict]]) -> dict:
        if not self.api_key:
            raise ValueError("API key is not initialized. Please call init() with your API key.")
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_key
        }
        
        body = {
            "data": data,
            "table": table
        }
        
        response = requests.post(f"{self.base_url}/log", headers=headers, data=json.dumps(body))
        return self.check_and_return(response)

    def query(self, query: str) -> dict:
        if not self.api_key:
            raise ValueError("API key is not initialized. Please call init() with your API key.")
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_key
        }
        
        body = {
            "query": query,
            "realtime": True,
            "json": True
        }
        
        response = requests.post(f"{self.base_url}/query", headers=headers, data=json.dumps(body))
        return self.check_and_return(response)

telemetry = Telemetry()
