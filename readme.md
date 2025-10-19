# MovieMate Backend

Minimal Django REST backend for MovieMate.

Quick links
- Project entry: [moviemate_backend/manage.py](moviemate_backend/manage.py)  
- Settings: [moviemate_backend/moviemate_backend/settings.py](moviemate_backend/moviemate_backend/settings.py)  
- Root URLs: [moviemate_backend/moviemate_backend/urls.py](moviemate_backend/moviemate_backend/urls.py)  
- Movies app URLs: [moviemate_backend/movies/urls.py](moviemate_backend/movies/urls.py)  
- Model: [`movies.models.Movie`](moviemate_backend/movies/models.py)  
- Serializer: [`movies.serializers.MovieSerializer`](moviemate_backend/movies/serializers.py)  
- Views: [`movies.views.get_movies`](moviemate_backend/movies/views.py), [`movies.views.get_movie`](moviemate_backend/movies/views.py), [`movies.views.add_movie`](moviemate_backend/movies/views.py), [`movies.views.update_movie`](moviemate_backend/movies/views.py), [`movies.views.delete_movie`](moviemate_backend/movies/views.py)

Requirements
- Python 3.11+ recommended
- See or create `requirements.txt` for packages (Django, djangorestframework, etc.)

Local setup
1. Create & activate virtualenv:
   - Unix/macOS: `python -m venv env && source env/bin/activate`
   - Windows (Powershell): `python -m venv env; .\env\Scripts\Activate.ps1`
2. Install dependencies:
   pip install -r requirements.txt
3. Configure environment (optional): copy `.env` or set env vars. See [moviemate_backend/moviemate_backend/settings.py](moviemate_backend/moviemate_backend/settings.py) for used vars (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, etc.).
4. Run migrations and start server:
   python manage.py migrate
   python manage.py runserver

API endpoints
- GET /api/movies/ — list movies (-> [`movies.views.get_movies`](moviemate_backend/movies/views.py))  
- POST /api/movies/add/ — create movie (-> [`movies.views.add_movie`](moviemate_backend/movies/views.py))  
- GET /api/movies/<id>/ — retrieve movie (-> [`movies.views.get_movie`](moviemate_backend/movies/views.py))  
- PUT/PATCH /api/movies/<id>/update/ — update movie (-> [`movies.views.update_movie`](moviemate_backend/movies/views.py))  
- DELETE /api/movies/<id>/delete/ — delete movie (-> [`movies.views.delete_movie`](moviemate_backend/movies/views.py))

Notes
- Movie model fields and defaults: see [`movies.models.Movie`](moviemate_backend/movies/models.py).  
- Media files are stored under `media/` (see `MEDIA_ROOT` in settings). The repo currently ignores `media/` and `db.sqlite3` in `.gitignore`.
- For production use a managed DB (Postgres) and configure `DATABASE_URL` or adjust `DATABASES` in [moviemate_backend/moviemate_backend/settings.py](moviemate_backend/moviemate_backend/settings.py).

Deploying (short)
- Add `requirements.txt`, `Procfile` (e.g. `web: gunicorn moviemate_backend.wsgi:application`), and set env vars on host (SECRET_KEY, DEBUG=False, ALLOWED_HOSTS, DATABASE_URL). Use `python manage.py migrate` and `python manage.py collectstatic --noinput` during deploy.

License
- Add a LICENSE file if you want to publish this repository publicly.