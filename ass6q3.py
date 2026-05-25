import requests

def news_api(name):
    url = f"https://newsapi.org/v2/everything?q={name}&from=2026-05-23&to=2026-05-23&sortBy=popularity&apiKey=f465551f065d4893a3ef58755cc47c10"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print(f"Top news articles about '{name}':")
        for article in data["articles"][:3]:
            print("Title :", article["title"])
            print("Source:", article["source"]["name"])
            print("----------------------------------")
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
        return

name = input("Enter the topic you want to search for: ")
news_api(name)