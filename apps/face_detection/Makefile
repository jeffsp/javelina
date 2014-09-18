# @file Makefile
# @brief face_recognition project
# @author Jeff Perry <jeffsp@gmail.com>
# @version 1.0
# @date 2014-05-10

BUILD=debug

.PHONY: waf run fd

waf:
	@echo "#include <string>" > version.h
	@echo "namespace javelina {" >> version.h
	@echo "namespace face_detection {" >> version.h
	@echo -n "std::string version (\"" >> version.h
	@date +%Y%m%d.%H%M%S | tr -d '\n' >> version.h
	@echo "\");" >> version.h
	@echo "}" >> version.h
	@echo "}" >> version.h
	waf

run: fd

fd: waf
	for i in $$( find db/*.jpg ); do  \
	./build/$(BUILD)/face_detection $$i; \
	done

INSTALL_DIR=/usr/local/bin

install: waf
	sudo install -s -v \
		./build/release/face_detection \
		$(INSTALL_DIR)

uninstall:
	sudo rm -f \
		$(INSTALL_DIR)/face_detection
