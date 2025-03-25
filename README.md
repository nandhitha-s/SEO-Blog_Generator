# Multi-Agent SEO Blog Generator (Backend)

## Overview
This project is a backend system for generating a 2000-word SEO-optimized blog post on HR trends for 2025. It uses a multi-agent architecture to research, plan, generate, optimize, and review the blog content, saving the final output in TXT, HTML, and PDF formats. The system leverages free APIs (Groq and Serper) to ensure cost-effectiveness while delivering high-quality results.

## Approach Evolution
Initially, I explored using AWS services (e.g., AWS Lambda, Amazon Comprehend) for content generation and optimization. AWS offered robust tools for natural language processing and scalability, but after a few runs, I encountered high billing costs due to API usage and compute time. To address this, I switched to Groq and Serper APIs, which are free and well-suited for this task. Groq provides efficient language model capabilities for content generation and optimization, while Serper handles web scraping for research. This pivot reduced costs to zero while maintaining quality, making the project sustainable for submission.

## Features
- Multi-Agent Pipeline:
  - Research Agent: Scrapes Google News for "HR trends 2025" using Serper API, selects a topic with Groq.
  - Planning Agent: Creates a blog outline with H1, H2, and H3 headings.
  - Content Generation Agent: Writes an initial blog draft based on the outline.
  - Optimizer Agent: Enhances SEO (keyword density 1-2%, proper headings, meta description) and expands content.
  - Review Agent: Polishes the blog to exactly 2000 words, ensuring readability and coherence.
- Output Formats: Final blog saved as TXT, HTML, and PDF in output/ folder.
- Intermediate Outputs: Research, outline, initial, and optimized drafts saved in intermediate/ folder.
- SEO Optimization: Targets keywords like "HR trends 2025", "Artificial Intelligence in HR", "automation in HR".

## Project Structure

The project is organized into directories for agents, intermediate outputs, final outputs, and root-level files. Below is a clear breakdown:

| Directory/File         | Description                                      |
|------------------------|--------------------------------------------------|
| **agents/**            | Contains all agent scripts for the pipeline      |
| agents/content_generation_agent.py | Generates the initial blog draft     |
| agents/optimizer_agent.py | Optimizes the blog for SEO and expands content |
| agents/planning_agent.py | Creates the blog outline                |
| agents/research_agent.py | Researches HR trends using Serper API   |
| agents/review_agent.py | Polishes the final blog to 2000 words     |
| **intermediate/**      | Stores intermediate outputs (ignored by Git)     |
| intermediate/blog_post.txt | Initial blog draft                     |
| intermediate/optimized_blog_post.txt | SEO-optimized draft          |
| intermediate/outline.txt | Blog structure with headings             |
| intermediate/research_output.txt | Research topic and key points    |
| **output/**            | Stores final blog outputs (ignored by Git)       |
| output/final_blog_post.html | Final blog in HTML format             |
| output/final_blog_post.pdf | Final blog in PDF format               |
| output/final_blog_post.txt | Final 2000-word blog in Markdown       |
| **venv/**              | Virtual environment (ignored by Git)             |
| **.env**               | API keys (ignored by Git)                        |
| **.gitignore**         | Excludes venv/, outputs, etc. from Git           |
| **main.py**            | Orchestrates the entire pipeline                 |
| **requirements.txt**   | Lists project dependencies                       |
| **README.md**          | Project documentation                            |

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