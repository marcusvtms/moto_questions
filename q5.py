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
    
    def get_curr_node(self):
        return self.curr_node
    
    def get_curr_value(self):
        return self.curr_node.val
    
    def get_next_node(self):
        return self.curr_node.next
        
    def is_empty(self):
        return self.curr_node == None
        
    def print_list(self):
        node_print = self.curr_node
        while(not (node_print == None)):
            print(node_print.val)
            node_print = self.get_next_node() 
    
    
    

def main():
    test_list = lk_list()
    test_list.add_node(10)
    test_list.add_node(19)
    
    #test_list.print_list()
      


    
    


if __name__ == '__main__':
    main()
