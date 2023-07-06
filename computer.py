import ufc2x as cpu
import memory as mem
import clock as clk

import ufc2x as cpu
import sys
import memory as mem
import clock as clk 
import disk

disk.read(str(sys.argv[1]))

print("")

if str(sys.argv[1]) == "csw.out":
  print("Valor de A antes: ", mem.read_word(1))
  print("Valor de B antes: ", mem.read_word(2))
  print("Valor de C antes: ", mem.read_word(3))
  print("")


clk.start([cpu])

if str(sys.argv[1]) == "fatorial.out":
  print("")
  print("Fatorial de ", mem.read_word(1), ":", mem.read_word(4))
  print("")

elif str(sys.argv[1]) == "csw.out":
  print("")
  print("Valor de A: ", mem.read_word(1))
  print("Valor de B: ", mem.read_word(2))
  print("Valor de C: ", mem.read_word(3))
  print("Retorno: ", mem.read_word(4))
  print("")

elif str(sys.argv[1]) == "divmod.out":
  print("")
  print("Divisão inteira de",mem.read_word(1),"por",mem.read_word(2), ":", mem.read_word(3))
  print("Resto: ", mem.read_word(4))
  print("")