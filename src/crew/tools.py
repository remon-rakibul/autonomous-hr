from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.create_draft import GmailCreateDraft
from langchain_community.tools.gmail.get_thread import GmailGetThread
from langchain.tools import tool

class CreateDraftTool():
  @tool("Create Draft")
  def create_draft(data):
    """
    	Useful to create an email draft.
      The input to this tool should be a pipe (|) separated text
      of length 3 (three), representing who to send the email to,
      the subject of the email and the actual message.
      For example, `lorem@ipsum.com|Nice To Meet You|Hey it was great to meet you.`.
    """
    email, subject, message = data.split('|')
    gmail = GmailToolkit()
    draft = GmailCreateDraft(api_resource=gmail.api_resource)
    result = draft({
				'to': [email],
				'subject': subject,
				'message': message
		})
    return f"\nDraft created: {result}\n"



class CreateGmailThreadTool():
  @tool("Get Gmail Thread")
  def get_gmail_thread(thread_id: str) -> str:
      """
      Useful to get a gmail thread.
      The input to the tool should be the thread id of an email in string format.
      """
      gmail = GmailToolkit()
      tool = GmailGetThread(api_resource=gmail.api_resource)
      result = tool.run({"thread_id": thread_id})
      return result