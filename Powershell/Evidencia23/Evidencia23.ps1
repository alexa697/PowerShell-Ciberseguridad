"""cd C:\Users\HP\Documents\GitHub\PowerShell-Ciberseguridad\Powershell\Evidencia23
python -m pip install scrapy
python -m scrapy startproject noticias_fcfm
cd noticias_fcfm
python -m scrapy genspider noticias_fcfm_cl noticias.fcfm.cl"""

#python -m scrapy crawl noticias -a termino=ciberseguridad
#correr en terminal directo ya sea PS o CMD, no en el script de powershell

.\venv\Scripts\Activate.ps1
python -m scrapy crawl noticias -a termino=Atilano

# Luego, edita el archivo noticias_fcfm/noticias_fcfm/spiders/noticias_fcfm_cl.py con el siguiente contenido:
