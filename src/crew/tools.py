from langchain_community.tools.gmail.create_draft import GmailCreateDraft
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools.gmail.get_thread import GmailGetThread
from langchain_community.tools.gmail.get_message import GmailGetMessage
from langchain_community.agent_toolkits import GmailToolkit
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
  

class CreateTavilySearchTool():
    @tool("Search Web")
    def search_web(query):
      """
      Useful to search the web and get results.
      The input should be a query in string format to search the web.
      """
      tool = TavilySearchResults()
      result = tool.run({"query": query})
      return result
    

class CreateGmailMessageTool():
   @tool("Get Gmail Message")
   def get_gmail_message(message_id: str):
      """
      Useful to get a gmail message.
      The input to the tool should be the thread id of an email in string format.
      """
      gmail = GmailToolkit()
      tool = GmailGetMessage(api_resource=gmail.api_resource)
      result = tool.run({"message_id": message_id})
      return result