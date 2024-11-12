import requests

def fetch_log():
    try:
        response = requests.get("http://spotbugs:5000/log")
        

        # /app/data 저장
        if response.status_code == 200:
            data = response.json()
            print("[ Received log ]: \n", data["log"])
        else:
            print(f"Failed to fetch log. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_log()