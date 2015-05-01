#!/bin/bash
set -x #echo on

# Install version 6.99.3 of Ren'Py
if [ "$renpy_version" = "6993" ]
then
    cd ..
    wget http://www.renpy.org/dl/6.99.3/renpy-6.99.3-sdk.tar.bz2
    tar xf renpy-6.99.3-sdk.tar.bz2
    rm renpy-6.99.3-sdk.tar.bz2
    mv renpy-6.99.3-sdk renpy
fi

# Install version 6.99.1 of Ren'Py
if [ "$renpy_version" = "6991" ]
then
    cd ..
    wget http://www.renpy.org/dl/6.99.1/renpy-6.99.1-sdk.tar.bz2
    tar xf renpy-6.99.1-sdk.tar.bz2
    rm renpy-6.99.1-sdk.tar.bz2
    mv renpy-6.99.1-sdk renpy
fi

# Install version 6.18.3 of Ren'Py
if [ "$renpy_version" = "6183" ]
then
    cd ..
    wget http://www.renpy.org/dl/6.18.3/renpy-6.18.3-sdk.tar.bz2
    tar xf renpy-6.18.3-sdk.tar.bz2
    rm renpy-6.18.3-sdk.tar.bz2
    mv renpy-6.18.3-sdk renpy
fi
