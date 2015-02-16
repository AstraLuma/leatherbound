include local.mk

.PHONY: all
all:
	echo "Try deps or upload"

.PHONY: deps
deps:
	pip install -r requirements.txt -t lib/

.PHONY: upload
upload:
	appcfg.py -A $(APPID) update . 