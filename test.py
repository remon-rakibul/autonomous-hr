from langchain_community.tools.gmail.get_thread import GmailGetThread
from langchain_community.tools.gmail.get_message import GmailGetMessage

# tool = GmailGetThread()
tool = GmailGetMessage()

# result = tool.run({"thread_id": "190b5fce91a28d0f"})
result = tool.run({"message_id": "190b5fce91a28d0f"})
print(result)
print(result["body"])
print(result["subject"])
print(result["sender"])