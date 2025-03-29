import streamlit as st
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Streamlit UI setup
st.set_page_config(page_title="AI Research Crew", layout="wide")
st.title("🔍 AI-Powered Research Crew")
st.write("Automated research and content creation using CrewAI.")

# User input for topic
topic = st.text_input("Enter a topic for research:", "medical industry using generative AI")

# Define LLM model
llm = LLM(model="groq/deepseek-r1-distill-llama-70b", temperature=0.7)

# Web search tool
search_tool = SerperDevTool(n=5)

# Define Agents
Senior_research_analyst = Agent(
    role="Senior Research Analyst",
    goal=f"Research and summarize the latest information on {topic}",
    backstory="An expert in advanced web research, providing accurate insights.",
    allow_delegation=False,
    verbose=True,
    tool=search_tool,
    llm=llm
)

Content_writer = Agent(
    role="Content Writer",
    goal=f"Create engaging content on {topic} based on research findings",
    backstory="A skilled writer who transforms research into clear and engaging content.",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# Define Tasks
research_task = Task(
    description="""
        Conduct comprehensive research including:
        - Trends, innovations, and statistical data
        - Regulatory updates and policy changes
        - Source credibility evaluation and fact-checking
        - Structured research brief with citations
    """,
    expected_output="A structured research report with sources, fact-checked insights, and categorized themes.",
    agent=Senior_research_analyst
)

content_writing_task = Task(
    description="""
        - Create engaging content based on research findings
        - Ensure accuracy and reliability
        - Include examples, case studies, and SEO optimization
        - Provide citations and references
    """,
    expected_output="A high-quality, well-structured content piece tailored for the audience.",
    agent=Content_writer
)

# Initialize Crew
research_crew = Crew(
    agents=[Senior_research_analyst, Content_writer],
    tasks=[research_task, content_writing_task],
    verbose=True
)

# Run the Crew
if st.button("Start Research"):
    st.write("🚀 Research in progress...")
    result = research_crew.kickoff({"topic": topic})
    st.success("✅ Research Completed!")
    st.subheader("📌 Research Findings:")
    st.write(result)
