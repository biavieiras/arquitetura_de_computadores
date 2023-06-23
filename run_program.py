import ufc2x as cpu
import sys
import memory as mem
import clock as clk 
import disk

mem.write_word(50,23)
mem.write_word(100,5)

#add o memory_adress[50] ao X
# X <- X+memory_adress[50]
mem.write_byte(1,2)
mem.write_byte(2,50)


#divisão
mem.write_byte(3,29)
mem.write_byte(4,100)
#print(cpu.X)
#print(cpu.Y)
#print(cpu.H)

# salvando o resultado da divisão em 150
mem.write_byte(5,10)
mem.write_byte(6,150)

#salvando em X o valor de memory[50]
mem.write_byte(7,53)
mem.write_byte(8,50)

#fazendo a operação de resto de X com o memory[100]
mem.write_byte(9,49)
mem.write_byte(10,100)

#salvando o resultado do resto em 180
mem.write_byte(11,10)
mem.write_byte(12,180)

mem.write_byte(13,255)

clk.start([cpu])

print("inteiro:",mem.read_word(150))
print("resto:",mem.read_word(180))
