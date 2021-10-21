from working_storage import WorkingStorage

class Variable:
    def __init__(self, ws: WorkingStorage, type : str = None, position : int = None, 
                length : int = 0, decimals : int = 0, signed : bool = False, occurs : int = 1) -> None:
        self.ws : WorkingStorage = ws
        self.type : str = type
        self.length : int = length
        self.decimals : int = decimals
        self.signed : bool = signed
        self.position : int = position
        self.occurs : int = occurs

    def getValue(self):
        return self.ws.getValue(self.position, self.position + self.length * self.occurs).decode('ascii')

    def setValue(self, value : str):
        return self.ws.setValue(self.position, bytearray(value, 'ascii')[0:self.length * self.occurs])     


wk = WorkingStorage(100)
wk.setValue(0, bytearray(b'\x30\x31'))
wk.copy(0, 10, 2)
wk.print()

intager = Variable(
    ws=wk,
    type='int',
    position=10,
    length=2,
    decimals=0,
    signed=False
)

a_intager = Variable(
    ws=wk,
    type='int',
    position=12,
    length=2,
    decimals=0,
    signed=True
)

intager.setValue("12")
a_intager.setValue("+3")

print(intager.getValue())
print(a_intager.getValue())
