"""
Create a two new gate classes, one called NorGate the other called NandGate. 
NandGates work like AndGates that have a Not attached to the output. 
NorGates work lake OrGates that have a Not attached to the output.

Create a series of gates that prove the following equality: 

NOT (( A and B) or (C and D)) == NOT( A and B ) and NOT (C and D)

Make sure to use some of your new gates in the simulation.

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
    
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
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
    
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
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



def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = NorGate("G3")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    print(g3.getOutput())
    
    g4 = NandGate("G4")
    g5 = NandGate("G5")
    g6 = AndGate("G6")
    c1 = Connector(g4, g6)
    c2 = Connector(g5, g6)
    print(g6.getOutput())

main()

