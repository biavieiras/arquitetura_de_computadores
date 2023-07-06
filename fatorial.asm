goto main
wb 0

a ww 5
b ww 0
c ww 1
d ww 0


main pull x, a
     pull y, a

fatorial sub x, c
     jz x, final
     mov x, b
     mult y, b
     goto fatorial

final mov y, d
     halt
