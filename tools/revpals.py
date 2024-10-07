#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Usage: python3 revpals.py path/to/gfx/

List Pokemon and trainer sprites with reversed palettes (darker color first).
"""

import sys
import glob

import png

def luminance(c):
	r, g, b = c
	return 0.299 * r**2 + 0.587 * g**2 + 0.114 * b**2

def is_reversed(filename):
	with open(filename, 'rb') as file:
		reader = png.Reader(file)
		reader.preamble()
		try:
			palette = [c[:3] for c in reader.palette()]
		except:
			return False
	if len(palette) != 4 or palette[0] != (255, 255, 255) or palette[3] != (0, 0, 0):
		return False
	return luminance(palette[1]) < luminance(palette[2])

def main():
	if len(sys.argv) != 2:
		print(f'Usage: {sys.argv[0]} path/to/gfx/', file=sys.stderr)
		sys.exit(1)
	for filename in sorted(glob.glob(f'{sys.argv[1]}/**/*.png', recursive=True)):
		name = filename.removeprefix(sys.argv[1]).removeprefix('/')
		if is_reversed(filename):
			print(name, file=sys.stderr)

if __name__ == '__main__':
	main()
