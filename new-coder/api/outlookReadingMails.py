import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6)

messages = inbox.Items

print messages

message = messages.GetLast()
body_content = message.subject
print body_content