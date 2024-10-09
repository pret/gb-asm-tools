#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Usage: python3 revpals.py image.png...

List Pokemon and trainer sprites with reversed palettes (darker color first).

Copyright (c) 2024, Rangi42
SPDX-License-Identifier: MIT
"""

import sys

import png

def luminance(c):
	r, g, b = c
	return 0.299 * r**2 + 0.587 * g**2 + 0.114 * b**2

def format_color(c):
	r, g, b = c
	return f'#{r:02X}{g:02X}{b:02X}'

def reversed_colors(filename):
	with open(filename, 'rb') as file:
		reader = png.Reader(file)
		reader.preamble()
		try:
			palette = [c[:3] for c in reader.palette()]
		except:
			return
	if len(palette) != 4 or palette[0] != (255, 255, 255) or palette[3] != (0, 0, 0):
		return
	if luminance(palette[1]) < luminance(palette[2]):
		return (palette[1], palette[2])

def main():
	if len(sys.argv) < 2:
		print(f'Usage: {sys.argv[0]} image.png...', file=sys.stderr)
		sys.exit(1)
	for filename in sys.argv[1:]:
		if (r := reversed_colors(filename)):
			print(f'{filename} indexes {format_color(r[0])} before {format_color(r[1])}', file=sys.stderr)

if __name__ == '__main__':
	main()
