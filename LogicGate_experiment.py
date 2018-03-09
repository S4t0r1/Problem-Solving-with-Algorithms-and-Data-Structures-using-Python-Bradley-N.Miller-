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
    
    def compute_values(self, inputSum=None, inputCin=None):
        a = str(inputSum) if inputSum else str(self.getPinA())
        b = str(inputCin) if inputCin else str(self.getPinB())
        self.summ = 1 if XorGate.performGateLogic(self, pinA=a, pinB=b) else 0
        self.carry = 1 if AndGate.performGateLogic(self, pinA=a, pinB=b) else 0
        return str(self.carry), str(self.summ)
# ..} Excercise 11


def main():
    cout1, summ1 = Halfadder("H1").compute_values()
    cout2, summ2 = Halfadder("H2").compute_values(summ1, cout1)
    cout3 = OrGate("OR1").performGateLogic(pinA=cout1, pinB=cout2)
    print ("cin = {cout1} | cout = {cout3} | sum = {summ2}".format(**locals()))
    

main()
