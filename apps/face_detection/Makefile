# @file Makefile
# @brief face_recognition project
# @author Jeff Perry <jeffsp@gmail.com>
# @version 1.0
# @date 2014-05-10

BUILD=debug

.PHONY: waf run face_detection

waf:
	waf

run: fd

fd: waf
	for i in $$( find db/*.jpg ); do  \
	./build/$(BUILD)/face_detection $$i; \
	done
