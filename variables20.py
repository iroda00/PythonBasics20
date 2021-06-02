msg = 'Hello'
language = 'Python'
msg_with_lan = msg + language

print(msg + language)
print(msg_with_lan)
print(f"{msg}{language}")
print(f"the sum of 25 +500 is: {25+500}")
  ### whitespaces spaces, enter, tabs,
print(f"\tmessage : {msg.title()}")
print(f"\tmessage: \n\t{msg.title()}")
msg = '    john doe    '
print(msg.strip())
print(msg.lstrip())
print(msg.rstrip())
msg1 = "Hello, would you like to learn Python today"
print(msg1)
person_name = 'eric'
print(f"\tHello {person_name.title()}, \n\twant to learn Python?")
print(f"Hello {person_name.title()}, want to learn Python?")

###str.split()
### str.split('delimiter')

full_name = 'john,doe'
full_name.split(',')
print(full_name)
['john', 'doe']
print(full_name)
full_name = 'john/doe'
print(full_name.split('/'))
['john', 'doe']
full_name = ' john/doe/45679'
print(full_name.split('/'))
print(full_name.split(' '))
