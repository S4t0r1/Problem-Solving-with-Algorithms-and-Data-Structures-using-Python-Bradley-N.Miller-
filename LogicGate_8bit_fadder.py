"""
Makes a 8-bit-Fulladder, it consists of 2x 4-bit-Fulladders and each 1-bit-Fulladder consists of 2 Halfadders...


---> 1st 4-bit Halfadder

Enter Pin A (0|1) for H1 -->  0
Enter Pin B (0|1) for H1 -->  0
Enter Pin B (0|1) for H2 -->  0
cin = 0 | cout = 0 | sum = 0

Enter Pin A (0|1) for H1 -->  1
Enter Pin B (0|1) for H1 -->  0
cin = 0 | cout = 0 | sum = 1

Enter Pin A (0|1) for H1 -->  0
Enter Pin B (0|1) for H1 -->  1
cin = 0 | cout = 0 | sum = 1

Enter Pin A (0|1) for H1 -->  1
Enter Pin B (0|1) for H1 -->  1
cin = 0 | cout = 1 | sum = 0

---> 2nd 4-bit Halfadder

Enter Pin A (0|1) for H1 -->  0
Enter Pin B (0|1) for H1 -->  0
cin = 1 | cout = 0 | sum = 1

Enter Pin A (0|1) for H1 -->  0
Enter Pin B (0|1) for H1 -->  1
cin = 1 | cout = 1 | sum = 0

Enter Pin A (0|1) for H1 -->  1
Enter Pin B (0|1) for H1 -->  0
cin = 1 | cout = 1 | sum = 0

Enter Pin A (0|1) for H1 -->  1
Enter Pin B (0|1) for H1 -->  1
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
    
    def __init__(self, n):
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
    
    def compute_values(self, input_cin=0):
        cout1, summ1 = Halfadder("H1").compute_values()
        cout2, summ2 = Halfadder("H2").compute_values(summ1, input_cin)
        cout3 = OrGate("OR1").performGateLogic(pinA=cout1, pinB=cout2)
        print ("cin = {input_cin} | cout = {cout3} | sum = {summ2}".format(**locals()))
        return str(cout3), str(summ2)

def main():
    f1 = Fulladder("F1").compute_values()
    f2 = Fulladder("F2").compute_values(f1[0])
    f3 = Fulladder("F3").compute_values(f2[0])
    f4 = Fulladder("F4").compute_values(f3[0])
    cin = f4[0]
    f5 = Fulladder("F5").compute_values(cin)
    f6 = Fulladder("F6").compute_values(cin)
    f7 = Fulladder("F7").compute_values(cin)
    f8 = Fulladder("F8").compute_values(cin)

main()