#!/usr/bin/env python3
import sys
import importlib

def main():
    encoder = importlib.import_module(sys.argv[1])
    encoded_text = ''
    for line in sys.stdin.readlines():
        encoded_text += encoder.encode(line)
    print(encoder.emit(encoded_text))

if __name__ == '__main__':
    main()
