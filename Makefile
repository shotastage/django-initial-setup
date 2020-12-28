up:
	python setup.py sdist bdist_wheel
	twine upload dist/*

build:
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist/
	rm -rf django_initial_setup.egg-info/
	rm -rf build/


test:
	rm -rf dist/
	rm -rf django_initial_setup.egg-info/
	rm -rf build/
	python setup.py sdist bdist_wheel
	pipenv uninstall django-initial-setup
	pipenv install -d ./dist/django_initial_setup-0.0.9-py3-none-any.whl
