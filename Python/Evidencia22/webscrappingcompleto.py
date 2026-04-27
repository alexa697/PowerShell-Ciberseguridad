import requests, os, bs4, random

# Crear carpeta para guardar imágenes
os.makedirs('xkcd', exist_ok=True)

# Generar 5 números aleatorios de cómics
comic_ids = random.sample(range(1, 2800), 5)

for comic_id in comic_ids:
    url = f'https://xkcd.com/{comic_id}/'
    print(f'Descargando página {url}...')

    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        comicElem = soup.select('#comic img')

        if comicElem == []:
            print('No se encontró imagen en esta página.')
            continue

        comicUrl = comicElem[0].get('src')

        if not comicUrl:
            print('No se encontró URL de imagen.')
            continue

        print(f'Descargando imagen: {comicUrl}')
        response = requests.get('https:' + comicUrl)
        response.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

        for chunk in response.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    except Exception as e:
        print(f'Error al procesar {url}: {e}')
print('Descarga completada.')