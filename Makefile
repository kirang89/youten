.PHONY: docs test

help:
	@echo "  env         create a development environment using virtualenv"
	@echo "  shell       launch customised shell prompt with necessary imports"
	@echo "  initdb      create the necessary tables for the app"
	@echo "  dropdb      delete all necessary tables for the app"
	@echo "  deps        install dependencies using pip"
	@echo "  clean       remove unwanted files like .pyc's"
	@echo "  test        run tests"
	@echo "  testc       run tests with coverage"

env:
	sudo easy_install pip && \
	pip install virtualenv && \
	virtualenv env && \
	. env/bin/activate && \
	make deps

shell:
	./shell.py

initdb:
	python create_db.py

dropdb:
	python drop_db.py

deps:
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;

test:
	env/bin/nosetests tests

testc:
	env/bin/nosetests tests --with-coverage --cover-package=api