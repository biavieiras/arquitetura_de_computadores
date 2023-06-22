
import memory
from array import array

firmware = array('L', [0]) * 512

# main: PC <- PC + 1; MBR <- read_byte(PC); goto MBR
firmware[0] =   0b000000000_100_00110101_001000_001_001

# HALT
firmware[255] = 0b000000000_000_00000000_000000_000_000

# X = X + memory[address]

## 2: PC <- PC + 1; fetch; goto 3
firmware[2] = 0b000000011_000_00110101_001000_001_001

## 3: MAR <- MBR; read_word(MAR); goto 4
firmware[3] = 0b000000100_000_00010100_100000_010_010

## 4: H <- MDR; goto 5
firmware[4] = 0b000000101_000_00010100_000001_000_000

## 5: X <- H + X; goto 0
firmware[5] = 0b000000000_000_00111100_000100_000_011


# X = X - memory[address]

## 6: PC <- PC + 1; fetch; goto 7
firmware[6] = 0b000000111_000_00110101_001000_001_001

## 7: MAR <- MBR; read; goto 8
firmware[7] = 0b000001000_000_00010100_100000_010_010

## 8: H <- MDR; goto 9
firmware[8] = 0b000001001_000_00010100_000001_000_000

## 9: X <- X - H; goto 0
firmware[9] = 0b000000000_000_00111111_000100_000_011

# memory[address] = X

## 10: PC <- PC + 1; fetch; goto 11
firmware[10] = 0b00001011_000_00110101_001000_001_001

## 11: MAR <- MBR; goto 12
firmware[11] = 0b00001100_000_00010100_100000_000_010

## 12: MDR <- X; write; goto 0
firmware[12] = 0b00000000_000_00010100_010000_100_011

# goto address 

## 13: PC <- PC + 1; fetch; goto 14
firmware[13] = 0b00001110_000_00110101_001000_001_001

## 14: PC <- MBR; fetch; goto MBR
firmware[14] = 0b00000000_100_00010100_001000_001_010

# if X == 0 goto address

## 15: X <- X; if alu = 0 goto 272 else goto 16
firmware[15] = 0b00010000_001_00010100_000100_000_011

## 16: PC <- PC + 1; goto 0
firmware[16] = 0b00000000_000_00110101_001000_000_001

# X <- X * memory[adress]

## 17: PC <- PC + 1; fetch; goto 18
firmware[17] = 0b00010010_000_00110101_001000_001_001
## 18: MAR <- MBR; read; goto 19
firmware[18] = 0b000010011_000_00010100_100000_010_010
## 19: H <- MDR; GOTO 20
firmware[19] = 0b000010100_000_00010100_000001_000_000
## 20: if X - H < 0; GOTO 21 + 256; else GOTO 21
firmware[20] = 0b000010101_01000111111000000000011
### [21] H é menor ou igual
## Y <- H; GOTO 22
firmware[21] = 0b000010110_00000011000000010000000
### [277] H é maior
## Y <- X; GOTO 23
firmware[277] = 0b000010111_00000010100000010000011
## H <- X; GOTO 23
firmware[22] = 0b000010111_00000010100000001000011
### [23] inicia a multiplicação
## X <- 0; GOTO 24
firmware[23] = 0b000011000_00000010000000100000000
## if Y == 0 GOTO 256 + 25; else GOTO 25
firmware[24] = 0b000011001_00100010100000000000100
### [281] y é zero, portanto, vá para a próxima instrução
firmware[281] = 0b000000000_10000110101001000001001
## Y <- Y - 1; GOTO 26
firmware[25] = 0b000011010_00000110110000010000100
## X <- X + H; GOTO 24
firmware[26] = 0b000011000_00000111100000100000011
# H fica o maior
# Y fica o menor

