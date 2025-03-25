from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class ContentPlanningAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def create_outline(self, topic, research_data):
        key_points_str = "\n".join(research_data["key_points"])  # Join outside f-string
        prompt = (
            f"Create a detailed outline for a 2000-word HR blog post on '{topic}'. "
            "Include an H1 title, 5-7 H2 sections, and 2-3 H3 subheadings per H2. "
            "Base it on these key points:\n" + key_points_str
        )
        try:
            response = self.client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Groq API error: {e}")
            return "Error creating outline."

if __name__ == "__main__":
    agent = ContentPlanningAgent()
    topic = "Artificial Intelligence and Automation in HR"
    research_data = {
        "key_points": [
            "Enhanced Employee Experience: AI will enable hyper-personalized interactions...",
            "Streamlined Tasks: Automation will free up HR professionals...",
            "Data-Driven Decision Making: AI will analyze data...",
            "Human-Centric Workplace: The use of AI and automation...",
            "Increased Productivity: By leveraging AI and automation..."
        ]
    }
    outline = agent.create_outline(topic, research_data)
    print(f"Outline:\n{outline}")