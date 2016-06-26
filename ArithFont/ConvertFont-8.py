#!/usr/bin/env python3

import sys


def main():
    sys.stdout.write(
'''/* This file is generated automatically by ConvertFont-8.py, do not edit it. */
const unsigned char font[96][8] = {
''')
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.split()
        if line[0] == 'ENCODING':
            charenc = int(line[1])  # Assume stored in order
        elif line[0] == 'BBX':
            sizex, sizey, offx, offy = map(int, line[1:5])
        elif line[0] == 'BITMAP':
            bitmap = [0]*(7-sizey-offy)
            while True:
                line = sys.stdin.readline().strip()
                if line == 'ENDCHAR':
                    bitmap.extend([0]*(8-len(bitmap)) )
                    output_char(bitmap, charenc, sys.stdout)
                    break
                else:
                    bitmap.append(int(line, 16)>>(offx+2))
    sys.stdout.write('};\n')


def output_char(bitmap, charenc, f):
    hexarray = ', '.join(map(lambda x: '0x%02x' % x, bitmap))
    f.write('    {%s}, /* %r, %d */\n' % (hexarray, chr(charenc), charenc-32))

if __name__ == '__main__':
    main()
