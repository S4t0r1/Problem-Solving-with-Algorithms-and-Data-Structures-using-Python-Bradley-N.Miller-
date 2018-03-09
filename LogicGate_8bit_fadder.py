"""
Makes a 8-bit-Fulladder, each 1-bit-Fulladder consists of 2 Halfadders...


Enter Pin A (0|1) for H0 -->  0
Enter Pin B (0|1) for H0 -->  0

cin = 0 | cout = 0 | sum = 0

Enter Pin A (0|1) for H1 -->  1
Enter Pin B (0|1) for H1 -->  0

cin = 0 | cout = 0 | sum = 1

Enter Pin A (0|1) for H2 -->  0
Enter Pin B (0|1) for H2 -->  1

cin = 0 | cout = 0 | sum = 1

Enter Pin A (0|1) for H3 -->  1
Enter Pin B (0|1) for H3 -->  1

cin = 0 | cout = 1 | sum = 0

Enter Pin A (0|1) for H4 -->  0
Enter Pin B (0|1) for H4 -->  0

cin = 1 | cout = 0 | sum = 1

Enter Pin A (0|1) for H5 -->  1
Enter Pin B (0|1) for H5 -->  0

cin = 1 | cout = 1 | sum = 0

Enter Pin A (0|1) for H6 -->  0
Enter Pin B (0|1) for H6 -->  1

cin = 1 | cout = 1 | sum = 0

Enter Pin A (0|1) for H7 -->  1
Enter Pin B (0|1) for H7 -->  1

cin = 1 | cout = 1 | sum = 1


...corresponds to the Fulladder Truth Table....

"""



class LogicGate(object):
    
    def __init__(self, n):
        self.name = n
        self.output = None
    
    
    def getName(self):
        return self.name
    
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    
    def __init__(self, n):
        LogicGate.__init__(self,n)
        
        self.pinA = None
        self.pinB = None
    
    
    def getPinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A (0|1) for " + self.getName() + " --> "))
        else:
            return self.pinA.getFrom().getOutput()
    
    
    def getPinB(self):
        if self.pinB is None:
            return int(input("Enter Pin B (0|1) for " + self.getName() + " --> "))
        else:
            return self.pinB.getFrom().getOutput()
    
    
    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("ERROR: All gates full.")


class AndGate(BinaryGate):
    
    def __init__(self, n):
        BinaryGate.__init__(self, n)
    
    
    def performGateLogic(self, pinA=None, pinB=None):
        a = pinA or self.getPinA()
        b = pinB or self.getPinB()
        if int(a) == 1 and int(b) == 1:
            return 1
        else:
            return 0


class NandGate(AndGate):
    
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


class OrGate(BinaryGate):
    
    def __init__(self, n):
        BinaryGate.__init__(self, n)
    
    
    def performGateLogic(self, pinA=None, pinB=None):
        a = pinA or self.getPinA()
        b = pinB or self.getPinB()
        if int(a) == 1 or int(b) == 1:
            return 1
        else:
            return 0


class NorGate(OrGate):
    
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


# Excercise 10 {..
class XorGate(OrGate):
    
    def performGateLogic(self, pinA=None, pinB=None):
        a = pinA or self.getPinA()
        b = pinB or self.getPinB()
        return 1 if (a != b) else 0
# ..} Excercise 10



class UnaryGate(LogicGate):
    
    def __init__(self, n):
        LogicGate.__init__(self, n)
        
        self.pin = None
    
    
    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin (0|1) for " + self.getName() + " --> "))
        else:
            return self.pin.getFrom().getOutput()
    
    
    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("ERROR: All gates full.")


class NotGate(UnaryGate):
    
    def __init__(self, n):
        UnaryGate.__init__(self, n)
    
    
    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector(object):
    
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        
        tgate.setNextPin(self)
    
    
    def getFrom(self):
        return self.fromgate
    
    
    def getTo(self):
        return self.togate


# Excercise 11 {..
class Halfadder(BinaryGate):
    
    def __init__(self, n=""):
        BinaryGate.__init__(self, n)
    
    def compute_values(self, inputA=None, inputB=None):
        a = str(inputA) if inputA else str(self.getPinA())
        b = str(inputB) if inputB else str(self.getPinB())
        self.summ = 1 if XorGate.performGateLogic(self, pinA=a, pinB=b) else 0
        self.carry = 1 if AndGate.performGateLogic(self, pinA=a, pinB=b) else 0
        return str(self.carry), str(self.summ)
# ..} Excercise 11


class Fulladder(Halfadder):
    
    def __init__(self, n):
        Halfadder.__init__(self, n)
    
    def compute_output(self, input_cin=0, count=0):
        cout1, summ1 = Halfadder("H{0}".format(count)).compute_values()
        cout2, summ2 = Halfadder().compute_values(summ1, str(input_cin))
        cout3 = OrGate("OR1").performGateLogic(pinA=cout1, pinB=cout2)
        print ("cin = {input_cin} | cout = {cout3} | sum = {summ2}".format(**locals()))
        return str(cout3), str(summ2)

class N_bit_fulladder(Fulladder):
    
    def __init__(self, n):
        Fulladder.__init__(self, n)
    
    def full_adders(self, n_bit_adder=1):
        cin = 0
        for i in range(n_bit_adder):
            outputs = Fulladder("F").compute_output(cin, i)
            cin = outputs[0] if i < 4 else 1


def main():
    f8 = N_bit_fulladder("N8").full_adders(8)

main()
