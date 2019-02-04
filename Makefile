WORKERS ?= 10
TLA_FILES_DIR ?=
PATTERN_TO_REPLACE ?=

PROTOCOL_DIR := protocols
TLA_DIR := tla
PDF_DIR := pdf

run:
	cd $(PROTOCOL_DIR) && python3 ../jupiter-all-batch.py ../result.md $(WORKERS)

run-refinement:
	cd $(PROTOCOL_DIR) && python3 ../jupiter-refinement-batch.py ../mc_result_dir $(WORKERS)

run-refinement-minimal:
	cd $(PROTOCOL_DIR) && python3 ../jupiter-refinement-batch-minimal.py ../mc_result_minimal_dir $(WORKERS)

clean:
	cd $(PROTOCOL_DIR) && for i in `find . -maxdepth 1 -type d | grep Jupiter`; do find $$i -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf; done

update:
	@test $(TLA_FILES_DIR) || (echo Error: TLA_FILES_DIR not set && false)
	cd $(TLA_DIR) && for j in *.tla; do cp -a $(TLA_FILES_DIR)/$$j .; done
	-cd $(PROTOCOL_DIR) && for i in `find . -maxdepth 1 -type d | grep Jupiter`; do for j in `ls $$i | grep .tla`; do ln -s ../../$(TLA_DIR)/$${j} $${i}/ 2>/dev/null; done; done

anonymous:
	@test $(PATTERN_TO_REPLACE) || (echo Error: PATTERN_TO_REPLACE not set && false)
	find . -type f -name \*.tla -o -name \*.py | xargs sed -i 's/$(PATTERN_TO_REPLACE)/anonymous/g'

gen-pdf:
	mkdir -p $(PDF_DIR)
	cp -f $(TLA_DIR)/* $(PDF_DIR)
	cd $(PDF_DIR) && for j in `ls *tla`; do java -cp ../tla2tools.jar tla2tex.TLA -ps -psCommand dvipdf -shade $$j; done && ls | grep -v '.pdf' | xargs rm
	-cd $(PROTOCOL_DIR) && for i in `find . -maxdepth 1 -type d | grep Jupiter`; do for j in `ls $$i | grep .tla`; do ln -s ../../$(PDF_DIR)/$${j%tla}pdf $${i}/ 2>/dev/null; done; done
