#!/bin/sh
SED_ARG="-e 's/SOMETHING//g'"

echo SOMETHINGhei | eval sed "$SED_ARG"
