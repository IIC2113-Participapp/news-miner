
# :snake: NewsMiner :snake:

## Descripción
En pocas palabras, este microcomponente realiza una *minería* de noticias a partir diferentes fuentes, para, después, entregarlas a la aplicación principal. Para llevar a cabo su implementación, decidimos seguir el [*__open/closed principle__*](https://en.wikipedia.org/wiki/Open/closed_principle). Nuestra intención es que, al momento de agregar una nueva fuente, el código escrito en Python (casi) no sufra modificaciones. Luego, sólo se deberá agregar *metadata* en el archivo JSON.

## Herramientas
[Python] será nuestra principal herramienta de trabajo. :snake:<br>
:warning: Para evitar fallas de compatibilidad, se **debe** usar la versión **3.4.X**.

### Librerías de Python
Las librerías utilizadas están resumidas en la siguiente tabla.

| Nombre           | ¿Y para qué?                             | Versión    |
| ---------------- | ---------------------------------------- | ---------- |
| [beautifulsoup4] | Para hacer *parsing* de documentos HTML. | **4.4.0**  |
| [requests]       | Para hacer solicitudes HTTP.             | **2.7.0**  |

Todas ellas aparecen, además, en el archivo `requirements.txt`. Luego, se **debe** usar este archivo para instalarlas con `pip`. Esto permite que tengamos las mismas versiones al momento de trabajar, consiguiendo instalaciones **replicables**, sin hacer esfuerzo. Bueno, un poco: debemos escribir

```sh
$ pip install -r requirements.txt
```

En efecto, esto es... *as easy as __py__*. :grinning:

## Archivos
Los archivos del repositorio están resumidos en la siguiente tabla.

| Nombre             | ¿Y qué almacena?                                        |
| ------------------ | ------------------------------------------------------- |
| `.gitignore`       | Reglas para que `git` ignore ciertos archivos/carpetas. |
| `requirements.txt` | Librerías utilizadas por `pip`.                         |
| `script.py`        | Toda la magia serpentina para obtener noticias.         |
| `sources.json`     | *Metadata* de las fuentes, en formato JSON.             |

[python]:         http://www.pyzo.org/_images/xkcd_python.png
[beautifulsoup4]: https://pypi.python.org/pypi/beautifulsoup4
[requests]:       https://pypi.python.org/pypi/requests
