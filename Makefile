WORKERS ?= 10
TLA_FILES_DIR ?=

run:
	python3 tlcbatch.py result.md $(WORKERS)

clean:
	for i in `find . -maxdepth 1 -type d | grep Jupiter`; do find $$i -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf; done

update:
	@test $(TLA_FILES_DIR) || (echo Error: TLA_FILES_DIR not set && test)
	for i in `find . -maxdepth 1 -type d | grep Jupiter`; do for j in `ls $$i | grep .tla`; do cp -a $(TLA_FILES_DIR)/$$j $${i}/$$j; done; done