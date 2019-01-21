WORKERS ?= 10

run:
	python3 tlcbatch.py result.md $(WORKERS)

clean:
	for i in `find . -maxdepth 1 -type d | grep Jupiter`; do find $$i -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf; done
