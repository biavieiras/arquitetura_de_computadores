
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

# if X == 0 goto address( if==0)

## 15: X <- X; if alu = 0 goto 272 else goto 16
firmware[15] = 0b00010000_001_00010100_000100_000_011

## 16: PC <- PC + 1; goto 0
firmware[16] = 0b00000000_000_00110101_001000_000_001

# X <- X * memory[adress](add)

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



# X <- X // memory[address](div)
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


# X <- X!(fat)
## if X == 0 goto 38+256; goto 38
firmware[37] = 0b000100110_001_00010100_000100000011
#X<-X+1;goto 0
firmware[294] = 0b000000000_000_00110101_000100_000_011
##1 MDR <- X; GOTO 39
firmware[38] = 0b000100111_000_00010100_010000_000_011
##2: MDR <- MDR-1 goto 40
firmware[39] = 0b000101000_000_00110110_010000_000_000
##3 if MDR == 0; GOTO 41 + 256; else GOTO 41
firmware[40] = 0b000101001_001_00010100_000000_000_000
##4 Y <- MDR goto 42
firmware[41] = 0b000101010_000_00010100_000010_000_000
##5 H<- x goto 43
firmware[42] = 0b000101011_000_00010100_000001_000_011
##6 X<- 0 goto 44
firmware[43] = 0b000101100_000_00010000_000100_000_000
##7 if Y == 0 goto 45 + 256 ; else goto 45
firmware[44] = 0b000101101_001_00010100_000000_000_100
##8 X <- X+H goto 46;
firmware[45] = 0b000101110_000_00111100_000100_000_011
##9 Y <- Y-1 goto 44;
firmware[46] = 0b000101100_000_00110110_000010_000_100
##10 MDR <- MDR-1 GOTO 40
firmware[301] = 0b000101000_000_00110110_010000_000_000
############## [297] VAI PARA A PRÓXIMA INSTRUÇÃO
firmware[297] = 0b00000000_010_00011010_100100_000_1001


# X <- X + 1(inc)
firmware[47] = 0b00000000000000110101000100000011

# X <- X - 1; GOTO 0(dec)
firmware[48] = 0b00000000000000110110000100000011

# X <- X % memory[address](mod)
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 50
firmware[49] = 0b000110010_00000110101001000001001
## MAR <- MBR; read_word; GOTO 51
firmware[50] = 0b000110011_00000010100100000010010
## H <- MDR; GOTO 52
firmware[51] = 0b000110100_00000010100000001000000
## X <- X - H; if X - H < 0 GOTO 52 + 256; else 52
firmware[52] = 0b000110100_01000111111000100000011
### [295] X é menor que 0
## X <- X + H; GOTO 0
firmware[308] = 0b00000000_000000111100000100000011

# X <- memory[address](Pull)
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 54
firmware[53] = 0b000110110_000_00110101_001000_001_001
## MAR <- MBR; read_word; GOTO 55
firmware[54] = 0b000110111_00000010100100000010010
## X <- MDR; GOTO 0
firmware[55] = 0b000000000_000_00010100_000100_000_000

# X <- 0
firmware[56] = 0b00000000000000010000000100000000

# Y = Y + memory[address]

## 2: PC <- PC + 1; fetch; goto 58
firmware[57] = 0b000111010_000_00110101_001000_001_001

## 3: MAR <- MBR; read_word(MAR); goto 59
firmware[58] = 0b000111011_000_00010100_100000_010_010

## 4: H <- MDR; goto 60
firmware[59] = 0b000111100_000_00010100_000001_000_000

## 5: Y <- H + Y; goto 0
firmware[60] = 0b000000000_000_00111100_000100_000_100


# Y <- Y * memory[adress](add)
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
firmware[23] = 0b000011000_000_00010000_000100_000000
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

### [23] inicia a multiplicação
## H <- Y GOTO 62
firmware[61] = 0b000111110_000_00010100_000001_000_100
## Y <- 0; GOTO 63
firmware[62] = 0b000111111_000_00010000_000010_000_000
## MDR <- MDR - 1; GOTO 64
firmware[63] = 0b001000000_000_00110110_010000_000_100
## Y <- Y + H; GOTO 65
firmware[64] = 0b001000001_000_00111100_000010_000_100
## if MDR == 0 GOTO 256 + 62; else GOTO 62
firmware[65] = 0b000111110_001_00010100_000000_000_000
##FINALIZA
firmware[318] = 0b000000000_100_00110101_001000_001_001
# H fica o maior
# Y fica o menor


# memory[address] = Y

## 10: PC <- PC + 1; fetch; goto 11
firmware[66] = 0b001000011_000_00110101_001000_001_001

## 11: MAR <- MBR; goto 12
firmware[67] = 0b001000100_000_00010100_100000_000_010

## 12: MDR <- Y; write; goto 0
firmware[68] = 0b00000000_000_00010100_010000_100_100





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







