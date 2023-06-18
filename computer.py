import ufc2x as cpu
import memory as mem
import clock as clk

import ufc2x as cpu
import sys
import memory as mem
import clock as clk 
import disk

disk.read('out.bin')

print("Antes da operação: ", mem.read_word(1))

clk.start([cpu])

print("Depois da operação ", mem.read_word(1))