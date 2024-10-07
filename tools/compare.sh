#!/bin/sh
# Compares two given ROM files

hexdump -C "$1" > "$1".txt
hexdump -C "$2" > "$2".txt

diff -u "$1".txt "$2".txt | less
