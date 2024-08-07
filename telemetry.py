import requests
import json

class Telemetry:
    def __init__(self):
        self.api_key = None
        self.base_url = "https://api.telemetry.sh"

    def init(self, api_key: str):
        self.api_key = api_key

    def log(self, table: str, data: dict) -> dict:
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
        return response.json()

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
        return response.json()

telemetry = Telemetry()
