# Multi-Agent SEO Blog Generator (Backend)

## Overview
This project is a backend system for generating a 2000-word SEO-optimized blog post on HR trends for 2025. It uses a multi-agent architecture to research, plan, generate, optimize, and review the blog content, saving the final output in TXT, HTML, and PDF formats. The system leverages free APIs (Groq and Serper) to ensure cost-effectiveness while delivering high-quality results.

## Approach Evolution
Initially, I used AWS services like Lambda and Comprehend for content generation and optimization, leveraging their scalability and NLP capabilities. However, high costs from API calls and compute time, plus the complexity of managing AWS resources, made this approach unsustainable. I switched to free Groq and Serper APIs, which met the project’s needs—Groq for efficient content generation and optimization, and Serper for web scraping "HR trends 2025" data. This pivot eliminated costs, maintained quality, and simplified development, ensuring the project’s sustainability for submission.

## Features
- **Multi-Agent Pipeline**: A modular system for efficient blog generation.
  - **Research Agent**: Scrapes Google News for "HR trends 2025" using Serper API, selects a topic with Groq (e.g., "AI in HR for 2025").
  - **Planning Agent**: Creates an outline with one H1, 5-7 H2s (e.g., "Introduction", "AI Recruitment"), and 2-3 H3s per H2.
  - **Content Generation Agent**: Writes a 500-1000 word draft using Groq, targeting HR professionals with a professional tone.
  - **Optimizer Agent**: Enhances SEO with 1-2% keyword density ("HR trends 2025", "AI in HR"), adds a 150-160 char meta description, and expands content.
  - **Review Agent**: Polishes the blog to 2000 words, ensuring readability, SEO-friendly headings (one H1, 5-7 H2s, 2-3 H3s per H2), and coherence.
- **Output Formats**:
  - **TXT**: `final_blog_post.txt` (Markdown) for editing.
  - **HTML**: `final_blog_post.html` for web publishing.
  - **PDF**: `final_blog_post.pdf` for sharing/printing.
- **Intermediate Outputs** (in `intermediate/`):
  - `research_output.txt`: Topic and key points.
  - `outline.txt`: Blog structure.
  - `blog_post.txt`: Initial draft.
  - `optimized_blog_post.txt`: SEO-optimized draft.
- **SEO Optimization**:
  - **Keywords**: 1-2% density for "HR trends 2025", "AI in HR", "automation in HR".
  - **Meta Description**: 150-160 chars for search snippets.
  - **Headings**: H1, H2, H3 for structure and SEO.
  - **Engagement**: Adds examples and stats for better dwell time.
  
## Project Structure

The project is organized into directories for agents, intermediate outputs, final outputs, and root-level files. Below is a clear breakdown:
```
## Project Structure
SEO-Blog_Generator/
├── agents/
│   ├── content_generation_agent.py
│   ├── optimizer_agent.py
│   ├── planning_agent.py
│   ├── research_agent.py
│   ├── review_agent.py
├── intermediate/  # Ignored by Git
│   ├── blog_post.txt
│   ├── optimized_blog_post.txt
│   ├── outline.txt
│   ├── research_output.txt
├── output/  # Ignored by Git
│   ├── final_blog_post.html
│   ├── final_blog_post.pdf
│   ├── final_blog_post.txt
├── venv/  # Ignored by Git
├── .env  # Ignored by Git
├── .gitignore
├── main.py
├── requirements.txt
├── README.md
```
**Note**: Directories and files marked as "ignored by Git" (e.g., `venv/`, `intermediate/`, `output/`, `.env`) are excluded via `.gitignore` to keep the repository clean.

## Dependencies
Listed in requirements.txt:
- langchain==0.0.123
- requests==2.31.0
- beautifulsoup4==4.12.2
- markdown==3.5.1
- python-dotenv==1.0.0
- groq==0.4.0
- reportlab==4.2.2

## Setup Instructions
1. Clone the Repository:
   git clone <your-repo-url>
   cd SEO-Blog_Generator
2. Set Up Virtual Environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies:
   pip install -r requirements.txt
4. Configure API Keys:
   - Create a .env file in the root directory.
   - Add your Groq and Serper API keys:
     GROQ_API_KEY=your-groq-key
     SERPER_API_KEY=your-serper-key
   - Obtain keys from Groq (https://groq.com) and Serper (https://serper.dev) (both free tiers used).

## Usage
1. Run the Pipeline:
   python main.py
2. Output:
   - Intermediate files (research_output.txt, outline.txt, etc.) are saved in intermediate/ folder.
   - Final blog post (2000 words) is saved in output/ folder as:
     - final_blog_post.txt (Markdown)
     - final_blog_post.html (HTML)
     - final_blog_post.pdf (PDF)

## Output Details
- Intermediate Outputs (intermediate/ folder):
  - research_output.txt: Topic and key points from research.
  - outline.txt: Blog structure with H1, H2, H3 headings.
  - blog_post.txt: Initial draft.
  - optimized_blog_post.txt: SEO-optimized draft.
- Final Outputs (output/ folder):
  - final_blog_post.txt: Final 2000-word blog in Markdown.
  - final_blog_post.html: HTML version for web display.
  - final_blog_post.pdf: PDF version for printing/sharing.

## APIs Used
- Groq: Free language model API for content generation, optimization, and review.
- Serper: Free API for scraping Google News in the research phase.

## Challenges and Solutions
- AWS Billing: Initially used AWS for content generation, but high costs led to a switch to Groq, which is free and efficient.
- Word Count Issues: Early drafts were ~750 words. Adjusted the Review Agent’s prompt to enforce exactly 2000 words by expanding sections with examples and stats.
- Heading Recognition: Initial blog used bold (** ) headings, causing detection issues. Updated agents to convert to Markdown (# ) format.

## Future Improvements
- Frontend Integration: Add a Flask frontend to trigger generation and display outputs via a web interface.
- Advanced SEO: Incorporate meta tags, alt text for images (if added), and backlink suggestions.
- Content Variety: Support multiple topics beyond HR trends by making the research query configurable.

## Submission Details
- Date: March 25, 2025
- Author: Nandhitha
- Task: ABEX SEO Blog Generator
- Deliverables: 2000-word SEO-optimized blog in TXT, HTML, PDF formats, using free APIs.
