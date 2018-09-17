#!/usr/bin/env python

#Rule assumed: for more than 3 letters - first letter kept in place and up to
#2/3 letters with places changed; for less than 3 letters - first letter kept
#additional assumption - both words have the same length and letters

def check_partial_permutation(word1, word2):
    bool_return = False
    if (len(word1) > 3):
        if (word1[0] == word2[0]):
            letters_change = number_letters_changed(word1, word2)
            if(letters_change < (len(word1)/3.0)):
                bool_return = True
    else:
        if (word1[0] == word2[0]):
            bool_return = True
    
    return bool_return
    
#This function makes use of the additional assumption
def number_letters_changed(word1, word2):
    letters_changed = 0
    if(len(word1)==len(word2)):
        for i in range (0, len(word1)):
            if (word1[i] != word2[i]):
                letters_changed += 1
    return  letters_changed

def main():
    word_input1 = 'probably'
    word_input2 = 'porbalby'
    print('check permutations return ')
    print(check_partial_permutation(word_input1, word_input2))
      


    
    


if __name__ == '__main__':
    main()
