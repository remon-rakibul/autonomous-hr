from crewai import Crew
from langchain_community.callbacks import get_openai_callback

from .agents import EmailFilterAgents
from .tasks import EmailFilterTasks

class EmailFilterCrew():
	def __init__(self):
		agents = EmailFilterAgents()
		self.filter_agent = agents.email_filter_agent()
		self.action_agent = agents.email_action_agent()
		self.writer_agent = agents.email_response_writer()

	def kickoff(self, state):
		print("### Filtering emails")
		tasks = EmailFilterTasks()
		crew = Crew(
			agents=[self.filter_agent, self.action_agent, self.writer_agent],
			tasks=[
				tasks.filter_emails_task(self.filter_agent, self._format_emails(state['emails'])),
				tasks.action_required_emails_task(self.action_agent),
				tasks.draft_responses_task(self.writer_agent)
			],
			# full_output=True,
			verbose=True,
			# output_token_usage=True,

		)
		# with get_openai_callback() as cb:

		result = crew.kickoff()
			# # print(cb)
			
			# print("\n\n")
			# print(f"Total Tokens: {cb.total_tokens}")
			# print(f"Prompt Tokens: {cb.prompt_tokens}")
			# print(f"Completion Tokens: {cb.completion_tokens}")
			# print(f"Successful Requests: {cb.successful_requests}")
			# print("\n\n")


		# print("crew usages metrics: ")
		# print(crew.usage_metrics)
		return {**state, "action_required_emails": result}

	def _format_emails(self, emails):
		emails_string = []
		for email in emails:
			# print(email)
			arr = [
				# f"ID: {email['id']}",
				f"- Thread ID: {email['threadId']}",
				f"- Snippet: {email['snippet']}",
				f"- From: {email['sender']}",
				f"--------"
			]
			emails_string.append("\n".join(arr))
		return "\n".join(emails_string)