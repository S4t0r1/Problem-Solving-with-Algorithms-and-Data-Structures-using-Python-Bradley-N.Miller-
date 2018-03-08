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
        a = pinA if pinA is not None else self.getPinA()
        b = pinB if pinB is not None else self.getPinB()
        if a == 1 and b == 1:
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
        a = pinA if pinA is not None else self.getPinA()
        b = pinB if pinB is not None else self.getPinB()
        if a == 1 or b == 1:
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
        a = pinA if pinA is not None else self.getPinA()
        b = pinB if pinB is not None else self.getPinB()
        if a != b:
            return 1
        else:
            return 0
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


class Halfadder(BinaryGate):
    
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        self.summ = 0
        self.carry = 0
    
    def compute_values(self):
        a = self.getPinA()
        b = self.getPinB()
        self.summ = 1 if XorGate.performGateLogic(self, pinA=a, pinB=b) == 1 else 0
        self.carry = 1 if AndGate.performGateLogic(self, pinA=a, pinB=b) == 1 else 0
        return self.carry, self.summ


def main():
    g1 = Halfadder("H1")
    print(g1.compute_values())
    g2 = AndGate("G2")
    print(g2.getOutput())
    g3 = NotGate("G3")
    print(g3.getOutput())

main()
