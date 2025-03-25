from groq import Groq
from dotenv import load_dotenv
import os
import re

load_dotenv()

class OptimizerAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.keywords = ["HR trends 2025", "Artificial Intelligence in HR", "automation in HR"]

    def count_keywords(self, text):
        word_count = len(re.findall(r'\w+', text))
        keyword_counts = {kw: len(re.findall(r'\b' + re.escape(kw) + r'\b', text, re.IGNORECASE)) for kw in self.keywords}
        density = {kw: (count / word_count * 100) if word_count > 0 else 0 for kw, count in keyword_counts.items()}
        return word_count, keyword_counts, density

    def count_headings(self, text):
        heading_count = {
            "H1": len(re.findall(r'^\*\*[^ *\n]+\*\*$|^# .+', text, re.MULTILINE)),
            "H2": len(re.findall(r'^\*\*[^ *\n]+\*\*(?!\*)|^## .+', text, re.MULTILINE)) - 1,
            "H3": len(re.findall(r'^### .+', text, re.MULTILINE))
        }
        return heading_count

    def optimize_blog(self, blog_file="blog_post.txt"):
        try:
            with open(blog_file, "r", encoding="utf-8") as f:
                blog_text = f.read().strip()
        except FileNotFoundError:
            print(f"Error: {blog_file} not found. Using placeholder text.")
            blog_text = "# Sample HR Blog\n## Intro\nText here."

        word_count, keyword_counts, density = self.count_keywords(blog_text)
        heading_count = self.count_headings(blog_text)

        prompt = (
            f"Optimize and expand this {word_count}-word blog post to exactly 2000 words for SEO in Markdown format:\n\n{blog_text}\n\n"
            "Follow these steps:\n"
            "1. Convert bold headings (**Title**) to Markdown (# Title, ## Title, ### Title).\n"
            "2. Ensure keyword density of 1-2% for: {', '.join(self.keywords)} (current: {', '.join([f'{kw}: {d:.2f}%' for kw, d in density.items()])})—insert keywords naturally every 50-100 words.\n"
            "3. Structure with one # H1, 5-7 ## H2s, 2-3 ### H3s per H2 (current: H1={heading_count['H1']}, H2={heading_count['H2']}, H3={heading_count['H3']}).\n"
            "4. Add a 150-160 char meta description at the top (e.g., '<!-- Meta: ... -->') if missing.\n"
            "5. Expand each section (Introduction, Elevating Employee Experience, etc.) to at least 300-400 words with detailed examples, case studies, and insights based on the outline and key points.\n"
            "6. Improve readability: use short sentences (15-20 words), clear language, and engaging transitions.\n"
            "7. Maintain a professional tone, optimized for SEO, and ensure the total word count reaches exactly 2000 words.dtrictly 2000 words\n"
            "Return the optimized blog post."
        )
        
        try:
            response = self.client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=7000  # Increased to ensure 2000 words
            )
            optimized_blog = response.choices[0].message.content.strip()
            return optimized_blog, word_count, keyword_counts, density, heading_count
        except Exception as e:
            print(f"Groq API error: {e}")
            return blog_text, word_count, keyword_counts, density, heading_count

if __name__ == "__main__":
    agent = OptimizerAgent()
    optimized_blog, word_count, keyword_counts, density, heading_count = agent.optimize_blog()
    print(f"Original Word Count: {word_count}")
    print(f"Keyword Counts: {keyword_counts}")
    print(f"Keyword Density: {density}")
    print(f"Headings: {heading_count}")
    print(f"Optimized Blog Post:\n{optimized_blog}")