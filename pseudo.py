ADT Converging_Tree:
    objects: "a nonempty and finite set of connected nodes, where each node has control solution to acquire parent's signal."
    functions:
        "All ct, ct_1, ct_2, ct_3, ..., ct_k belongs to Converging_Tree"
        "value is a boolean value, True or False"
        "Cv_Tree is an abbrebiation of Converging_Tree"
        Cv_Tree Create()        ::= Create an empty Converging_Tree
        Boolean IsEmpty(ct)     ::= if (ct == an empty Converging_Tree):
                                        return True else return False
        Cv_Tree MakeCT(ct_1)    ::= if (control solution of ct_1 exists):
                                        return (a Converging_Tree which has ct_1 as root and
                                            control solutions (ct_2, ct_3, ..., ct_k) are subtrees of ct_1)
                                    else:
                                        return None #ct_1 becomes leaf node
        Cv_Tree Trim_Tree(ct)   ::= if (more than one nodes have same value):
                                        remove all of them escept the first discovered one from ct
                                        return ct
        element Data(ct)        ::= if (IsEmpty(ct)):
                                        return error
                                    else:
                                        return data of ct's root.
        tuple   Subtrees(CT)    ::= if (IsEmpty(ct)):
                                        return none
                                    else:
                                        return (subtrees of ct)

def equation_solver(network):
    for node in network:
        positive_pert_max = 2**size(node.equation.posiive)
        negative_pert_max = 2**size(node.equation.negativ)
        constant = node.equation.constant
        for i in (0 to positive_pert_max):
            for j in (0 to negative_pert_max):
                positive_perturbation = str(bin(i)).strip(binary_identifier)
                negative_perturbation = str(bin(j)).strip(binary_identifier)
                determinant = substitute(node.equation, positive_perturbation,
                                            negative_perturbation, constant)
                solution = concatenate(positive_perturbation, negative_perturbation)
                if determinant > 0:
                    node.solution_1.append(solution)
                else:
                    node.solution_0.append(solution)

def draw_converging_tree(root, converging_tree):
    if not root:
        return
    (nodes, values) = ct_2_nodes(root)    # Extratc network's node information from Converging_Tree
    se_table = Array(size = (len(nodes), max(nodes.solutions(value))))   #make a table to stor solutions of simultaneous equations
    for i, node in enumerate(nodes):
        se_table[i] = node.solutions(value(i))
    solution_list = combination(se_table)
    for sol in solution_list:
        if sol is appropriate node to be updated:
            ct = Converging_Tree(sol)
            root.subtree(ct)    # make ct as a subtee of root
    Converging_tree.Trim_Tree()
    for cts in root.subtrees:
        draw_converging_tree(cts, converging_tree)
