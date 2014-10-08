# @file Makefile
# @brief moments project
# @author Jeff Perry <jeffsp@gmail.com>
# @version 1.0
# @date 2014-09-30

BUILD=debug
INSTALL_DIR=/usr/local/bin

.PHONY: waf run fd check install uninstall

waf: version.h
	waf

version.h: moments.cc moments.h
	../version.sh ./version.h moments

run: check

check: waf
	for i in $$( find ../db/*.jpg ); do  \
		./build/$(BUILD)/moments $$i; \
	done

install: waf
	sudo install -s -v \
		./build/release/moments \
		$(INSTALL_DIR)

uninstall:
	sudo rm -f \
		$(INSTALL_DIR)/moments
