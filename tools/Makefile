.PHONY: all clean

CC := gcc
CFLAGS := -O3 -flto -std=c11 -Wall -Wextra -pedantic

tools := \
	bpp2png

all: $(tools)
	@:

clean:
	$(RM) $(tools)

bpp2png: bpp2png.c lodepng/lodepng.c common.h lodepng/lodepng.h
	$(CC) $(CFLAGS) -o $@ bpp2png.c lodepng/lodepng.c

%: %.c
	$(CC) $(CFLAGS) -o $@ $<
