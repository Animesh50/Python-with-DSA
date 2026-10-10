class progammer:
    componey = "MiceoSoft"
    def __init__(self, name, salery, pin):
        self.name = name
        self.salery = salery
        self.pin = pin

p = progammer("Harry", 1200000, 45432)
print(p.name, p.salery, p.pin, p.componey)
r = progammer("Rohan", 1200000, 343233)
print(r.name, r.salery, r.pin, r.componey)