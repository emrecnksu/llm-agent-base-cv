# llm_agent/llm_agent/crew_setup.py

from crewai import Crew
from llm_agent.tasks import create_analyze_cv_task, create_improve_cv_task
from llm_agent.agents import get_agents 

def run_crew(cv_text: str, language: str = "en"):
    cv_analyst_agent, cv_writer_agent = get_agents(language)

    analyze_task = create_analyze_cv_task(cv_analyst_agent, cv_text, language)
    improve_task = create_improve_cv_task(cv_writer_agent, cv_text, analyze_task, language)

    crew = Crew(
        agents=[cv_analyst_agent, cv_writer_agent],
        tasks=[analyze_task, improve_task]
    )

    result = crew.kickoff()
    return result
