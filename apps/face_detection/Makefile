# @file Makefile
# @brief face_recognition project
# @author Jeff Perry <jeffsp@gmail.com>
# @version 1.0
# @date 2014-05-10

BUILD=debug
INSTALL_DIR=/usr/local/bin

.PHONY: waf run fd check install uninstall

waf: version.h
	waf

version.h: face_detection.cc face_detection.h
	@echo "Creating version.h..."
	@echo "#include <string>" > version.h
	@echo "namespace javelina {" >> version.h
	@echo "namespace face_detection {" >> version.h
	@echo -n "std::string version (\"" >> version.h
	@date +%Y%m%d.%H%M%S | tr -d '\n' >> version.h
	@echo "\");" >> version.h
	@echo "}" >> version.h
	@echo "}" >> version.h

run: check

fd: waf
	for i in $$( find db/*.jpg ); do  \
		./build/$(BUILD)/face_detection $$i; \
	done

check:
	for i in $$( find db/*.jpg ); do  \
		./draw_faces.py $$i tmp.png; \
		display tmp.png; \
		rm tmp.png; \
	done

install: waf
	sudo install -s -v \
		./build/release/face_detection \
		$(INSTALL_DIR)

uninstall:
	sudo rm -f \
		$(INSTALL_DIR)/face_detection
