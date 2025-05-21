# Proyecto ETL y Dashboard de Datos de Fútbol

Este repositorio contiene un **pipeline ETL** completo que procesa datos de fútbol de Kaggle, los carga en **MongoDB Atlas** y ofrece un **dashboard interactivo** basado en **Streamlit**. Todo el proyecto está **contenarizado con Docker** para garantizar portabilidad y facilidad de despliegue.

---

## 📂 Estructura del repositorio

```text
proyecto_etl/
├── .gitignore
├── requirements.txt
├── scripts.py                # Script ETL (Extract-Transform-Load)
├── Dockerfile                # Dockerfile para ejecutar ETL
├── Dockerfile.dashboard      # Dockerfile para desplegar el dashboard
├── streamlit_app.py          # Aplicación Streamlit para visualización
└── kaggle_dataset/           # Dataset original en CSV
    ├── coaches.csv
    ├── leagues.csv
    ├── matches.csv
    ├── players.csv
    ├── referees.csv
    ├── scores.csv
    ├── seasons.csv
    ├── stadiums.csv
    ├── standings.csv
    └── teams.csv
```

---

## 🚀 1. Pipeline ETL

### Descripción

* **Extract**: Lectura de archivos CSV desde `kaggle_dataset/`.
* **Transform**: Se añade una columna `processed` a cada registro.
* **Load**: Inserción en colecciones de MongoDB Atlas.

### Comandos

```bash
# Construir la imagen ETL
docker build -t etl_kaggle_image .

# Ejecutar el contenedor ETL (carga los datos en MongoDB Atlas)
docker run --rm etl_kaggle_image
```

---

## 📊 2. Dashboard con Streamlit

Se emplea Streamlit para crear una interfaz web que consulta directamente MongoDB Atlas y muestra tablas y gráficas.

### Imagen de ejemplo del dashboard

![image](https://github.com/user-attachments/assets/e3ec9f79-9482-4871-a85e-e08590e09f2d)


### Comandos

```bash
# Construir la imagen del dashboard
docker build -f Dockerfile.dashboard -t dashboard-app .

# Ejecutar el contenedor y exponer en localhost:8501
docker run -p 8501:8501 dashboard-app
```

Accede luego en el navegador a:

```
http://localhost:8501
```

---

## 🔍 3. Verificación en MongoDB Atlas

Una vez ejecutado el ETL, podrás comprobar las colecciones y registros cargados en tu cluster de MongoDB Atlas.

### Datos cargados en Atlas

![image](https://github.com/user-attachments/assets/42a3385b-ff0a-44a0-82b9-5dd2cad3eab8)


---

## 📖 Tecnologías y Herramientas

* **Python** 3.10
* **Pandas** para manipulación de datos
* **PyMongo** para conexión a MongoDB
* **Streamlit** para visualización interactiva
* **MongoDB Atlas** (servicio en la nube)
* **Docker** para contenerización

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.
© 2025 Proyecto de Ingeniería de Sistemas.

---

*Desarrollado por Andrés (Andresgh12).*
