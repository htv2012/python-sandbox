from battleship_game import ShipBoard

s = ShipBoard()
s.add("A1", "A2", "A3", "A4", "A5")
s.add("B3", "C3", "D3")
s.add("G0", "H0")
s.add("E6", "E7", "E8")
s.add("F4", "G4", "H4", "I4")

print(s)
for co in "D1 D2 A6 A9 G0 H0 E9 E8 G0".split():
    print(f"{co} --> {s.assess(co)}")
print(s)
