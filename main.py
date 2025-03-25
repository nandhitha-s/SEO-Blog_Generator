from agents.research_agent import ResearchAgent
from agents.planning_agent import ContentPlanningAgent
from agents.content_generation_agent import ContentGenerationAgent
from agents.optimizer_agent import OptimizerAgent
from agents.review_agent import ReviewAgent
from dotenv import load_dotenv
import os
import markdown
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

load_dotenv()

def save_as_pdf(content, file_path):
    """Save Markdown content as a PDF with basic formatting."""
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    for line in content.split("\n"):
        if line.startswith("# "):
            story.append(Paragraph(line[2:], styles["Heading1"]))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:], styles["Heading2"]))
        elif line.startswith("### "):
            story.append(Paragraph(line[4:], styles["Heading3"]))
        elif line.strip():
            story.append(Paragraph(line, styles["BodyText"]))
        story.append(Spacer(1, 12))
    
    doc.build(story)

def generate_blog():
    research_agent = ResearchAgent()
    planning_agent = ContentPlanningAgent()
    content_agent = ContentGenerationAgent()
    optimizer_agent = OptimizerAgent()
    review_agent = ReviewAgent()

    # Create folders
    intermediate_dir = "intermediate"
    output_dir = "output"
    os.makedirs(intermediate_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # Research phase
    topic, research_data = research_agent.research_topic()
    research_file = os.path.join(intermediate_dir, "research_output.txt")
    with open(research_file, "w", encoding="utf-8") as f:
        f.write(f"Topic: {topic}\n\nKey Points:\n")
        for point in research_data["key_points"]:
            f.write(f"- {point}\n")
    print(f"Research output saved to {research_file}")

    # Planning phase
    outline = planning_agent.create_outline(topic, research_data)
    outline_file = os.path.join(intermediate_dir, "outline.txt")
    with open(outline_file, "w", encoding="utf-8") as f:
        f.write(outline)
    print(f"Outline saved to {outline_file}")

    # Content generation phase
    blog_post = content_agent.generate_blog_post(topic, research_data, outline_file)
    blog_file = os.path.join(intermediate_dir, "blog_post.txt")
    with open(blog_file, "w", encoding="utf-8") as f:
        f.write(blog_post)
    print(f"Blog post saved to {blog_file}")

    # Optimization phase
    optimized_blog, _, _, _, _ = optimizer_agent.optimize_blog(blog_file)
    optimized_file = os.path.join(intermediate_dir, "optimized_blog_post.txt")
    with open(optimized_file, "w", encoding="utf-8") as f:
        f.write(optimized_blog)
    print(f"Optimized blog post saved to {optimized_file}")

    # Review phase
    final_blog, word_count, keyword_counts, density, heading_count = review_agent.review_blog(optimized_file)
    
    # Save final outputs in multiple formats
    # Markdown
    md_file = os.path.join(output_dir, "final_blog_post.md")
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(final_blog)
    # TXT
    txt_file = os.path.join(output_dir, "final_blog_post.txt")
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(final_blog)
    # HTML
    html_content = markdown.markdown(final_blog)
    html_file = os.path.join(output_dir, "final_blog_post.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(f"<!DOCTYPE html><html><head><title>{topic}</title></head><body>{html_content}</body></html>")
    # PDF
    pdf_file = os.path.join(output_dir, "final_blog_post.pdf")
    save_as_pdf(final_blog, pdf_file)

    print(f"Final blog post saved to {md_file}, {txt_file}, {html_file}, and {pdf_file}")
    print(f"Word Count: {word_count}")
    print(f"Keyword Counts: {keyword_counts}")
    print(f"Keyword Density: {density}")
    print(f"Headings: {heading_count}")

if __name__ == "__main__":
    generate_blog()