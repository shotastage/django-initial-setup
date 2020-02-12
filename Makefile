build:
	python setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	rm -rf dist/
	rm -rf django_initial_setup.egg-info/
	rm -rf build/
