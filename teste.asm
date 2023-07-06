goto main
wb 0

a ww 5
b ww 3
c ww 1
d ww 

main 
add x, a
sub x, b
mov y,c
jz y, final
mult x, a
div y, d
mod x, c
pull y, a
inc x, c
dec y, b
zero y
goto final
halt
fat x, c