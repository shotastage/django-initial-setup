up:
	python setup.py sdist bdist_wheel
	twine upload dist/*

build:
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist/
	rm -rf django_initial_setup.egg-info/
	rm -rf build/
