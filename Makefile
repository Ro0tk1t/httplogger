all:
	make install

install:
	pip install -e .
	@ make clean

test:
	nosetests -c nose.cfg

clean:
	@ - rm -rf *.egg-info dist
