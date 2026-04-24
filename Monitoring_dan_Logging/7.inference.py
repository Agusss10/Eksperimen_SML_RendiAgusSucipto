import requests
import json

# URL endpoint MLflow
url = "http://127.0.0.1:5001/invocations"

data = {
    "inputs": [
        [22, 59000, 123.0, 35000, 16.02, 0.59, 3, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True]
    ]
}

# request ke model
response = requests.post(
    url,
    headers={"Content-Type": "application/json"},
    data=json.dumps(data)
)

# tampilkan hasil
print("Status:", response.status_code)
print("Response:", response.json())