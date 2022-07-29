#!/usr/bin/python3
import sys
import re

def formatcmt(line):
    """It assumes formating with 4 space indentation.
    Use: `fprettify -i 4 -l 80 --strict-indent`
    before and after to fix edge cases."""
    cmt_reg = re.compile(r"""!.*""")
    blcmt = re.compile(r"""(^|\s{4}|\s{8}|\s{12}|\s{16})!\ .*""")

    cmtln = cmt_reg.search(line)
    if not cmtln:
        return line
    bl = blcmt.search(line)
    if bl:  # fine indentation and spacing
        return line
    line = re.sub(r"\s{0,3}!\s{0,3}", "  ! ", line)
    return line


def main():
    usage = f"No or bad file specified: \nTry: {sys.argv[0]} infile.f90 > outfile.f90\n"

    if len(sys.argv) < 2:
        sys.stderr.write(usage)
        exit(1)
    try:
        with open(sys.argv[1], "r") as f:
            for i in f.readlines():
                sys.stdout.write(formatcmt(i))
    except:
        sys.stdout.write(usage)
        exit(1)


if __name__ == "__main__":
    main()
