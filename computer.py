import ufc2x as cpu
import memory as mem
import clock as clk

import ufc2x as cpu
import sys
import memory as mem
import clock as clk 
import disk

disk.read('out.bin')

print("Antes da operação: ", mem.read_word(3))
#for i in range(100):
  #print(i,":",mem.read_byte(i))

clk.start([cpu])

print("Depois da operação: ", mem.read_word(3))
#print("resto ", mem.read_word(4))
#print("divisão ", mem.read_word(1))