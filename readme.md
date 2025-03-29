

## Project Overview

This project is designed to automate the process of researching, analyzing, and generating content on a specific topic. In this case, the topic is "medical industry using generative AI." The system uses advanced tools like **Groq API** for natural language processing and **Serper API** for web searches to gather, analyze, and create high-quality content.

![Screenshot 2025-03-29 165903](https://github.com/user-attachments/assets/468f617f-18df-45d7-84e6-34f030cea070)

## Project Breakdown

### Key Components:

- **Agent1 - Senior Research Analyst**: An expert in advanced web research, responsible for gathering, analyzing, and summarizing the latest information from the web.
  
- **Agent2 - Content Writer**: A skilled writer who transforms the research findings into engaging and informative content.

- **LLM (Language Model)**: A model used to enhance the agents' abilities in processing natural language and generating insights. In this case, the "groq/llama-3.1-70b-versatile" model is being used.

- **Tools**:
  - **SerperDevTool**: Used for conducting web searches and collecting the most relevant search results.
  - **dotenv**: For managing environment variables and API keys securely.

![alt text](<Screenshot 2025-03-29 165325.png>)
### Workflow

1. **Research Phase**: The Senior Research Analyst agent uses the **SerperDevTool** to gather current trends, market analysis, regulatory updates, and more. After evaluating the credibility of sources, the findings are compiled into a structured research brief.
  
2. **Content Creation Phase**: The Content Writer agent uses the research findings to create an engaging, SEO-optimized content piece. The content is tailored to the target audience and includes case studies, examples, and relevant citations.

3. **Crew Execution**: Both the agents work in coordination under the **Crew** class, which handles their tasks and executes them in a collaborative manner.

### Tools and Libraries Used

- **crewai**: For creating and managing intelligent agents (Agent, Task, Crew, LLM).
- **crewai_tools**: For using additional tools like the **SerperDevTool**.
- **dotenv**: For securely loading API keys from environment variables.
- **os**: For system-level operations like accessing environment variables.

## Setup Instructions

### Prerequisites

Before running the project, ensure that the following tools are installed:

1. Python 3.7 or above.
2. Install the necessary Python libraries:
    ```bash
    pip install crewai crewai_tools python-dotenv
    ```

3. Set up environment variables for **GROQ_API_KEY** and **SERPER_API_KEY**.

### .env File Example

```env
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

### Running the Project

1. Clone this repository or download the code.
2. Set up your environment variables as described in the `.env` file.
3. Run the script to begin the research and content creation process:

```bash
python your_script_name.py
```

The script will start by running the **Senior Research Analyst** agent to gather research. Then, the **Content Writer** agent will create content based on the research findings. 

## Task Breakdown

### Research Task (Agent 1: Senior Research Analyst)

- **Objective**: Conduct comprehensive research on the topic, including current trends, market analysis, regulatory updates, and more.
- **Expected Output**: A detailed report containing research findings, source list, and a structured research brief with fact-checked information.

### Content Writing Task (Agent 2: Content Writer)

- **Objective**: Create an engaging and informative content piece based on the research findings. Ensure accuracy, reliability, and clarity.
- **Expected Output**: A high-quality content piece that includes research insights, examples, SEO best practices, and proper citations.

## Agent Workflow

1. **Senior Research Analyst**: Conducts the research, evaluates source credibility, and produces a detailed report.
2. **Content Writer**: Uses the report to create content that is engaging, informative, and SEO-friendly.

## Example of Output

The output of the entire process is a high-quality content piece tailored to the topic, such as:

- A comprehensive research report on the medical industry using generative AI, containing the latest trends, data, and key insights.
- A content piece that is well-structured, informative, and SEO-optimized for publication.

## Customization

You can easily customize this workflow for any other topic by changing the value of the `topic` variable in the script. The agents will automatically adjust their behavior based on the new topic.

```python
topic = "your_new_topic_here"
```

## License

This project is open source and available under the MIT License. See the LICENSE file for more details.

---

Feel free to reach out if you encounter any issues or have any questions!

---

### Enjoy the Automation! 🚀

