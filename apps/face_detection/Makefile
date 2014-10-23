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
	../version.sh ./version.h face_detection

run: check

fd: waf
	for i in $$( find ../images/face_detection/*.jpg ); do  \
		./build/$(BUILD)/face_detection $$i; \
	done

check:
	for i in $$( find ../images/face_detection/*.jpg ); do  \
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
