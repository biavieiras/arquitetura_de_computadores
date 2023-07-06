goto main
wb 0


a ww 390
b ww 3
c ww 500
d ww 0
e ww 1


main add x, a
    sub x, c
    jz x, final
    pull x, c
    mov x, a
    pull x, e
    mov x, d
    halt

final pull x, b
    mov x, c
    halt

   