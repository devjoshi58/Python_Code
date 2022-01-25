def minion_2(s):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    i=0

    while i<len(s):

        if s[i] in vowels:
            kevsc+= len(s)-i
        
        else:
            stusc+= len(s)-i
        
        i=i+1


    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")


if __name__ == '__main__':
    minion_2('BANANA')