# This is just my personal scripts for development

build:
	docker build -t docker-selenium-lambda .
bash:
	@make build
	docker run --rm -it --entrypoint '' docker-selenium-lambda bash
local:
	@make build
	docker run --rm -it --entrypoint '' docker-selenium-lambda python debug.py
deploy:
	@make local
	sls deploy --region ap-northeast-1
	sls invoke -f server --region ap-northeast-1 --path args.json
test:
	@make local
	sls invoke -f server --region ap-northeast-1 --path args.json
