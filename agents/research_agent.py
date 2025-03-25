import requests
from groq import Groq
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os

load_dotenv()

class ResearchAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.serper_api_key = os.getenv("SERPER_API_KEY")

    def scrape_article(self, url):
        """Scrape main content from a given URL."""
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.select("p")
            content = " ".join([p.get_text(strip=True) for p in paragraphs[:10]])
            return content[:2000] if content else "No content extracted."
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None

    def research_topic(self):
        url = "https://google.serper.dev/search"
        headers = {"X-API-KEY": self.serper_api_key, "Content-Type": "application/json"}
        payload = {"q": "HR trends 2025", "gl": "us", "num": 10}

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            news_results = response.json().get("organic", [])
            articles = [{"title": item["title"], "url": item["link"]} for item in news_results[:10]]
            print(f"Serper Articles: {[a['title'] for a in articles]}")
        except requests.RequestException as e:
            print(f"Serper API error: {e}. Using fallback data.")
            articles = [{"title": "AI in HR grows", "url": "https://example.com/ai-hr"}]

        for article in articles:
            article["content"] = self.scrape_article(article["url"])

        valid_articles = [a for a in articles if a["content"] is not None]
        if not valid_articles:
            print("No valid article content scraped. Using fallback.")
            valid_articles = [{"title": "AI in HR grows", "content": "AI is growing in HR."}]

        prompt = "From these Google News articles on HR trends 2025, pick a trending topic:\n"
        for article in valid_articles:
            prompt += f"Title: {article['title']}\nContent (excerpt): {article['content'][:2000]}...\n\n"
        try:
            response = self.client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000
            )
            topic = response.choices[0].message.content.strip()
            topic = topic.split("**")[-1].strip() if "**" in topic else topic
            print(f"Selected Topic from Groq: {topic}")
            research_data = self.scrape_details(topic, valid_articles)
            return topic, research_data
        except Exception as e:
            print(f"Groq API error: {e}")
            return "AI in HR", {"key_points": ["Fallback point 1", "Fallback point 2"]}

    def scrape_details(self, topic, articles):
        prompt = f"Provide 3-5 concise key points about '{topic}' for an HR blog post based on these excerpts:\n"
        for article in articles:
            prompt += f"Title: {article['title']}\nContent (excerpt): {article['content'][:2000]}...\n\n"
        try:
            response = self.client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=2000
            )
            details = response.choices[0].message.content.strip()
            key_points = [line.strip() for line in details.split("\n") if line.strip() and not line.startswith("**") and not line.startswith("Here are")]
            return {"key_points": key_points[:10]}
        except Exception as e:
            print(f"Groq API error in scrape_details: {e}")
            return {"key_points": ["Error fetching details"]}

if __name__ == "__main__":
    agent = ResearchAgent()
    topic, data = agent.research_topic()
    print(f"Topic: {topic}")
    print(f"Key Points: {data['key_points']}")

    # Save to a text file
    output_file = "research_output.txt"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"Topic: {topic}\n\n")
            f.write("Key Points:\n")
            for point in data["key_points"]:
                f.write(f"- {point}\n")
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error saving to file: {e}")