"""
Robust Optimal control
node.py
Byunghyun Ban
2017.01.24.
"""


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

