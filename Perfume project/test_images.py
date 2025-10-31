import requests

urls = [
    "https://source.unsplash.com/220x220/?perfume",
    "https://source.unsplash.com/220x220/?perfume+bottle",
    "https://source.unsplash.com/220x220/?fragrance"
]

for i, url in enumerate(urls, 1):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"Image {i}: Accessible (Status: {response.status_code})")
        else:
            print(f"Image {i}: Not accessible (Status: {response.status_code})")
    except Exception as e:
        print(f"Image {i}: Error - {e}")
