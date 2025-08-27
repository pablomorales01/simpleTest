
# Simple CI App (Flask + Selenium + Docker)

Entrega lista para:
- App web mínima (Flask)
- Tests unitarios (pytest)
- Tests Selenium (Chrome en contenedor)
- Dockerfile + docker-compose
- Pipeline de CI (GitHub Actions) que genera **PDF** con el log
- Jenkinsfile opcional con los mismos pasos

## Estructura
```
.
├─ app.py
├─ app_lib.py
├─ templates/index.html
├─ requirements.txt
├─ tests/
│  ├─ unit/test_app.py
│  └─ selenium/test_ui.py
├─ Dockerfile
├─ Dockerfile.tests
├─ docker-compose.yml
├─ tools/make_pdf.py
├─ .github/workflows/ci.yml
└─ Jenkinsfile
```

## Cómo correr localmente (sin CI)
1) Requisitos: Docker y Docker Compose.
2) Construir y levantar pruebas Selenium:
```bash
docker compose build
docker compose up --abort-on-container-exit --exit-code-from tests
```
- Esto levanta:
  - `web` (Flask en Gunicorn) en http://localhost:8000
  - `selenium` (Chrome headless)
  - `tests` (pytest) que ejecuta los tests Selenium contra la app

3) Tests unitarios locales:
```bash
pip install -r requirements.txt
pytest -q tests/unit
```

4) Después de `docker compose up...`, verás un screenshot en `./artifacts/homepage.png`.

## GitHub Actions (recomendado)
- Suba este repo a GitHub con rama `main` (o ajuste el YAML).
- El workflow:
  - construye imágenes
  - ejecuta `docker compose up` para correr los tests Selenium
  - ejecuta tests unitarios
  - **genera un PDF** (`pipeline_log.pdf`) desde el log consolidado (`pipeline.log`)
  - sube artifacts: `pipeline.log`, `pipeline_log.pdf`, `artifacts/homepage.png`

En la pestaña "Actions" de GitHub, descargue los artifacts para su entrega.

## Jenkins (alternativa)
- Requiere Docker disponible en el agente.
- Cree un Pipeline y apunte al `Jenkinsfile` (o copie el contenido).
- El stage **PDF log** archiva `pipeline_log.pdf` y el screenshot.

## ¿Dónde está el Docker?
- `Dockerfile` empaqueta la app con Gunicorn.
- `docker-compose.yml` orquesta `web`, `selenium`, `tests`.
- El despliegue ocurre dentro del contenedor `web`; los tests validan la UI.

## Personalización rápida
- Cambie UI/HTML en `templates/index.html`.
- Agregue más rutas/funciones a `app.py`/`app_lib.py`.
- Agregue más pruebas en `tests/*`.
- Ajuste el flujo en `.github/workflows/ci.yml` o `Jenkinsfile`.

## Entrega
- **PDF requerido**: `pipeline_log.pdf` generado por el pipeline (Actions o Jenkins).
- **Evidencia visual**: `artifacts/homepage.png` (capturado por Selenium).

¡Éxitos! :)
