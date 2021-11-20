.PHONY: venv install test-install test clean nopyc

venv:
	@python --version || (echo "Python is not installed, please install Python 2 or Python 3"; exit 1);
	pip install virtualenv
	virtualenv --python=python venv

install: venv
	. venv/bin/activate; pip install .

test-install:
	. venv/bin/activate; pip install -r test/requirements.txt

test:
	. venv/bin/activate; python -m unittest discover -v
	. venv/bin/activate; python test/__init__.py
	. venv/bin/activate; flake8 --statistics --count
	. venv/bin/activate; coverage run test/__init__.py

clean: nopyc
	rm -rf venv

nopyc:
	find . -name \*.pyc -delete
