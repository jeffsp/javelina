# @file Makefile
# @brief resize an image
# @author Jeff Perry <jeffsp@gmail.com>
# @version 1.0
# @date 2014-10-09

TMPNAME=tmp.png
check:
	@./resize.sh input.jpg 384 512 $(TMPNAME)
	@identify -format "%w %h" $(TMPNAME) | grep -q "384 512"
	@rm -f $(TMPNAME)
	@echo Success

run: check
