import requests

import time

import re

url="http://www.jjwxc.net/onebook.php?novelid=109034&chapterid=1"
response=requests.get(url)
response.encoding='gb2312'
html=response.text
html= html.replace("<br>", "")
info=re.findall(r'<div style="clear:both;">([\s\S]*)<div id="favoriteshow_3" style="display:none" align="center"></div>',html)[0]
print(info)



#x=1
#url="http://www.jjwxc.net/onebook.php?novelid=109034&chapterid={}".format(x)
#while(x<10):
#response=requests.get(url)
#html=response.encode('utf-8')
#re.findall(html,<div style="clear:both;"></div>.*?<div id="favoriteshow_3" style="display:none" align="center"></div>)
#time.sleep(500)