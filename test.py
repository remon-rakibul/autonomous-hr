from langchain_community.tools.gmail.get_thread import GmailGetThread
from langchain_community.tools.gmail.get_message import GmailGetMessage
from langchain_community.tools.gmail.create_draft import GmailCreateDraft
from langchain_community.agent_toolkits import GmailToolkit
# from langchain.tools import tool

# tool = GmailGetThread()
# tool = GmailGetMessage()
tool = GmailCreateDraft()

# result = tool.run({"thread_id": "190b5fce91a28d0f"})
# result = tool.run({"message_id": "1910c8f404c2cdb0"})
result = tool.run({
    'to': ['test@gmail.com'],
    'subject': 'test',
    'message': 'test message'
})
print(result)
# print(result["body"])
# print(result["subject"])
# print(result["sender"])

data = "hazrat.arisaftech@gmail.com|Discussion on LLM Project Development|Dear Hazrat Ali,\n\nThank you for sharing the update on our ongoing large language model (LLM) project. I appreciate your efforts to implement strategies for data augmentation.\n\nTo further enhance model performance, I recommend exploring additional techniques such as hyperparameter tuning and establishing comprehensive evaluation metrics. It would also be beneficial to discuss potential external collaborations or resources that could support our project.\n\nPlease let me know your availability for a meeting next week to discuss these matters in more detail.\n\nBest regards,\nMd Rakibul Haque"

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
#     print(data)
#     email, subject, message = data.split('|')
#     gmail = GmailToolkit()
#     draft = GmailCreateDraft(api_resource=gmail.api_resource)
#     result = draft.run({"data":{
# 				'to': [data['email']],
# 				'subject': data['subject'],
# 				'message': data['message']
# 		}})
#     return f"\nDraft created: {result}\n"