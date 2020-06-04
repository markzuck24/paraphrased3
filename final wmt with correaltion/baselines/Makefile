.PHONY: clean all

all: CDER.sys.score PER.sys.score TER.sys.score WER.sys.score sentence-BLEU.seg.score mteval-inter.sys.score

MOSESROOT = /home/adi/Downloads/mosesdecoder

TOKENIZER = $(MOSESROOT)/scripts/tokenizer/tokenizer.perl 

tokenized:
	for sysoutput in data/plain/system-outputs/newstest2014/*/* data/plain/references/*; do \
		basename=$$(basename $$sysoutput); \
		dirname=$$(dirname $$sysoutput); \
		newdir=$$(echo $$dirname | sed "s|^data/plain|tokenized|"); \
		mkdir -p $$newdir; \
		cat $$sysoutput | $(TOKENIZER) | perl -pe '$$_= lc($$_)' > $$newdir/$$basename ; \
	done

%.sys.score: tokenized
	metric=$*; \
	for system in tokenized/system-outputs/newstest2014/*/*; do \
		basename=$$(basename $$system); \
		testset=$$(echo $$basename | cut -d. -f1); \
		systemname=$$(echo $$basename | cut -d. -f2,3); \
		direction=$$(echo $$basename | cut -d. -f4); \
		reference="tokenized/references/newstest2014-ref.$$direction"; \
		score=$$($(MOSESROOT)/mert/evaluator \
									--sctype $$metric \
									--reference $$reference \
									--candidate $$system); \
		echo $$metric $$direction $$testset $$systemname $$score | tr " " "\t"; \
	done > $@


sentence-BLEU.seg.score: tokenized
	for system in tokenized/system-outputs/newstest2014/*/*; do \
		metric=sentBLEU; \
		basename=$$(basename $$system); \
		testset=$$(echo $$basename | cut -d. -f1); \
		systemname=$$(echo $$basename | cut -d. -f2,3); \
		direction=$$(echo $$basename | cut -d. -f4); \
		reference="tokenized/references/newstest2014-ref.$$direction"; \
		i=1; \
		cat $$system | $(MOSESROOT)/mert/sentence-bleu $$reference | while read score; do \
			echo $$metric $$direction $$testset $$systemname $$i $$score | tr " " "\t"; \
			i=$$(($$i+1)); \
		done; \
	done > $@

mteval-inter.sys.score:
	for system in data/plain/system-outputs/newstest2014/*/*; do \
		basename=$$(basename $$system); \
		testset=$$(echo $$basename | cut -d. -f1); \
		systemname=$$(echo $$basename | cut -d. -f2,3); \
		direction=$$(echo $$basename | cut -d. -f4); \
		reference="data/plain/references/newstest2014-ref.$$direction"; \
		cat $$system \
			| ./wrapmteval.pl --international-tokenization --fake-source $$reference \
		   	| grep "for system" \
			> tmp; \
		NIST=$$(cat tmp | sed "s/  */	/g" | cut -f4); \
		BLEU=$$(cat tmp | sed "s/  */	/g" | cut -f8); \
		echo NIST $$direction $$testset $$systemname $$NIST | tr " " "\t"; \
		echo BLEU $$direction $$testset $$systemname $$BLEU | tr " " "\t"; \
		rm tmp; \
	done > $@

clean:
	rm -rf tokenized *.score
