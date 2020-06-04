SHELL=/bin/bash

HUMAN_JUDGMENTS = judgements-2014-05-14.csv
HUMAN_SCORES = human-2014-05-16.scores
HUMAN_FOLDED = human-2014-05-16.folded

TO_EN   = fr-en de-en hi-en cs-en ru-en
FROM_EN = en-fr en-de en-hi en-cs en-ru

# Should we compute system level confidences?
COMPUTE_CONFIDENCE = false

# Number of bootstrapped samples for segment level confidence estimation (0 for no confidence estimation)
SEGMENT_BOOTSTRAP_SAMPLES = 0

# The format of the output tables (plain,simple,grid,pipe,orgtbl,rst,mediawiki,latex)
TABLE_FORMAT = plain

.PHONY: all clean realclean baselines

all: system.correlations.toEn system.correlations.fromEn segment.correlations.toEn segment.correlations.fromEn

system.correlations.%: $(HUMAN_SCORES) $(HUMAN_FOLDED) baselines submissions
	[ "$*" = "toEn" ] && DIRS="$(TO_EN)"; \
	[ "$*" = "fromEn" ] && DIRS="$(FROM_EN)"; \
	$(COMPUTE_CONFIDENCE) && FOLDED_RESULTS="$(HUMAN_FOLDED)/*.human.scores"; \
	./compute-system-correlations \
		--metrics submissions/*/*.sys.score \
				  baselines/*.sys.score \
		--human $(HUMAN_SCORES) \
		--directions $$DIRS \
		--tablefmt $(TABLE_FORMAT) \
		--samples $$FOLDED_RESULTS \
		> $@

segment.correlations.%: $(HUMAN_JUDGMENTS) baselines submissions
	[ "$*" = "toEn" ] && DIRS="$(TO_EN)"; \
	[ "$*" = "fromEn" ] && DIRS="$(FROM_EN)"; \
	./compute-segment-correlations \
		--judgments $< \
		--metrics submissions/*/*.seg.score \
				  baselines/*.seg.score \
		--directions $$DIRS \
		--variant wmt14 \
		--bootstrap $(SEGMENT_BOOTSTRAP_SAMPLES) \
		--rseed 1234 \
		--tablefmt $(TABLE_FORMAT) \
		> $@

baselines:
	$(MAKE) -C $@

clean:
	rm -rf *.toEn *fromEn

realclean: clean
	$(MAKE) -C baselines clean
