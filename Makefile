NAME := ufc-stats-crawler
TAG := $(shell git log -1 --pretty=%h)
NAMESPACE := tedostrem/ufc-stats-crawler
DATA_DIR := ${PWD}/data

.PHONY : build push

all : build push

build :
	docker build -t ${NAMESPACE}/${NAME}:${TAG} -t ${NAMESPACE}/${NAME}:latest .

bash :
	docker run -it -v /app/data/:${DATA_DIR} ${NAMESPACE}/${NAME}:${TAG} bash

ufcFights :
	docker run -it -v /app/data/:${DATA_DIR} ${NAMESPACE}/${NAME}:${TAG} scrapy crawl -L DEBUG -o - -t json ufcFights

ufcFighters :
	docker run -it -v /app/data/:${DATA_DIR} ${NAMESPACE}/${NAME}:${TAG} scrapy crawl -L DEBUG -o - -t json ufcFighters

upcoming :
	docker run -it -v /app/data/:${DATA_DIR} ${NAMESPACE}/${NAME}:${TAG} scrapy crawl -L DEBUG -o - -t json upcoming

push :
	docker push ${NAMESPACE}/${NAME}
