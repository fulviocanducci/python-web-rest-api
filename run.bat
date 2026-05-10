@echo off
call venv\Scripts\activate
pip freeze > requirements.txt
uvicorn main:app --reload --port 8001
pause