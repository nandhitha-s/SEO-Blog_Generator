# Multi-Agent SEO Blog Generator (Backend)

## Overview
This project is a backend system for generating a 2000-word SEO-optimized blog post on HR trends for 2025. It uses a multi-agent architecture to research, plan, generate, optimize, and review the blog content, saving the final output in TXT, HTML, and PDF formats. The system leverages free APIs (Groq and Serper) to ensure cost-effectiveness while delivering high-quality results.

## Approach Evolution
In the initial phase of this project, I explored leveraging AWS services to build the content generation and optimization pipeline. Specifically, I used AWS Lambda for serverless execution of the agents and Amazon Comprehend for natural language processing tasks, such as keyword extraction and sentiment analysis. AWS provided a robust infrastructure with powerful tools for scalability, allowing the system to handle large-scale content generation efficiently. Additionally, AWS offered seamless integration with other services like S3 for storing intermediate outputs and DynamoDB for managing metadata.

However, after several test runs, I encountered significant challenges with AWS. The primary issue was the high billing costs incurred due to frequent API calls to Amazon Comprehend and the compute time on AWS Lambda. For example, each content generation task required multiple API requests to process and analyze text, and the cumulative costs quickly became unsustainable for a project of this scope. Furthermore, the complexity of managing AWS resources—such as configuring IAM roles, setting up Lambda triggers, and monitoring usage—added unnecessary overhead to the development process.

To address these challenges, I researched alternative solutions that could deliver similar functionality at a lower cost. This led me to pivot to Groq and Serper APIs, both of which offer free tiers that align perfectly with the project’s requirements. Groq, a high-performance language model API, became the backbone for content generation, optimization, and review tasks. It provided fast and accurate text generation capabilities, rivaling Amazon Comprehend’s NLP features, while being completely free for the usage levels required. Serper, on the other hand, offered a free API for web scraping, enabling the Research Agent to efficiently gather data from Google News for the topic "HR trends 2025" without incurring costs.

This strategic pivot reduced the project’s operational costs to zero while maintaining, and in some cases improving, the quality of the output. Groq’s language model proved to be highly efficient, delivering coherent and contextually relevant content, while Serper’s scraping capabilities ensured the research phase was both comprehensive and cost-effective. The switch also simplified the development process by eliminating the need for complex AWS configurations, allowing me to focus on refining the agent pipeline and ensuring the final blog met the 2000-word requirement. This approach made the project sustainable for submission and demonstrated the value of leveraging free, high-quality APIs for cost-sensitive applications.

## Features
- **Multi-Agent Pipeline**: The system is built on a modular, multi-agent architecture that breaks down the blog generation process into distinct, specialized tasks for efficiency and scalability.
  - **Research Agent**: This agent initiates the pipeline by scraping Google News for articles related to "HR trends 2025" using the Serper API. It processes the scraped data to extract key points, such as emerging trends, statistics, and expert opinions, and then uses Groq to analyze the data and select a focused topic for the blog (e.g., "The Role of AI in HR Transformation for 2025"). This ensures the blog is grounded in current, relevant information.
  - **Planning Agent**: Using the research data, this agent creates a structured blog outline with one H1 heading (the blog title), 5-7 H2 headings for main sections (e.g., "Introduction", "AI-Driven Recruitment", "Conclusion"), and 2-3 H3 subheadings per H2 for detailed points. The outline ensures a logical flow and comprehensive coverage of the topic, setting a strong foundation for content generation.
  - **Content Generation Agent**: This agent writes an initial blog draft based on the outline, leveraging Groq’s language model to produce coherent, engaging content. It incorporates the researched key points and ensures the tone is professional yet accessible, targeting HR professionals and business leaders interested in 2025 trends. The initial draft typically ranges from 500-1000 words, which is later expanded.
  - **Optimizer Agent**: The optimizer enhances the draft for SEO by targeting a keyword density of 1-2% for primary keywords like "HR trends 2025", "Artificial Intelligence in HR", and "automation in HR". It also adds a meta description (150-160 characters) for search engine snippets, ensures proper heading structure (H1, H2, H3), and expands the content with additional examples, case studies, and statistics to improve depth and engagement.
  - **Review Agent**: The final agent polishes the blog to meet the 2000-word requirement, using Groq to refine the text for readability (sentences of 15-20 words, clear transitions) and coherence. It adjusts keyword usage for natural flow, ensures the heading structure aligns with SEO best practices (one H1, 5-7 H2s, 2-3 H3s per H2), and fixes grammar, spelling, and style issues to maintain a professional tone.
- **Output Formats**: The final blog is saved in multiple formats to cater to different use cases:
  - **TXT**: Stored as `final_blog_post.txt` in Markdown format, ideal for further editing or integration into content management systems.
  - **HTML**: Saved as `final_blog_post.html`, ready for direct web publishing with basic formatting preserved.
  - **PDF**: Generated as `final_blog_post.pdf` using ReportLab, suitable for sharing or printing, with headings styled for readability.
- **Intermediate Outputs**: Each stage of the pipeline produces intermediate files, saved in the `intermediate/` folder for debugging and transparency:
  - `research_output.txt`: Captures the selected topic and key points from the research phase.
  - `outline.txt`: Contains the blog’s structural outline.
  - `blog_post.txt`: The initial draft from the Content Generation Agent.
  - `optimized_blog_post.txt`: The SEO-optimized draft before final review.
- **SEO Optimization**: The system targets specific keywords ("HR trends 2025", "Artificial Intelligence in HR", "automation in HR") to improve search engine visibility. It ensures:
  - **Keyword Density**: 1-2% to avoid over-optimization while maintaining relevance.
  - **Meta Description**: A concise 150-160 character summary for search engine results.
  - **Heading Structure**: Proper use of H1 (title), H2 (main sections), and H3 (subsections) to enhance readability and SEO.
  - **Content Depth**: Includes examples, statistics, and actionable insights to increase engagement and dwell time, key factors for SEO ranking.

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
