from langchain_community.tools.gmail.create_draft import GmailCreateDraft
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools.gmail.get_thread import GmailGetThread
from langchain_community.tools.gmail.get_message import GmailGetMessage
from langchain_community.agent_toolkits import GmailToolkit
from langchain.tools import tool

# class CreateDraftTool():
#   @tool("Create Draft")
#   def create_draft(data):
#     """
#     	Useful to create an email draft.
#       The input to this tool should be a pipe (|) separated text
#       of length 3 (three), representing who to send the email to,
#       the subject of the email and the actual message.
#       For example, `lorem@ipsum.com|Nice To Meet You|Hey it was great to meet you.`.
#     """
#     email, subject, message = data.split('|')
#     gmail = GmailToolkit()
#     draft = GmailCreateDraft(api_resource=gmail.api_resource)
#     result = draft.run({
# 				'to': [email],
# 				'subject': subject,
# 				'message': message
# 		})
#     return f"\nDraft created: {result}\n"


class CreateDraftTool():
  @tool("Create Draft")
  def create_draft(email,message,subject):
    """
 		Useful to create an email draft.
    """
    # email, subject, message = data.split('|')
    # email, subject, message = data['email'],data['subject'],data['message']
    # print(f'data: {data}')
    print('email: ',email.strip("\""))
    # print(type(email))
    print('subject: ',subject.strip("\""))
    print('message: ',message.strip("\""))
    # if email[0] == "'" or email[0] == '"':
    #      email = email[1:]
    #      email = str(email)
    # print(email)
    gmail = GmailToolkit()
    draft = GmailCreateDraft(api_resource=gmail.api_resource)
    result = draft.run({
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
   def get_gmail_message(message_id):
      """
      Useful to get a gmail message.
      The input to the tool should be the message id of an email.
      """
      # print("message id from llm")
      # print(message_id)
      # print(type(message_id))
      # print(str(message_id))
      if message_id[0] == "'" or message_id[0] == '"':
         message_id = message_id[1:]
         message_id = str(message_id)
      # print(message_id)
      gmail = GmailToolkit()
      tool = GmailGetMessage(api_resource=gmail.api_resource)
      result = tool.run({"message_id": message_id})
      return {
         'message_id': result['id'],
         'subject': result['subject'],
         'body': result['body'],
         'sender': result['sender']
         }
   
# CreateDraftTool.create_draft("hazrat.arisaftech@gmail.com|Discussion on LLM Project Development Response|Hi Hazrat, thank you for sharing the progress and next steps of our ongoing large language model (LLM) project. I have reviewed the points you highlighted and appreciate your input on data augmentation strategies, hyperparameter tuning, evaluation, and establishing comprehensive metrics for model performance. I agree that addressing challenges related to data diversity and model overfitting is crucial to the project's success. I am available to meet next week to discuss these matters in more detail. Please let me know a suitable time and date. Best regards, Md Rakibul Haque")