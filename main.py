"""
Robust Optimal control
Equation Solver
Byunghyun Ban
2017.01.24.
"""
import time
import Network as Nt

start = time.time()
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

mdm2 = net.find_node("Mdm2")
chk12 = net.find_node("CHK1/2")

pip3 = net.find_node("PIP3")

nfkb = net.find_node("NFkB")

atmatr = net.find_node("ATM/ATR")
pi3k = net.find_node("PI3K")
p53pten = net.find_node("p53/PTEN")

ras = net.find_node("Ras")

ikk = net.find_node("IKK")
snail = net.find_node("Snail")
ecadh = net.find_node("Ecadh")

rtk = net.find_node("RTK")
nf1 = net.find_node("NF1")

pkc = net.find_node("PKC")
wnt = net.find_node("WNT")
gli = net.find_node("Gli")

tak1 = net.find_node("TAK1")

end = time.time() - start
print (end)