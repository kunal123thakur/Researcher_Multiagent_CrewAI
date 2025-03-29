from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool


from dotenv import load_dotenv
import os
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
topic = "medical industry using generative ai"

#tool 1
llm = LLM(
    model="groq/deepseek-r1-distill-llama-70b",
    # api_key = GROQ_API_KEY,
    temperature=0.7
)


#tool 2 web search tool (serper dev tool)

search_tool = SerperDevTool(n=5) # n is the number of search results to return

#Agent1
Senior_research_analyst = Agent(
    role = "Senior Research Analyst",
    goal = f"Research, analyze and summarize the latest information on {topic} from the web",
    backstory= "An expert in advanced web research, the Senior Research Analyst excels at searching across the internet to gather the most relevant and up-to-date information"
                " With a keen eye for detail, they are proficient in fact-checking and cross-checking data to ensure accuracy and reliability"
                " Their extensive experience and dedication make them an invaluable asset in the field of research and analysis."
                " The Senior Research Analyst is committed to providing high-quality insights and reports to support informed decision-making and strategic planning.",
    allow_delegation = False,# the agent can't delegate the task to another agent
    verbose=True,#debugging
    tool=search_tool,
    llm=llm

)

#Agent2 Content writer
Content_writer = Agent(
    role = "Content Writer",
    goal = f"Create engaging and informative content on {topic} based on the research findings",
    backstory= "A skilled and creative writer, the Content Writer specializes in transforming complex information into engaging and informative content"
                " With a talent for storytelling and a passion for communication, they craft compelling narratives that captivate and inform the audience"
                " Their ability to distill key insights and present them in a clear and concise manner makes them an essential contributor to the team"
                " The Content Writer is dedicated to producing high-quality content that educates, entertains, and inspires readers.",
    allow_delegation = False,# the agent can't delegate the task to another agent
    verbose=True,#debugging
    llm=llm

) 

#Research Tasks

research_task = Task(
    description=("""
            1.conduct comprehensive research on including:
                -current trends and developments
                -key industry trends and innovation
                -statistical data and market analysis
                -regulatory updates and policy changes
            2.Evaluate source credibility and fact-check information
            3.organize finding into a structured research brief
            4.include all relevant citations and sources            
    """),
    expected_output="""A detailed research report containing
        -research findings and analysis
        -structured research brief with citations
        -source list
        -fact-checked information
        -clear categorization of main themes and patterns
        
        Please format with clear sections and bullet points for easy readability""",
    agent=Senior_research_analyst,

)

#Content writing task

content_writing_task = Task(
    description=("""
            1. Create engaging and informative content based on the research findings
            2. Ensure accuracy and reliability of information
            3. Write in a clear and concise manner
            4. Include relevant examples and case studies to support key points
            5. Tailor content to the target audience and platform
            6. Incorporate SEO best practices for online content
            7. Provide proper citations and references for all sources used
            8. Review and revise content as needed for quality and clarity
    """),
    expected_output="""A well-written and engaging content piece that:
        -presents key research findings in an informative manner
        -is accurate, reliable, and well-researched
        -includes relevant examples and case studies
        -is tailored to the target audience and platform
        -incorporates SEO best practices
        -provides proper citations and references
        -is reviewed and revised for quality and clarity
        
        Please ensure the content is engaging and informative, with a clear structure and flow""",
    agent=Content_writer,

)

#Crew
research_crew = Crew(
    # name="Research Crew",
    agents=[Senior_research_analyst, Content_writer],
    tasks=[research_task, content_writing_task],
    verbose=True
    # llm= yaha ek llm use kr sakte hain heirarchical tasks ke liye

)

# result = research_crew.kickoff(input={"topic":topic})
result = research_crew.kickoff({"topic": topic})
print(result)