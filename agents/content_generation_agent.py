from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class ContentGenerationAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_blog_post(self, topic, research_data, outline_file="outline.txt"):
        # Read the outline from file
        try:
            with open(outline_file, "r", encoding="utf-8") as f:
                outline = f.read().strip()
        except FileNotFoundError:
            print(f"Error: {outline_file} not found. Using fallback outline.")
            outline = "H1: {topic}\nH2: Introduction\nH2: Key Point 1\nH2: Key Point 2\nH2: Conclusion"

        # Construct prompt
        key_points_str = "\n".join(research_data["key_points"])
        prompt = (
            f"Write a 2000-word HR blog post on '{topic}'. "
            "Follow this outline:\n{outline}\n\n"
            "Incorporate these key points:\n{key_points_str}\n\n"
            "Ensure the tone is professional, engaging, and SEO-optimized with keywords like "
            "'HR trends 2025', 'Artificial Intelligence in HR', and 'automation in HR'. "
            "Use natural language and avoid repetition."
        )
        
        try:
            response = self.client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=4000  # ~2000 words (assuming ~2 chars/token)
            )
            blog_post = response.choices[0].message.content.strip()
            return blog_post
        except Exception as e:
            print(f"Groq API error: {e}")
            return "Error generating blog post."

if __name__ == "__main__":
    agent = ContentGenerationAgent()
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
    blog_post = agent.generate_blog_post(topic, research_data)
    print(f"Blog Post:\n{blog_post}")