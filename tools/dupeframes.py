#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Usage: python3 dupeframes.py path/to/gfx/pokemon/

Check for duplicate frames in Pokemon sprites (path/to/gfx/pokemon/*/front.png).
"""

import sys
import glob

import png

def duplicate_frames(filename):
	with open(filename, 'rb') as file:
		width, height, rows = png.Reader(file).asRGBA8()[:3]
		rows = list(rows)
	if height % width:
		print(f'{filename} is not a vertical strip of square frames!', file=sys.stderr)
		return
	num_frames = height // width
	frames = [rows[i*width:(i+1)*width] for i in range(num_frames)]
	yield from ((i, j) for i in range(num_frames) for j in range(i+1, num_frames) if frames[i] == frames[j])

def main():
	if len(sys.argv) != 2:
		print(f'Usage: {sys.argv[0]} path/to/gfx/pokemon/', file=sys.stderr)
		sys.exit(1)
	for filename in sorted(glob.glob(f'{sys.argv[1]}/**/*.png')):
		name = filename.removeprefix(sys.argv[1] + '/')
		for (i, j) in duplicate_frames(filename):
			print(f'{name}: frame {j} is a duplicate of frame {i}', file=sys.stderr)

if __name__ == '__main__':
	main()
