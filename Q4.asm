goto main
wb 0

a ww 12
b ww 0
c ww 0
d ww 0


main pull x, a
     jz x, final
     dec x
     mov x, a
     mult x, a
     mov x, c
     
     goto main
 