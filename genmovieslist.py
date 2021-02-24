import os, json, urllib.request
os.remove('movies-list.md')
url = 'https://api.trakt.tv/users/tomyangsh/collection/movies'
headers = {'trakt-api-key': '4fb92befa9b5cf6c00c1d3fecbd96f8992c388b4539f5ed34431372bbee1eca8'}
req = urllib.request.Request(url, None, headers)
with urllib.request.urlopen(req) as response:
  res = response.read().decode()
resjson = json.loads(res)
for i in range(0, len(resjson)-1):
  tmdbid = resjson[i]['movie']['ids']['tmdb']
  with urllib.request.urlopen('https://api.themoviedb.org/3/movie/'+str(tmdbid)+'?api_key=b729fb42b650d53389fb933b99f4b072&language=zh') as response:
    tmdbinfo = json.loads(response.read().decode())
  f = open('movies-list.md', "a")
  f.write(tmdbinfo['title']+'\n\n')
  f.close()
  i = i+1
