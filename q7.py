#!/usr/bin/env python

class node:
    def __init__(self):
        self.val = None
        self.next = None

class lk_list:
    def __init__(self):
        self.curr_node = None
    
    def add_node(self, value):
        n_node = node()
        n_node.val = value
        n_node.next = self.curr_node
        self.curr_node = n_node
    
    def get_head(self):
        return self.curr_node
    
    def get_head_value(self):
        return self.curr_node.val
    
    def get_next_node(self):
        return self.curr_node.next
        
    def is_empty(self):
        return self.curr_node == None
        
    def print_list(self, list_node):
        if list_node is not None:
            print(str(list_node.val)+' -'),
            self.print_list(list_node.next)
            
    def join_list(self, list_tail):
        node_aux = self.get_head()
        
        while node_aux.next is not None:
            node_aux = node_aux.next
        
        node_aux.next = list_tail.get_head()

#returns node common to both lists 
def node_intersect(listA, listB):
    node_return = None
    found = 0
    
    node_aux_A = listA.get_head()
    
    while ((node_aux_A is not None) and not(found)):
        node_aux_B = listB.get_head()
        while ((node_aux_B is not None) and not(found)):
            if node_aux_B == node_aux_A:
                node_return = node_aux_B
                found = 1
            node_aux_B = node_aux_B.next
        node_aux_A =  node_aux_A.next
        
    return node_return

def main():
    list_A = [0, 2, 4, 5]
    list_B = [0, 2, 3]
    list_C = [44, 3, 4, 5, 6]
    
    test_listA = lk_list()
    test_listB = lk_list()
    test_listC = lk_list()
    
    for elmnt in list_A:
        test_listA.add_node(elmnt)

    for elmnt in list_B:
        test_listB.add_node(elmnt)

    for elmnt in list_C:
        test_listC.add_node(elmnt)
    
    test_listA.join_list(test_listC)
    print('ListA joined')
    test_listA.print_list(test_listA.get_head())
    
    test_listB.join_list(test_listC)
    print('\n\nListB joined')
    test_listB.print_list(test_listB.get_head())
    
    
    print('\n\nTest if returned node intersection is the same as head(listC): '),
    print(node_intersect(test_listA, test_listB)==test_listC.get_head())
    
    
    
    


if __name__ == '__main__':
    main()
