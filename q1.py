#!/usr/bin/env python

#assumes the array already has the appropriate size to enable shifting all 
#elements
def replace_spaces(array_chars, array_size):
    shift_acumulator = 0 #changes for each space found. Add to the position of
    #next spaces found
    spaces_indexes = [0]*array_size
    space_index = 0
    
    
    for i in range(0, array_size):
        if (array_chars[i]==' '):
            spaces_indexes[space_index] = i + shift_acumulator #accounts for the
#shifting related to possible previous space replacement
            shift_acumulator += 2
            space_index += 1
                
    print('printando space indexes list\n')
    print(spaces_indexes)
    
    
    for i in range(0, space_index):
        shift_array(array_chars, spaces_indexes[i], (array_size-1), 2)
        aux = spaces_indexes[i]
        array_chars[aux] = '&'
        array_chars[aux + 1] = '3'
        array_chars[aux + 2] = '2'
        array_size += 2 #accounting for new chars added with the replacement
        
   
        
def shift_array(array_chars, initial_position, final_position, shift_number):

    while(final_position > initial_position):
        array_chars[final_position + shift_number] = array_chars[final_position]
        final_position -= 1




def main():
    char_input = 'user is not allowed'
    char_input_size = len(char_input)
    
    array_input = ['0']*3*char_input_size
    
    for i in range(0,char_input_size):
        array_input[i] = char_input[i]
        
    replace_spaces(array_input, char_input_size)
    print(''.join(array_input))    


    
    


if __name__ == '__main__':
    main()
