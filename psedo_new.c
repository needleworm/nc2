ADT Converging_Tree{
    objects   "a nonempty and finite set of connected nodes, where each node has control solution to acquire parent's signal."
    functions{
        // ct, ct_2 elongs to Converging_Tree
        // Cv_Tree is an abbrebiation of Converging_Tree
        Cv_Tree create(root, value)         ::= Create an Converging_Tree with root, value;
        Boolean isEmpty(ct)                 ::= if ct is an empty Converging_Tree
                                                  return true;
                                                else
                                                  return false;
        Cv_Tree makeCT(ct)                  ::= if control solution S of ct exists
                                                  make all S as children of ct;
                                                return ct;
        Cv_Tree cascade(ct, ct_2, SBL)      ::= if ct_2 is a subtree of ct
                                                  make SBL as siblings of ct_2
                                                  remove all subtrees whose level is higher than ct_2.level;
                                                  remove ct_2 from ct;
                                                return ct;
        element data(ct)                    ::= if not ct.IsEmpty()
                                                  return data of ct;
                                                return null;
        Cv_Tree subtrees(ct)                ::= if not ct.IsEmpty()
                                                  return children of ct;
                                                return null;
    }
}


Function convergingTree(phenotype, value){
  // network의 링크 방향은 역전되어 있다.
  queue = [];
  new_ct = new Convergint_Tree();
  queue.enqueue(phenotype and value);
  while queue{
    LOW = MAX_INT;
    temp = null;
    /* Step 1 */
    current = queue.dequeue();
    ct = new Convergint_Tree(current.nodes, current.value);
    /* Setp 1-1-2 */
    if ct contradicts any of ancestors  // Case 2-1
      continue;
    /* Step 1-1-1 */
    for each set S on new_ct
      if S covers ct  // Case 1-2
        continue;
      /* Case 1-1 */
      else if S.level < LOW{
          LOW = s.level;
          temp = S;
      }
    if temp{
      SIBLINGS = [ct];
      while queue.front is sibling of ct{
        sibling = queue.dequeue();
        if sibling covers temp
          SIBLINGS.append(sibling);
      }
      new_ct.cascad(temp, SIBLINGS);
      for each CT of new ct, whose level is LOW
        if CT.lecel == lowset
          queue.enqueue(solution node and value sets of CT);
    }
    /* Step 1-1 */
    else // case 1-3
      queue.enqueue(solution node and value sets of CT);