'''
# x <- X // memory[address]

## 27: PC <- PC + 1; fetch; goto 28
firmware[27] = 0b000011100_000_00110101_001000_001_001

## 28: MAR <- MBR; read; goto 29
firmware[28] = 0b000011101_000_00010100_100000_010_010

## 29: H <- MDR; GOTO 30
firmware[29] = 0b000011110_000_00010100_000001_000_000

## 30: Y <- X; GOTO 31
firmware[30] = 0b000011111_000_00010100_000010_000_011

## 31: X <- 0; GOTO 32
firmware[31] = 0b000100000_000_00010000_000100_000_000
## 32: if Y-H == 0 goto 33 +256; else goto 33
firmware[32] = 0b000100001_001_00111111_000000_000_100

## 33: if Y - H < 0 GOTO 34 + 256; else GOTO 34
firmware[33] = 0b000100010_010_00111111_000000_000_100
## Y <- Y - H; if Y - H < 0 GOTO 35 + 256; else GOTO 35
##firmware[33] = 0b000100011_010_00111111_000010_000_100

## 34: Y <- Y - H goto 35
firmware[34] = 0b000100011_000_00111111_000010_000_100

## 289: Y <- Y - H goto 35
firmware[289] = 0b000100011_000_00111111_000010_000_100

## 35: X <- X + 1 goto 32;
firmware[35] = 0b000100000_000_00110101_000100_000_011

## [290] vá para a próxima instrução
firmware[290] = 0b000000000_100_00110101_001000_001_001
#firmware[290] = 0b000000000_100_00110101_001000_001_001
#firmware[283] = 0b000000000_100_00110101_001000_001_001

'''
# X <- X + 1(inc)
firmware[36] = 0b00000000000000110101000100000011

## X <- X - 1; GOTO 0(dec)
firmware[37] = 0b00000000000000110110000100000011





# X <- X // memory[address]
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 30
firmware[29] = 0b000011110_000_00110101_001000_001_001
## MAR <- MBR; read_word; GOTO 31
firmware[30] = 0b000011111_000_00010100_100000_010_010
## H <- MDR; GOTO 32
firmware[31] = 0b000100000_000_00010100_000001_000_000
## Y <- X; GOTO 33
firmware[32] = 0b000100001_000_00010100_000010_000_011
## X <- 0; GOTO 34
firmware[33] = 0b000100010_000_00010000_000100_000_000
## Y <- Y - H; if Y - H < 0 GOTO 35 + 256; else GOTO 35
firmware[34] = 0b000100011_010_00111111_000010_000_100
### [35] Y é maior ou igual a 0
## X <- X + 1; GOTO 34
firmware[35] = 0b000100010_000_00110101_000100_000_011
### [291] Y é menor que 0
firmware[291] = 0b000000000_100_00110101_001000_001_001





'''
#H= X/Y (div)
firmware[27]= 0b000011100_000_00010000_000001_000_000
            #H<-0 
firmware[28]= 0b000011101_001_00010100_000000_000_100 
            #IF Y=0 GOTO 285; ELSE GOTO 29  
firmware[285]=0b011111111_000_00110101_000000_000_100_1000
            #GOTO HALT
firmware[29]= 0b000011110_001_00010100_000000_000_011 
            #IF X=0 GOTO 286; ELSE GOTO 30
firmware[286]=0b000000000_000_00110101_000000_001_001
            #GOTO MAIN
firmware[30]= 0b000011111000000100000000001000000111
            #K<-0
firmware[31]= 0b000100000000001110010000001000000011
            #K<-K+1
firmware[32]= 0b000100001001001111110000000000100011
            #IF Y-K=0 GOTO 289;ELSE GOTO 33
firmware[289]=0b000100010000001101010000000000111111
            #GOTO 34
firmware[33]= 0b000011111001001111110000000000011011
            #IF (X-K)=0 GOTO 289 ;ELSE GOTO 31
firmware[287]=0b000000000000001101010000000001001000
            #GOTO MAIN
firmware[34]= 0b000100011000001111110001000000011010
            #X<-X-Y
firmware[35]= 0b000011101000001110010000010000111000
            #H <- H+1


'''

# X <- X + 1
##

MPC = 0
MIR = 0

MAR = 0
MDR = 0
PC  = 0
MBR = 0
X = 0
Y = 0
H = 0

