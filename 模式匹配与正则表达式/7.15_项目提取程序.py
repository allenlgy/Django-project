import re, pyperclip

# 1. 为电话号码创建一个正则表达式
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)                       # separator
    (\d{3})                         # first 3 digit
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|xext\.)\s*(\d{2,5}))?  # extension
    )''',re.VERBOSE)

# 2. 为 E-mail 地址创建一个正则表达式
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # username
    @                           # @ symbol
    [a-zA-Z0-9.-]+              # domain name
    (\.[a-zA-Z]{2,4})           # dot-something
    )''',re.VERBOSE)

# 3. 在剪贴板文本中找到所有匹配
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

print(matches)

# 4. 所有匹配连接成一个字符串，复制到剪贴板
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')