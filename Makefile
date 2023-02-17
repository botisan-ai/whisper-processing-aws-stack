-include .env
export

build-lambdas:
	cd lambdas && ./build_and_push.sh

deploy:
	cd infrastructure && npx aws-cdk@2.65.0 deploy $(stack)