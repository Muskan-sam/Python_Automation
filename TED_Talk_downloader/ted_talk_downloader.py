import requests #getting content of the ted talk page

import bs4 #web scraping

import re #regular expressions

from urllib.request import urlretrieve #downloading the video

import sys #for arguments parsing

#exception handling
if len(sys.argv)>1:
    url = sys.argv[1]
else:
   sys.exit("ERROR: Please provide the url of the ted talk")

#url = 'https://www.ted.com/talks/malcolm_gladwell_choice_happiness_and_spaghetti_sauce/'
#url = 'https://www.ted.com/talks/ken_robinson_says_schools_kill_creativity'
#url = 'https://www.ted.com/talks/adam_mosseri_a_creator_led_internet_built_on_blockchain'

r = requests.get(url)
print("Download about to start")
soup = bs4.BeautifulSoup(r.content, features="lxml")

#finding the video url
for val in soup.findAll('script', attrs={'type':'application/json'}):
    if(re.search("py.tedcdn.com", str(val))) is not None:
      result = str(val)
      print(result)
      
p = re.compile(r'(?P<url>https?://[^\s]+)(mp4)')
result_mp4 = re.search(p, result).group("url")
mp4_url = result_mp4.split('"')[0]
print("Downloading video from ... "+mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split("?")[0]
print("Saving in ... "+file_name)

r = requests.get(mp4_url)

with open(file_name, 'wb') as f:
  f.write(r.content)

print("Download complete")
        

