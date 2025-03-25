from groq import Groq
from dotenv import load_dotenv
import os
import re

load_dotenv()

class ReviewAgent:
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
            "H1": len(re.findall(r'^# .+', text, re.MULTILINE)),
            "H2": len(re.findall(r'^## .+', text, re.MULTILINE)),
            "H3": len(re.findall(r'^### .+', text, re.MULTILINE))
        }
        return heading_count

    def review_blog(self, blog_file="intermediate/optimized_blog_post.txt"):
        try:
            with open(blog_file, "r", encoding="utf-8") as f:
                blog_text = f.read().strip()
        except FileNotFoundError:
            print(f"Error: {blog_file} not found. Using placeholder text.")
            blog_text = "# Sample Blog\n## Intro\nText here."

        word_count, keyword_counts, density = self.count_keywords(blog_text)
        heading_count = self.count_headings(blog_text)

        prompt = (
            f"Review and polish this {word_count}-word blog post in Markdown format:\n\n{blog_text}\n\n"
            "Ensure:\n"
            "- Exactly 2000 words—add or trim content naturally if needed (current: {word_count}).\n"
            "- Keyword density of 1-2% for: {', '.join(self.keywords)} (current: {', '.join([f'{kw}: {d:.2f}%' for kw, d in density.items()])})—adjust usage for natural flow.\n"
            "- One # H1, 5-7 ## H2s, 2-3 ### H3s per H2 (current: H1={heading_count['H1']}, H2={heading_count['H2']}, H3={heading_count['H3']}).\n"
            "- Retain the meta description (e.g., '<!-- Meta: ... -->') and ensure it’s 150-160 chars.\n"
            "- Enhance readability: sentences 15-20 words, clear transitions, no repetition.\n"
            "- Fix grammar, spelling, and coherence issues.\n"
            "- Maintain a professional, engaging, SEO-optimized tone.\n"
            "Return the final polished blog post."
        )
        
        try:
            response = self.client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=7000
            )
            final_blog = response.choices[0].message.content.strip()
            return final_blog, word_count, keyword_counts, density, heading_count
        except Exception as e:
            print(f"Groq API error: {e}")
            return blog_text, word_count, keyword_counts, density, heading_count

if __name__ == "__main__":
    agent = ReviewAgent()
    final_blog, word_count, keyword_counts, density, heading_count = agent.review_blog()
    print(f"Original Word Count: {word_count}")
    print(f"Keyword Counts: {keyword_counts}")
    print(f"Keyword Density: {density}")
    print(f"Headings: {heading_count}")
    print(f"Final Blog Post:\n{final_blog}")