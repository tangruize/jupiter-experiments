WORKERS ?= 10
TLA_FILES_DIR ?=
PATTERN_TO_DEL ?= ______dummy_pattern______

run:
	python3 jupiter-all-batch.py result.md $(WORKERS)

run-refinement:
	python3 jupiter-refinement-batch.py mc_result_dir $(WORKERS)

run-refinement-minimal:
	python3 jupiter-refinement-batch-minimal.py mc_result_minimal_dir $(WORKERS)

clean:
	for i in `find . -maxdepth 1 -type d | grep Jupiter`; do find $$i -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf; done

update:
	@test $(TLA_FILES_DIR) || (echo Error: TLA_FILES_DIR not set && false)
	for i in `find . -maxdepth 1 -type d | grep Jupiter`; do for j in `ls $$i | grep .tla`; do cp -a $(TLA_FILES_DIR)/$$j $${i}/$$j; done; done

anonymous:
	find . -type f -name \*.tla -o -name \*.py | xargs sed -i -e '/\* Modification History/,+2d' -e '/$(PATTERN_TO_DEL)/d'