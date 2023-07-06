goto main
wb 0


a ww 17
b ww 2
r ww 0
c ww 0


main pull x, a
     div x, b
     mov x, r
     pull y, a
     mod y, b
     mov y, c
     halt