NGT = 0
Z = 1

BUS_A = 0
BUS_B = 0
BUS_C = 0

def read_regs(reg_num):
    global MDR, PC, MBR, X, Y, H, BUS_A, BUS_B
    
    BUS_A = H
    
    if reg_num == 0:
        BUS_B = MDR
    elif reg_num == 1:
        BUS_B = PC
    elif reg_num == 2:
        BUS_B = MBR
    elif reg_num == 3:
        BUS_B = X
    elif reg_num == 4:
        BUS_B = Y
    else:
        BUS_B = 0
            
def write_regs(reg_bits):

    global MAR, BUS_C, MDR, PC, X, Y, H

    if reg_bits & 0b100000:
        MAR = BUS_C
        
    if reg_bits & 0b010000:
        MDR = BUS_C
        
    if reg_bits & 0b001000:
        PC = BUS_C
        
    if reg_bits & 0b000100:
        X = BUS_C
        
    if reg_bits & 0b000010:
        Y = BUS_C
        
    if reg_bits & 0b000001:
        H = BUS_C
        
            
def alu(control_bits):

    global BUS_A, BUS_B, BUS_C, NGT, Z
    
    a = BUS_A 
    b = BUS_B
    o = 0
    
    shift_bits = control_bits & 0b11000000
    shift_bits = shift_bits >> 6
    
    control_bits = control_bits & 0b00111111
    
    if control_bits == 0b011000: 
        o = a
    elif control_bits == 0b010100:
        o = b
    elif control_bits == 0b011010:
        o = ~a
    elif control_bits == 0b101100:
        o = ~b
    elif control_bits == 0b111100:
        o = a + b    
    elif control_bits == 0b111101:
        o = a + b + 1
    elif control_bits == 0b111001:
        o = a + 1
    elif control_bits == 0b110101:
        o = b + 1
    elif control_bits == 0b111111:
        o = b - a
    elif control_bits == 0b110110:
        o = b - 1
    elif control_bits == 0b111011:
        o = -a
    elif control_bits == 0b001100:
        o = a & b
    elif control_bits == 0b011100:
        o = a | b
    elif control_bits == 0b010000:
        o = 0
    elif control_bits == 0b110001:
        o = 1
    elif control_bits == 0b110010:
        o = -1 
        
    if o == 0:
        Z = 1
    else:
        Z = 0
    
    if o < 0:
      NGT = 1
    else:
      NGT = 0

    if shift_bits == 0b01:
        o = o << 1
    elif shift_bits == 0b10:
        o = o >> 1
    elif shift_bits == 0b11:
        o = o << 8
        
    BUS_C = o
 

def next_instruction(next, jam):

    global MPC, MBR, NGT, Z
    
    if jam == 0:
        MPC = next
        return
        
    if jam & 0b001:                 # JAMZ
        next = next | (Z << 8)
        
    if jam & 0b010:                 # JAMN
        next = next | (NGT << 8)

    if jam & 0b100:                 # JMPC
        next = next | MBR
        
    MPC = next


def memory_io(mem_bits):

    global PC, MBR, MDR, MAR
    
    if mem_bits & 0b001:                # FETCH
       MBR = memory.read_byte(PC)
       
    if mem_bits & 0b010:                # READ
       MDR = memory.read_word(MAR)
       
    if mem_bits & 0b100:                # WRITE
       memory.write_word(MAR, MDR)
       
def step():
   
    global MIR, MPC
    
    MIR = firmware[MPC]
    
    if MIR == 0:
        return False    
    
    read_regs        ( MIR & 0b00000000000000000000000000000111)
    alu              ((MIR & 0b00000000000011111111000000000000) >> 12)
    write_regs       ((MIR & 0b00000000000000000000111111000000) >> 6)
    memory_io        ((MIR & 0b00000000000000000000000000111000) >> 3)
    next_instruction ((MIR & 0b11111111100000000000000000000000) >> 23,
                      (MIR & 0b00000000011100000000000000000000) >> 20)
                      
    return True







