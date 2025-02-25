from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class JiraTaskRequestFlowAutomationForCrewManagementCrew():
    """JiraTaskRequestFlowAutomationForCrewManagement crew"""

    @agent
    def task_fetcher(self) -> Agent:
        return Agent(
            config=self.agents_config['task_fetcher'],
            tools=[],
        )

    @agent
    def jira_authenticator(self) -> Agent:
        return Agent(
            config=self.agents_config['jira_authenticator'],
            tools=[],
        )


    @task
    def fetch_active_tasks_task(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_active_tasks_task'],
            tools=[],
        )

    @task
    def authenticate_jira_task(self) -> Task:
        return Task(
            config=self.tasks_config['authenticate_jira_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the JiraTaskRequestFlowAutomationForCrewManagement crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
