run:
	streamlit run src/options/app.py

test:
	pytest

edge:
	pytest tests/unit tests/integration

unit:
	pytest tests/unit

int:
	pytest tests/integration

e2e:
	pytest tests/e2e