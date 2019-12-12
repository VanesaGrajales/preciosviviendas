import requests
import bs4
from urllib.error import HTTPError
from requests.exceptions import ConnectionError
from urllib.error import URLError

#Esta funcion se realiza para verificar que la pagina web no genera error
#https://www.udemy.com/course/python_webscraping/

def abrir(url):
    try:
        var = "no error"
        read = requests.get(url)
        requests.session().close()
    except HTTPError as e:
        var = "ocurrio error"
    except URLError as e:
        var = "ocurrio error"
    except ConnectionError as e:
        var = "ocurrio error"
    if (var == "no error"):
        return read
    else:
        return "error al abrir"



