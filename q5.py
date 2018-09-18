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
    
    def remove_duplicate(self, size, duplicates_verif):
        if size > 1:
            duplicates_verif.add(self.get_head_value())
            self.remove_duplicate_aux(self.get_head(), self.get_next_node(), duplicates_verif)
    
    
    def remove_duplicate_aux(self, previous_node, curr_node, duplicates_veri):
        if curr_node is not None:
            if curr_node.val in duplicates_veri:
                previous_node.next = curr_node.next
                self.remove_duplicate_aux(previous_node, previous_node.next, duplicates_veri)
            else:
                duplicates_veri.add(curr_node.val)
                self.remove_duplicate_aux(curr_node, curr_node.next, duplicates_veri)
    

def main():
    list_numbers = [0, 1, 0, 6, 0, 0, 6, 0, 0, 0, 2, 0, 0, 0, 0]
    
    test_list = lk_list()
    
    for elmnt in list_numbers:
        test_list.add_node(elmnt)
    
    print('list with possible duplicates')
    test_list.print_list(test_list.get_head())
    
    print('\nhead value is ')
    print(test_list.get_head_value())
    
    duplicates = set()
    test_list.remove_duplicate(len(list_numbers), duplicates)
    print('list with duplicates removed')
    test_list.print_list(test_list.get_head())
    
    


if __name__ == '__main__':
    main()
