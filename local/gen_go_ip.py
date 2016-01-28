file='ip_tmpok.txt'
f=open(file,'r')
t=f.read()
import re

p = re.compile(r'((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))')
rs=p.findall(t)
rs=[x[0] for x in rs]
rt=''
for r in rs:
    rt= rt+ r +'|'
print rt



