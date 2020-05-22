import requests
import re
import json
import sys
from urllib import parse
def parse_url(url):
   return parse.urlparse(url)

def all_urls(html,url=None):
    urls=re.findall("""(?:href|src|action|ping)[ ]*?=[ ]*?("|')([\s\S]*?)\\1""",html,re.I)
    url_token=[token for _,token in urls]
    print(url_token)

def parse_forms(html,url=None):
    forms=re.findall("""<\s*?form([\s\S]*?)\s*?>([\s\S]*?)<\s*?/\s*?form\s*?>""",html,re.I)
    formlist=[]
    for attr,inners in forms:      
        method=re.findall("""method[ ]*?=[ ]*?("|')([\s\S]*?)\\1""",attr,re.I)
        if method:
            _,method=method[0]
        else:
            method="GET"
        action=re.findall("""action[ ]*?=[ ]*?("|')([\s\S]*?)\\1""",attr,re.I)
        if action:
            _,action=action[0]
        else:
            action=url or ""
        fields=[]
        remarks=""
        for inp_attr in re.findall("""<\s*?input([\s\S]*?)\s*?>""",inners,re.I):
            inptype=re.findall("""type[ ]*?=[ ]*?("|')([\s\S]*?)\\1""",inp_attr,re.I)
            if inptype:
                _,inptype=inptype[0]
            else:
                inptype="text"
            name=re.findall("""name[ ]*?=[ ]*?("|')([\s\S]*?)\\1""",inp_attr,re.I)
            if name:
                _,name=name[0]
            else:
                name=""
                remarks="Handle-Manually" if inptype.lower() !="submit" else ""
            value=re.findall("""value[ ]*?=[ ]*?("|')([\s\S]*?)\\1""",inp_attr,re.I)
            if value:
                _,value=value[0]
            else:
                value=""
            fielditem={"type":inptype,"name":name,"value":value}
            fields.append(fielditem)
        formitem={"method":method,"action":action,"fields":fields,"remarks":remarks}
        formlist.append(formitem)
    return formlist


if __name__ == "__main__":
    if len(sys.argv)>1:
        url=sys.argv[1]  
    else:
        url="https://www.google.com"
    if "http" not in url:
        url="https://"+url
    forms=parse_forms(requests.get(url).text,url=url)
    print(json.dumps(forms,indent=4))



