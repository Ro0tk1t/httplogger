all:
	make install

install:
	pip install -e .
	@ make clean

test:
	echo Done

clean:
	@ - rm -rf *.egg-info dist
