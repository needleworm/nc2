"""
Robust Optimal control
node.py
Byunghyun Ban
2017.01.24.
"""

import numpy as np


class Node:
    name = ""
    value = -1
    equation = {}
    solution_1 = []
    solution_0 = []
    pos_weight = []
    neg_weight = []

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

        self._solve_equation()

    def __str__(self):
        return self.name

    def is_constant(self):
        if self.value in (1, 0):
            return True
        positive_count = 0
        negative_count = 0
        constant = self.equation["constant"]

        for pos in self.equation['positive']:
            multiply = 1
            if '*' in pos:
                multiply, pos = pos.split('*')
            positive_count += multiply
        for neg in self.equation['negative']:
            multiply = 1
            if '*' in neg:
                multiply, neg = neg.split('*')
            negative_count += multiply

        if constant == 0:
            if positive_count == 0:
                self.value = 0
                return True
        elif constant > 0:
            if constant > negative_count:
                self.value = 1
                return True
        elif constant < 0:
            if constant + positive_count <= 0:
                self.value = 0
                return True
        return False

    def _update_weight(self):
        pos_weight = np.ones(len(self.equation["positive"]), dtype="short")
        neg_weight = np.ones(len(self.equation["negative"]), dtype="short")
        for i in range(len(self.equation["positive"])):
            if '*' in self.equation["positive"][i]:
                pos_weight[i] *= int(self.equation["positive"][i].split('*')[0])
        for i in range(len(self.equation["negative"])):
            if '*' in self.equation["negative"][i]:
                neg_weight[i] *= int(self.equation["negative"][i].split('*')[0])
        self.pos_weight = pos_weight
        self.neg_weight = neg_weight

    def _num_2_pert(self, num, size):
        if size == 0:
            return []
        binary = str(bin(num))[2:]
        pert = np.zeros(size, dtype="short")
        for i in range(len(binary)):
            pert[-i - 1] = int(binary[-i - 1])
        return pert

    def _solve_equation(self):
        self._update_weight()
        self.solution_0 = []
        self.solution_1 = []
        pos_pert_max = 2 ** len(self.pos_weight)
        neg_pert_max = 2 ** len(self.neg_weight)
        if pos_pert_max > 0 and neg_pert_max > 0:
            for i in range(pos_pert_max):
                for j in range(neg_pert_max):
                    pos_perturbation = self._num_2_pert(i, len(self.pos_weight))
                    neg_perturbation = self._num_2_pert(j, len(self.neg_weight))
                    pos_sum = np.sum(self.pos_weight * pos_perturbation)
                    neg_sum = np.sum(self.neg_weight * neg_perturbation)
                    determinant = pos_sum - neg_sum + self.equation["constant"]
                    solution = np.hstack((pos_perturbation, neg_perturbation))
                    if determinant > 0:
                        self.solution_1.append(solution)
                    else:
                        self.solution_0.append(solution)
        elif pos_pert_max == 0 and neg_pert_max > 0:
            for j in range(neg_pert_max):
                neg_perturbation = self._num_2_pert(j, len(self.neg_weight))
                neg_sum = np.sum(self.neg_weight * neg_perturbation)
                determinant = 0 - neg_sum + self.equation["constant"]
                if determinant > 0:
                    self.solution_1.append(neg_perturbation)
                else:
                    self.solution_0.append(neg_perturbation)
        elif pos_pert_max > 0 and neg_pert_max == 0:
            for j in range(pos_pert_max):
                pos_perturbation = self._num_2_pert(j, len(self.pos_weight))
                pos_sum = np.sum(self.pos_weight * pos_perturbation)
                determinant = pos_sum + self.equation["constant"]
                if determinant > 0:
                    self.solution_1.append(pos_perturbation)
                else:
                    self.solution_0.append(pos_perturbation)

        self.solution_1 = np.array(self.solution_1, dtype="short")
        self.solution_0 = np.array(self.solution_0, dtype="short")

    def solutions(self, value):
        if value == 1:
            pert_array = self.solution_1
        else:
            pert_array = self.solution_0
        for array in pert_array:
            self._array_printer(array)

    def _array_printer(self, pert_array):
        node_array = np.hstack((self.equation["positive"], self.equation["negative"]))
        print(end="{(")
        if len(node_array) == 1:
            print (node_array[0], end=") = (")
        else:
            for i in range(len(node_array) - 1):
                print(node_array[i], end=", ")
            print(node_array[-1], end=") = (")
        if len(pert_array) == 1:
            print(pert_array[0], end=")}\n")
        else:
            for i in range(len(pert_array) - 1):
                print(pert_array[i], end=", ")
            print(pert_array[-1], end=")}\n")






