runimg:
		@docker run --rm --name portal -it -p 8080:8080 -v $$(pwd):/app/ --env-file dot-env-template portal
buildimg:
		@docker build -t portal .
