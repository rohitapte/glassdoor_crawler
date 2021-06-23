import requests
import json

url = "http://localhost:9200/amazon/_search"

payload = json.dumps({
  "query": {
    "multi_match": {
      "query": "work"
    }
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
