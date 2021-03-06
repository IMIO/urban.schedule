#!/bin/bash
# i18ndude should be available in current $PATH (eg by running
# ``export PATH=$PATH:$BUILDOUT_DIR/bin`` when i18ndude is located in your buildout's bin directory)
#
# For every language you want to translate into you need a
# locales/[language]/LC_MESSAGES/imio.schedule.po
# (e.g. locales/de/LC_MESSAGES/imio.schedule.po)

domain=imio.schedule

i18ndude rebuild-pot --pot $domain.pot --create $domain ../
i18ndude merge --pot $domain.pot --merge manual_translations.pot

files="imio.schedule collective.eeafaceted.z3ctable"
for file in $files; do
    i18ndude sync --pot $file.pot fr/LC_MESSAGES/$file.po
    msgfmt -o fr/LC_MESSAGES/$file.mo fr/LC_MESSAGES/$file.po
done
