# WEB SCRAPER
Web Scraper escrito en Python, empleando el patron **Page Object Pattern** y la libreria **argparse** para manejo de **CLI** y **csv** para la salida del *scraping*

- **config.yaml**: En este archivo se organiza la información de configuración. Se transforma en un diccionario dentro del código.

- **common.py**: Se importa librería yaml empleada para convertir el 
archivo de configuración en un diccionario para ser utilizado en Python.

- **news_page_objects.py**: abstración del modelo de las páginas sujetas a *scraping*.

- **main.py**: definición de las operaciones de *scraping* a realizar.