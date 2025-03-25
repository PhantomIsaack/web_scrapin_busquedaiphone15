# Amazon15 Scraper

Este es un pequeño proyecto en Python que utiliza Selenium para extraer información de Amazon sobre el iPhone 15.

## ¿Qué hace este script?

- Abre Amazon con una búsqueda específica de iPhone 15.
- Extrae el nombre, precio y la fecha de extracción de los productos.
- Muestra los datos de forma clara en la terminal, uno por uno.

---

## Requisitos

Este proyecto necesita Python 3.9 o superior y las siguientes librerías:

- selenium
- webdriver_manager
- pandas
- tabulate

---

## Instrucciones de instalación y uso

Puedes usar este script desde la terminal o desde tu IDE favorito (como VSCode, PyCharm, etc.).

### Opción A: Desde la terminal (recomendado)

1. **Clona este repositorio:**

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

2. **Crea un entorno virtual (opcional pero recomendado):**

```bash
python3 -m venv principal
source principal/bin/activate  # En Linux/Mac
principal\Scripts\activate     # En Windows
```

3. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

4. **Ejecuta el script:**

```bash
python3 amazon15.py
```

---

### Opción B: Usando un IDE

1. Abre el proyecto con tu IDE preferido.
2. Asegúrate de tener un entorno virtual o que las librerías estén instaladas.
3. Instala las dependencias si es necesario desde la terminal del IDE o desde su interfaz.
4. Ejecuta `amazon15.py` desde el botón de "Run".

---

## Notas importantes

- El script abre una ventana del navegador automáticamente usando Chrome, así que asegúrate de tenerlo instalado.
- Si ves errores relacionados con el navegador o el driver, puedes actualizar el `webdriver_manager` con `pip install -U webdriver-manager`.

# web_scrapin_busquedaiphone15
# web_scrapin_busquedaiphone15
