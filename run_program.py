import ufc2x as cpu
import sys
import memory as mem
import clock as clk 
import disk

mem.write_word(50,2)
mem.write_word(100,10)


mem.write_byte(1,2)
mem.write_byte(2,100)



mem.write_byte(3,29)
mem.write_byte(4,50)
#print(cpu.X)
#print(cpu.Y)
#print(cpu.H)


mem.write_byte(5,10)
mem.write_byte(6,333)

clk.start([cpu])

print(mem.read_word(333))


