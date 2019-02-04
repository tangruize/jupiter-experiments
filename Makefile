WORKERS ?= 10
TLA_FILES_DIR ?=
PATTERN_TO_REPLACE ?=

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
	@test $(PATTERN_TO_REPLACE) || (echo Error: PATTERN_TO_REPLACE not set && false)
	find . -type f -name \*.tla -o -name \*.py | xargs sed -i 's/$(PATTERN_TO_REPLACE)/anonymous/g'

gen-pdf:
	mkdir -p pdf
	find . -type f -name \*.tla -not -path './pdf/*' -not -name MC.tla -exec cp -f {} pdf \;
	cd pdf && for j in `ls *tla`; do java -cp ../tla2tools.jar tla2tex.TLA -ps -psCommand dvipdf -shade $$j; done && ls | grep -v '.pdf' | xargs rm
	for i in `find . -maxdepth 1 -type d | grep Jupiter`; do for j in `ls $$i | grep .tla`; do ln -sf ../pdf/$${j%tla}pdf $${i}/; done; done

#gen-pdf:
#	for i in `find . -maxdepth 1 -type d | grep Jupiter`; do cd $$i; for j in `ls | grep .tla`; do java -cp ../tla2tools.jar tla2tex.TLA -ps -psCommand dvipdf -shade $$j; ls $${j%tla}* | grep -v '.tla\|.pdf' | xargs rm; done; cd -; done