# @file Makefile
# @brief CBIR
# @author Jeff Perry <jeffsp@gmail.com>
# @version 1.0
# @date 2014-05-31

APP_NAME=javelina
DEPLOY_DIR=/var/www/$(APP_NAME)
APP_DIR=$(DEPLOY_DIR)/$(APP_NAME)

default:
	python run.py

run: default

check:
	python test_all.py

deploy_clean:
	rm -irf $(DEPLOY_DIR)/*

deploy:
	grep -i debug *.py
	mkdir -p $(APP_DIR)
	cp -a ./.htaccess $(DEPLOY_DIR)
	cp -a ./config.py $(DEPLOY_DIR)
	cp -a ./v/ $(DEPLOY_DIR)
	cp -a ./$(APP_NAME).wsgi $(DEPLOY_DIR)
	cp -a ./$(APP_NAME)/*.py $(APP_DIR)
	cp -a ./$(APP_NAME)/templates/ $(APP_DIR)
