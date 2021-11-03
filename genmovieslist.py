import os, json, urllib.request
from itertools import chain
from pypinyin import pinyin, Style
os.remove('movies-list.md')

list = []
url = 'https://api.trakt.tv/users/tomyangsh/collection/movies'
headers = {'trakt-api-key': '4fb92befa9b5cf6c00c1d3fecbd96f8992c388b4539f5ed34431372bbee1eca8'}
req = urllib.request.Request(url, None, headers)
with urllib.request.urlopen(req) as response:
  res = response.read().decode()
resjson = json.loads(res)

for i in range(0, len(resjson)):
    tmdbid = resjson[i]['movie']['ids']['tmdb']
    try:
        with urllib.request.urlopen('https://api.themoviedb.org/3/movie/'+str(tmdbid)+'?api_key=b729fb42b650d53389fb933b99f4b072&language=zh-CN') as response:
            tmdbinfo = json.loads(response.read().decode())
        list.append(tmdbinfo['title']+' ('+str(resjson[i]['movie']['year'])+')')
        i = i+1
    except:
        i = i+1
        continue

def to_pinyin(s):
    return ''.join(chain.from_iterable(pinyin(s, style=Style.TONE3)))
list = sorted(list, key=to_pinyin)

for x in range(0, len(list)):
  f = open('movies-list.md', "a")
  f.write(list[x]+'\n\n')
  f.close()
  i = i+1
