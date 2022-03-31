run-streamlit:
	streamlit run streamlit_app.py

run-fastapi:
	uvicorn main:app --reload

run-database:
	mongod --dbpath db

