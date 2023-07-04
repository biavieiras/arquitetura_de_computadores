goto main
wb 0

r ww 0
a ww 50
b ww 3
c ww 0


main pull x, a
     div x, b
     mov x, r
     pull y, a
     mod y, b
     mov y, c
     halt
