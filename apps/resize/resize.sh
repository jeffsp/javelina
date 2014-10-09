#!/bin/bash

# Resize an image using imagemagick

USAGE="USAGE: resize <input_fn> <W> <H> <output_fn>"

if [ "$1" = "" ]; then
    echo "no input filename given"
    echo $USAGE
    exit -1
fi

if [ "$2" = "" ]; then
    echo "no width given"
    echo $USAGE
    exit -1
fi

if [ "$3" = "" ]; then
    echo "no height given"
    echo $USAGE
    exit -1
fi

if [ "$4" = "" ]; then
    echo "no output filename given"
    echo $USAGE
    exit -1
fi

TMPNAME=$(mktemp)

# resize without changing aspect ratio, fill entire area (^), then crop excess strips from top or bottom
convert $1 -resize $2x$3^ -gravity center -crop $2x$3+0+0 $TMPNAME.$4

# move from temp location to destination
mv $TMPNAME.$4 $4
