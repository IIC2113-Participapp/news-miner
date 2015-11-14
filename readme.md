
# :snake: NewsMiner :snake:

## Descripción
En pocas palabras, este microcomponente realiza una *minería* de noticias a partir diferentes fuentes, para, después, entregarlas a la aplicación principal. Para llevar a cabo su implementación, decidimos seguir el [*__open/closed principle__*](https://en.wikipedia.org/wiki/Open/closed_principle). Nuestra intención es que, al momento de agregar una nueva fuente, el [código](scraper.py) escrito en Python (casi) no sufra modificaciones. Luego, sólo se deberá agregar *metadata* en el [archivo](sources.json) JSON.

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

## Manual de estilo
Aquí no hay sorpresas: intentaremos seguir el [PEP8], amigo lector. No obstante, aun más importante, es que trataremos de incorporar el [PEP20] —también conocido como *The Zen of Python*. En este texto, el séptimo principio sucintamente afirma: *__readability counts__*. No olvidemos que el código será leído muchas más veces que escrito. Por esto, nuestro [benevolente pastor](https://en.wikipedia.org/wiki/Guido_van_Rossum), nos orienta al declarar que...

> *A style guide is about consistency.<br>
Consistency with this style guide is important.<br>
Consistency within a project is more important.<br>
Consistency within one module or function is most important.*

> *But most importantly: know when to be inconsistent -- sometimes the style guide just doesn't apply. When in doubt, use your best judgment. Look at other examples and decide what looks best.*

En otras palabras, estas normas no deben ser aplicadas *ciegamente*. Si bien el PEP8 nos encamina, también tendremos que usar nuestro criterio.

[python]:         http://www.pyzo.org/_images/xkcd_python.png
[beautifulsoup4]: https://pypi.python.org/pypi/beautifulsoup4
[requests]:       https://pypi.python.org/pypi/requests

[pep8]:  https://www.python.org/dev/peps/pep-0008
[pep20]: https://www.python.org/dev/peps/pep-0020
