#! python3
import requests, os, bs4

url = 'http://xkcd.com/3139' # starting url
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

# Download the page.
print('Downloading page %s...' % url)
res = requests.get(url)

soup = bs4.BeautifulSoup(res.text, "html.parser")
comicElem = soup.select('#comic img')

if comicElem == []:
    print('No se encontró.')
else:
    print(comicElem[0])
    input()
    comicUrl = comicElem[0].get('src')
    print('Descargando %s...' % (comicUrl))
    response = requests.get('http:'+comicUrl)

    if response.status_code == 200:
        imageFile = open(os.path.join('xkcd',
                                      os.path.basename(comicUrl)),
                         'wb')#wb, rb

        for chunk in response.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
print('Hecho.')