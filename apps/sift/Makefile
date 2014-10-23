# @file Makefile
# @brief sift makefile
# @author Jeff Perry <jeffsp@gmail.com>
# @version 1.0
# @date 2014-09-19

run: check

check:
	for i in $$( find ../images/sift/*.jpg ); do  \
		./sift_features.py $$i; \
	done
