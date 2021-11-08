import os

with open("file_path.txt","r") as f:
    file = f.readline().strip('\n')
    number = f.readline().strip('\n')
f.close()


sendMessage = f"""
tell application "Messages"
    set targetService to 1st account whose service type = iMessage
    set targetBuddy to participant "{number}" of targetService
    set targetFileName to POSIX file "{file}"
    send targetFileName to targetBuddy
end tell
"""
with open('sendfile.applescript','w') as f:
    f.write(sendMessage)
f.close()

os.system("osascript sendfile.applescript")
