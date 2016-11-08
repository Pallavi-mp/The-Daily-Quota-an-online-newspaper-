import re
import urllib.request
import urllib.parse
url='http://timesofindia.indiatimes.com'
try:
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))

newfile = open('index.html','w')

newfile.write("""<html><body><title>headlines</title><link type="text/css" rel="stylesheet" href="page.css"> </head>

<body>
<div id="about"></div>
<a href="index.html"><div id="a1" class="tab">HOME</div></a>
<a href="st.html"><div id="a2" class="tab">STOCK MARKET</div></a>
<a href="sports.html"><div id="a3" class="tab">SPORTS</div></a>
<a href="world.html"><div id="a4" class="tab">WORLD</div></a>
<a href="tech.html"><div id="a5" class="tab">TECHNOLOGY</div></a>
<a href="education.html"><div id="a8" class="tab">DISCUSSION</div></a>
<a href="travel.html"><div id="a7" class="tab">TRAVEL & FOOD</div></a>
<a href="entertainment.html"><div id="a6" class="tab">ENTERTAINMENT</div></a>
<div id="d0" class="box1"><div id="daily">The Daily Quota</div></div>
<div id="d1" class="box2"><br><br><br><br><p class="bg">Terrorists attack Army, BSF camps in Baramulla, one jawan martyred</p></div>
<div id="d2" class="box2"><br><br><br><br><p class="bg">Japan's Yoshinori Ohsumi wins Nobel Medicine Prize for work on cell 'recycling'</p></div>
<div id="d3" class="box2"><br><br><br><br><p class="bg">Paris deal: India committed, says PM Modi as Obama tweets praise, Ban Ki-moon says 'dhanyawad'</div>
<div id="d4" class="box2"><br><br><br><br><p class="bg">Weighty issue: 12-year-old Nagpur boy launches agitation against heavy schoolbags</p></div>
<div id="d5" class="box2"><br><br><br><br><p class="bg">Method to control 'hot' electrons comes a step closer</p></div>
<div id="d6" class="box2"><br><br><br><br><p class="bg">Siddharamaiah says Karnataka is a victim and not the villain in Cauvey row.</p></div>
""")
              

print("latest news")
data=str(respData)
newfile.write("""<div id = "news"><h1>LATEST NEWS</h1>""")

news=re.findall(r'<ul data-vr-zone="latest" class="list9">(.*?)</ul>',data)
a=news[0].split("title=")
b=0
for i in a:
    
    if ("href" in i):
        print(i.split("href")[0])
        newfile.write("""<p>""")
        #newfile.write(str(b+1))
        #newfile.write("""" class="box2"><br><br><br><br><p class="bg">""")
        newfile.write(i.split("href")[0])
        
        newfile.write("</p>")
        b=b+1
        if(b==6):
            break
        
newfile.write("</div><hr width='90%'></body></html>")       
newfile.close()


