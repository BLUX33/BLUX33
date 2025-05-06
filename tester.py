import requests

def test_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Success: {url} is reachable.")
            return 0
        else:
            print(f"Warning: {url} returned status code {response.status_code}.")
            return 1
    except Exception as e:
        print(f"Error: Could not reach {url}. Exception: {e}")
        return 1

if __name__ == "__main__":
    exit(test_website("https://storeino.com/"))
