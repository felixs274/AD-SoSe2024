# In Zusammenarbeit mit Felix Scholzn, Daniel Heisig und Simon Wagner Entstanden

import sys

class Instruction:
    NOP = "NOP"
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    PW3 = "PW3"
    DIV = "DIV"
    INC = "INC"
    LDA = "LDA"
    LDK = "LDK"
    STA = "STA"
    INP = "INP"
    OUT = "OUT"
    CMP = "CMP"
    JEQ = "JEQ"
    JNEQ = "JNEQ"
    HLT = "HLT"


class Memory:
    def __init__(self):
        self._mem = dict()

    def read(self, idx: int) -> int:
        if idx in self._mem:
            return self._mem[idx]
        else:
            return 0

    def write(self, idx: int, data: int):
        self._mem[idx] = data


class RegisterMachine:
    def __init__(self):
        self._programCounter = 0
        self._akkumulator = 0
        self._flags = 0
        self._progMem = Memory()
        self._dataMem = Memory()
    
    def step(self):
        inst = self._progMem.read(self._programCounter)
        addr = self._progMem.read(self._programCounter+1)
        self.exec(inst, addr)
        self._programCounter += 2

    def loadProgramm(self, program):
        for i, b in enumerate(program):
            self._progMem.write(i, b)

    def exec(self, inst, addr):
        match inst:
            case Instruction.NOP:
                pass
            case Instruction.ADD:
                self._akkumulator = self._akkumulator + self._dataMem.read(addr)
            case Instruction.SUB:
                self._akkumulator = self._akkumulator + self._dataMem.read(addr)
            case Instruction.MUL:
                self._akkumulator = self._akkumulator * self._dataMem.read(addr)
            case Instruction.PW3:
                self._akkumulator = self._akkumulator ** 3
            case Instruction.DIV:
                self._akkumulator = self._akkumulator / self._dataMem.read(addr)
            case Instruction.INC:
                self._akkumulator += 1
            case Instruction.LDA:
                self._akkumulator = self._dataMem.read(addr)
            case Instruction.LDK:
                self._akkumulator = addr
            case Instruction.STA:
                self._dataMem.write(addr, self._akkumulator)
            case Instruction.CMP:
                self._flags = self._dataMem.read(addr) - self._akkumulator
            case Instruction.JEQ:
                if self._flags == 0:
                    self._programCounter = addr-2
            case Instruction.JNEQ:
                if self._flags != 0:
                    self._programCounter = addr-2
            case Instruction.INP:
                inp = input("enter number:")
                inp = int(inp)
                self._akkumulator = inp
            case Instruction.OUT:
                print(f"out: {addr}: ", self._dataMem.read(addr))
            case Instruction.HLT:
                exit()

    def printState(self):
        print(f"PC: {self._programCounter} | Akku: {self._akkumulator} | Flag | {self._flags}")
        print(f"inst: {self._progMem.read(self._programCounter)} {self._progMem.read(self._programCounter+1)}")
        print(f"data mem: {' '.join([str(self._dataMem.read(k)) for k in sorted(list(self._dataMem._mem.keys()))])}")

class Parser:
    def parse(self, filepath):
        file = open(filepath, "r").read()

        labels = dict()
        instNr = 0
        programMemory = []
        for line in file.split("\n"):
            oline = line
            if "#" in line:
                line = line.split("#", 1)[0]
            
            if line.strip() == "":
                continue

            line = line.split(" ", 1)

            singleInstructions = [
                Instruction.NOP,
                Instruction.PW3,
                Instruction.INC,
                Instruction.INP,
                Instruction.HLT               
            ]

            instWithNumber = [
                Instruction.ADD,
                Instruction.SUB,
                Instruction.MUL,
                Instruction.DIV,
                Instruction.LDA,
                Instruction.LDK,
                Instruction.STA,
                Instruction.OUT,
                Instruction.CMP
            ]

            instJump = [
                Instruction.JEQ,
                Instruction.JNEQ
            ]

            inst = line[0]
            match inst:
                case inst if inst in singleInstructions:
                    programMemory.extend([inst, 0])
                case inst if inst in instWithNumber:
                    num = int(line[1])
                    programMemory.extend([inst, num])
                case inst if inst in instJump:
                    label = line[1].strip(": ")
                    if label not in labels:
                        raise NameError(f"unknown label {label} not in {labels}")
                    
                    jmpAddr = labels[label]*2
                    programMemory.extend([inst, jmpAddr])
                case "label":
                    label = line[1].strip(":")
                    labels[label] = instNr
                case _:
                    raise NameError(f"unknown inst {inst}, line: in {oline}")
            
            instNr += 1
        
        return programMemory



def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} filepath")
    
    filepath = sys.argv[1]
    r = RegisterMachine()
    p = Parser().parse(filepath)

    r.loadProgramm(p)
    while True:
        r.step()

main()