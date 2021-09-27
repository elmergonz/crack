#!/usr/bin/bash

CORE_COUNT=$1
FILE=$2

./bin/rarcrack --type zip --threads $CORE_COUNT $FILE
hola () {
    while true
    do
        echo hola;
        sleep 1;
    done
}

# hola
