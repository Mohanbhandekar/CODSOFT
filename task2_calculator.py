s=input();
l=['+','-','*','/','%'];
for i in l:
    if i in s:
        operator=i
s=s.split(operator)
if operator=='+':
    result=int(s[0])+int(s[1])
elif operator=='-':
    result=int(s[0])-int(s[1])
elif operator=='*':
    result=int(s[0])*int(s[1])
elif operator=='/':
    result=int(s[0])/int(s[1])
elif operator=='%':
    result=int(s[0])%int(s[1])
print(result)
