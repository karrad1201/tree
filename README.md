Пример:

```
├── .env
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── README.md
├── logs/
│   ├── app.log
├── src/
│   ├── main.py
│   ├── core/
│   │   ├── app.py
│   │   ├── config.py
│   │   ├── logging_config.py
│   │   ├── di/
│   │   │   ├── repository.py
│   │   │   ├── service.py
│   │   │   ├── __init__.py
│   │   ├── domain/
│   │   │   ├── entity/
│   │   │   │   ├── user.py
│   │   │   ├── repository/
│   │   │   │   ├── interface_user_repository.py
│   │   ├── exceptions/
│   │   │   ├── exceptions.py
│   ├── infrastructure/
│   │   ├── database/
│   │   │   ├── base.py
│   │   │   ├── connection.py
│   │   │   ├── init_db.py
│   │   │   ├── schemas.py
│   │   ├── repository/
│   │   │   ├── user_repository.py
│   ├── logs/
│   │   ├── app.log
│   ├── presentation/
│   │   ├── api/
│   │   │   ├── health.py
│   │   │   ├── __init__.py
│   │   │   ├── user/
│   │   │   │   ├── user_router.py
│   ├── services/
│   │   ├── user_service.py
├── tests/
│   ├── conftest.py
│   ├── integration/
│   │   ├── test_user_api.py
│   │   ├── logs/
│   │   │   ├── app.log
```
