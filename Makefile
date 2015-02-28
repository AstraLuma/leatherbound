include local.mk

.PHONY: dev
dev:
	dev_appserver.py .

.PHONY: deps
deps:
	pip install -r requirements.txt -t lib/

.PHONY: upload
upload:
	appcfg.py -A $(APPID) update . 
