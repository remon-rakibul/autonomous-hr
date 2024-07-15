from langchain_community.tools.gmail.get_thread import GmailGetThread


tool = GmailGetThread()

result = tool.run({"thread_id": "190a019e43f5746a"})
print(result)
