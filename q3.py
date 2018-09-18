#!/usr/bin/env python

#compute edit distance between 2 strings A and B
def edit_distance(word1_real, word2_real):
    m = len(word1_real)+1 #rows
    n = len(word2_real)+1 #columns
    
    d = [[0 for x in range(n)] for x in range(m)]
    
    for i in range(1, m):
        d[i][0] = i
        
    for j in range(1, n):
        d[0][j] = j
    
    delta_a_b = 0
    
    for j in range(1, n):
        
        for i in range(1, m):
            if(word1_real[i-1] == word2_real[j-1]):
                delta_a_b = 0
            else:
                delta_a_b = 1
            d[i][j] = min(d[i-1][j-1] + delta_a_b, d[i-1][j] + 1, d[i][j-1] + 1)

    return d[m-1][n-1]
    
def check_typo(word1, word2):
    typos = edit_distance(word1, word2)
    return (typos == 1) or (typos == 0) 

def main():
    word_input1 = 'ballad'
    word_input2 = 'handball'
    print('Typos check result is ')
    print(check_typo(word_input3, word_input4))


    
    


if __name__ == '__main__':
    main()
