import ufc2x as cpu
import sys
import memory as mem
import clock as clk 
import disk

mem.write_word(50,1)


#add o memory_adress[50] ao X
# X <- X+memory_adress[50]
mem.write_byte(1,2)
mem.write_byte(2,50)


#fatorial de X
mem.write_byte(3,37)
#mem.write_byte(4,50)
#print(cpu.X)
#print(cpu.Y)
#print(cpu.H)


mem.write_byte(4,10)
mem.write_byte(5,150)

mem.write_byte(6,255)

clk.start([cpu])

print(mem.read_word(150))
