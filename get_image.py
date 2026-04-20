import requests
from datetime import datetime

IMAGE_URL = "ここに画像URL"

now = datetime.now().strftime("%Y%m%d_%H%M")
filename = f"image_{now}.jpg"

response = requests.get(IMAGE_URL)

if response.status_code == 200:
    with open(filename, "wb") as f:
        f.write(response.content)
    print("saved", filename)
else:
    print("failed")
