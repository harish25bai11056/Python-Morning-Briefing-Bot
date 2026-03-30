import requests
import datetime
import random

def get_weather():
    """Fetches live weather for VIT Bhopal (Kothri Kalan)"""
    lat = 23.08
    lon = 76.85
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        
        temp = data['current_weather']['temperature']
        wind = data['current_weather']['windspeed']
        return f"🌡️ Temperature: {temp}°C | 💨 Wind: {wind} km/h"
    except Exception as e:
        return f"  Could not fetch weather: {e}"

def get_bhopal_news(api_key):
    """Fetches a random selection of 5 recent articles about Bhopal"""
    # Grabs a larger pool of articles sorted by relevance or recency
    url = f"https://newsapi.org/v2/everything?q=Bhopal&language=en&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        articles = response.json().get('articles', [])
        
        if not articles:
            return "  No recent news articles found for Bhopal right now."
            
        # If there are more than 5 articles, pick 5 at random!
        if len(articles) >= 5:
            selected_articles = random.sample(articles, 5)
        else:
            selected_articles = articles # Just use however many exist if less than 5
            
        news_str = ""
        for i, article in enumerate(selected_articles, 1):
            title = article.get('title', 'No Title')
            news_str += f"  {i}. {title}\n"
        return news_str
    except Exception as e:
         return f"  Could not fetch news: {e}"

def get_quote():
    """Fetches a random inspirational quote from ZenQuotes API"""
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return f"🌟 \"{quote}\" - {author}"
    except Exception as e:
        return f"  Could not fetch quote: {e}"

def get_traffic_route():
    """
    Simulates fetching live traffic data for two routes to campus.
    Compares the times and recommends the best route.
    """
    routes = {
        "Route A (Indore-Bhopal Highway)": random.randint(35, 65),
        "Route B (Local Village Road)": random.randint(45, 55)
    }
    
    best_route = min(routes, key=routes.get)
    
    traffic_report = ""
    for route, time in routes.items():
        if time > 50:
            condition = "🔴 Heavy Traffic"
        elif time > 40:
            condition = "🟡 Moderate Traffic"
        else:
            condition = "🟢 Light Traffic"
            
        traffic_report += f"  🚗 {route}: {time} mins ({condition})\n"
        
    traffic_report += f"\n  ✅ Recommendation: Take {best_route} today!"
    return traffic_report

def main():
    # Fetch exact current date and time
    now = datetime.datetime.now()
    exact_time = now.strftime("%A, %B %d, %Y at %I:%M:%S %p")

    print("========================================")
    print(" Good Morning! Here is your VIT Bhopal briefing.")
    print(f" Generated on: {exact_time}")
    print("========================================\n")
    
    print(get_quote())
    
    
    print("🌤️  VIT BHOPAL WEATHER:")
    print("  " + get_weather()) 
    
    print("\n🗺️  COMMUTE & ROUTE SELECTION:")
    print(get_traffic_route())
    
    print("\n📰 LATEST BHOPAL NEWS:")
    news_key = "25ae3d8ca7ce4af88bd5f3f2ee764a93" 
    print(get_bhopal_news(news_key))
        
    print("\n========================================")

if __name__ == "__main__":
    main()
