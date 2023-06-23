goto main
wb 0

a ww 21
b ww 10
c ww 0
r ww 0

main add x, a
     div x, b
     mov x, r
     zero x, c
     add x, a
     mod x, b
     mov x, c
     halt

