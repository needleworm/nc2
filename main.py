"""
Robust Optimal control
Equation Solver
Byunghyun Ban
2017.01.24.
"""


import Network as Nt

net = Nt.Network("original.txt")

apoptosis = net.find_node("Apoptosis")

caspase9 = net.find_node("Caspase9")
caspase8 = net.find_node("Caspase8")
