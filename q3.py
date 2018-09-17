#!/usr/bin/env python

#compute edit distance between 2 strings A and B
def edit_distance2(word1_real, word2_real):
    m = len(word1_real) + 1 #rows
    n = len(word2_real) + 1 #columns
    word1 = ['0']*(m)
    word2 = ['0']*(n)
    
    d = [[0]*(n) for i in range(m)]
    
    for i in range(0, m):
        d[i][0] = i
        
    for j in range(1, n):
        d[0][j] = j
    
    for i in range(1, m):
        word1[i] = word1_real[i-1]
        
    for j in range(1, n):
        word2[j] = word2_real[j-1]
        
    print('word 1 is ' + ''.join(word1))
    print('word 2 is ' + ''.join(word2))
    
    delta_a_b = 0
    
    for j in range(1, n):
        delta_a_b = 0
        for i in range(1, m):
            if(word1[i] != word2[j]):
                delta_a_b = 1
            d[i][j] = min(d[i-1][j-1] + delta_a_b, d[i-1][j] + 1, d[i][j-1] + 1)
 
    print('valor de saida de aux eh ')
    print(d)
    return d[m-1][n-1]
    

def mininum(x, y, z):
    mini = x
    if y < mini:
        mini = y
    if z < mini:
        mini = z
        if y < z:
            mini = y
    return mini

def main():
    word_input1 = 'pa'
    word_input2 = 'pa'
    print('edit distance returns')
    print(edit_distance2(word_input1, word_input2))
      


    
    


if __name__ == '__main__':
    main()
