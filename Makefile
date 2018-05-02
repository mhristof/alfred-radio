#
#

alfred-radio.alfredworkflow: info.plist generate.py
	zip -r alfred-radio.alfredworkflow info.plist icon.png generate.py icons/

all:
	@echo "Makefile needs your attention"


# vim:ft=make
#
