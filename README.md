# WattTimeTest
### Docker Instructions

- Your system should have docker and docker-compose for best results
- Download ZIP

```bash
cd /WattTimeTest/WattTime
docker-compose build && docker-compose up -d
```

- Open [http://localhost/](http://localhost/) after docker images are running

### Alternative Start

```bash
cd /WattTimeTest/WattTime
pip install -r requirements.txt
python manage.py runserver
```

- Open http://localhost:8000/
