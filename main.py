"""
Robust Optimal control
Equation Solver
Byunghyun Ban
2017.01.24.
"""


import Network as Nt

net = Nt.Network("original.txt")

apoptosis = net.find_node("Apoptosis")

caspase8 = net.find_node("Caspase8")
caspase9 = net.find_node("Caspase9")

fadd = net.find_node("FADD")
cytocApaf1 = net.find_node("Cytoc/APAF1")

tnfa = net.find_node("TNFa")

p53 = net.find_node("p53")
bax = net.find_node("BAX")
bak = net.find_node("Bak")
akt = net.find_node("AKT")
bcl2 = net.find_node("Bcl2")
bclxl = net.find_node("BclXL")
