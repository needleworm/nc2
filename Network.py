"""
Robust Optimal control
network.py
Byunghyun Ban
2017.01.24.
"""

import Node as nd

class Network():
    nodes = []
    node_names = []
    names = []
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
                node = nd.Node(split[0], equation=split[1])
                self.nodes.append(node)
                self.names.append(node.name)
        self.update()

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

    def _update_name(self):
        self.node_names = []
        for node in self.nodes:
            self.node_names.append(node.name)

    def update(self):
        while self._update():
            self._update_name()






