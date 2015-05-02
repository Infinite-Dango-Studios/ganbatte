#!/bin/bash
##########
# This file is used by Travis CI in order to install different versions of Ren'Py.
# It is called through the ".travis.yml" file.
#
# This script installs the version of Ren'Py specified by the renpy_version environmental variable.
##########

# Print out the commands that are run to the terminal for logging purposes
set -x

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
