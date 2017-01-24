"""
Robust Optimal control
network.py
Byunghyun Ban
2017.01.24.
"""


class Network():
    nodes = []
    constants = {}

    def __init__(self, network_file, header=True):
        file = open(network_file)
        if header:
            file.readline()
        for line in file:
            split = line.strip().split('\t')
            if split[1].strip() in '1 0':
                self.constants[split[0]] = int(split[1])
            else:
                node = Node(split[0], equation=split[1])
                self.nodes.append(node)
        while self._update():
            pass

    def _update(self):
        change = False
        for node in self.nodes:
            poscopy = node.equation["positive"]
            node.equation["positive"] = []
            for pos in poscopy:
                mult = 1
                if '*' in pos:
                    mult, pos = pos.split('*')
                    mult = int(mult)
                if pos in self.constants:
                    node.equation["constant"] += self.constants[pos] * mult
                    change = True
                else:
                    node.equation["positive"].append(pos)

            negcopy = node.equation["negative"]
            node.equation["negative"] = []
            for neg in negcopy:
                mult = 1
                if '*' in neg:
                    mult, neg = neg.split('*')
                    mult = int(mult)
                if neg in self.constants:
                    node.equation["constant"] -= self.constants[neg] * mult
                    change = True
                else:
                    node.equation["negative"].append(neg)

            if node.is_constant():
                self.constants[node.name] = node.value
                self.nodes.remove(node)
                return True
        return change

    def find_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return -1


class Node():
    name = ""
    value = -1
    equation = {}

    def __init__(self, name, equation="", val=-1):
        self.name = name
        if val in (1, 0):
            self.value = val
        else:
            self.equation = {"positive": [],
                             "negative": [],
                             "constant": 0}
            split = equation.split(')')
            if len(split) == 2:
                self.equation["constant"] += int(split[1])
                eq = split[0][1:]
            else:
                eq = split[0]
            temp = ""
            for i in range(len(eq)):
                if eq[i] == '-':
                    temp += '+'
                else:
                    temp += eq[i]
            split = temp.split('+')
            for node in split:
                if node == '':
                    continue
                idx = eq.index(node)
                if idx == 0:
                    self.equation["positive"].append(node)
                else:
                    if eq[idx-1] == '-':
                        self.equation["negative"].append(node)
                    elif eq[idx-1] == '+':
                        self.equation["positive"].append(node)

    def __str__(self):
        return self.name

    def is_constant(self):
        if self.value in (1, 0):
            return True
        poscount = 0
        negcount = 0
        constant = self.equation["constant"]


        for pos in self.equation['positive']:
            mult = 1
            if '*' in pos:
                mult, pos = pos.split('*')
            poscount += mult
        for neg in self.equation['negative']:
            mult = 1
            if '*' in neg:
                mult, neg = neg.split('*')
            negcount += mult


        if constant == 0:
            if poscount == 0:
                self.value = 0
                return True
        elif constant > 0:
            if constant > negcount:
                self.value = 1
                return True
        elif constant < 0:
            if constant + poscount <= 0:
                self.value = 0
                return True
        return False








