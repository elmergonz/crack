#!/usr/bin/bash

CORE_COUNT=$1
FILE=$2

main() {
    ./bin/rarcrack --type zip --threads $CORE_COUNT $FILE
}

demo() {
    rm ./demo/demo.zip.xml
    ./bin/rarcrack --type zip --threads $CORE_COUNT ./demo/demo.zip
}

if [ '$3' == '-d' ]; then
    demo
else
    main
fi
