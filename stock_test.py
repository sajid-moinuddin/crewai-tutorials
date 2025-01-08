from crewai_tools import SpiderTool, SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool, SeleniumScrapingTool
from crewai import Agent, Task, Crew
from utils import get_openai_api_key, get_serper_api_key, get_spider_api_key
from dotenv import load_dotenv
import os
import warnings


def main():


    # Warning control
    warnings.filterwarnings('ignore')

    # Load environment variables
    load_dotenv()

    # Set OpenAI API key and model name
    openai_api_key = get_openai_api_key()
    os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o'
    os.environ["SERPER_API_KEY"] = get_serper_api_key()



    spider_tool = SpiderTool()

    searcher = Agent(
        role="Web Research Expert",
        goal="Find related information from specific URL's",
        backstory="An expert web researcher that uses the web extremely well",
        tools=[spider_tool],
        verbose=True,
    )

    return_metadata = Task(
        description="Scrape https://spider.cloud with a limit of 1 and enable metadata",
        expected_output="Metadata and 10 word summary of spider.cloud",
        agent=searcher
    )

    crew = Crew(
        agents=[searcher],
        tasks=[
            return_metadata,
        ],
        verbose=True
    )

    crew.kickoff()

if __name__ == "__main__":
    main()
