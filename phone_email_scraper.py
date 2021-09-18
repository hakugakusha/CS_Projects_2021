import re
text = open("arkansas_tech_u_directory.txt", "r").read()

phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))? 
(\s|-)
\d\d\d
-
\d\d\d\d
(((ext(\.)?\s)|x) 
 (\d{2,5}))?
)
''', re.VERBOSE)

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+
''', re.VERBOSE)

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber)

allEmails = []
for email in extractedEmail:
    allEmails.append(email)

print(allEmails)
print(allPhoneNumbers)



