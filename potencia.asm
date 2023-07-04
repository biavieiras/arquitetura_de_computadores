goto main
wb 0

a ww 3
b ww 3
c ww 0

main pull x, a
    pull y, b
    jz y, final
    jz x, zerou
    dec y, c
    mov x, c

multiplica mult x, c
    dec y, c
    jz y, encerra
    goto multiplica
    
final inc y, c
    mov y, c
    halt

zerou halt

encerra mov x, c
    halt



