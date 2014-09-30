#!/bin/bash

# Generate a C++ header file that contains a nested namespace.
#
# The namespace will contain a version string that is based upon the current date and time.
#
# This version typically is regenerated each time a source file is changed and may be used as a simple unique identifier
# for executables.

USAGE="usage: $0 filename.h namespace"

if [ -z "$1" ]; then
    echo $USAGE
    exit
fi

if [ -z "$2" ]; then
    echo $USAGE
    exit
fi

FN=$1
NAMESPACE=$2

echo "Creating $FN"
echo "#include <string>" > $FN
echo "namespace javelina {" >> $FN
echo "namespace $NAMESPACE {" >> $FN
echo -n "std::string version (\"" >> $FN
date +%Y%m%d.%H%M%S | tr -d '\n' >> $FN
echo "\");" >> $FN
echo "}" >> $FN
echo "}" >> $FN
