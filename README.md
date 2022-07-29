# fmtFortranCmt.py

Utility to unify the style of comments in the Fortran.

It assumes formating with 4 space indentation.

Use: `fprettify -i 4 -l 80 --strict-indent` before and after to fix edge cases.

Run `sdiff in.f90 out.f90` to see what it does.
