# [2020-03-09] Challenge #383 [Easy] Necklace matching
#Challenge
#Imagine a necklace with lettered beads that can slide along the string. Here's an example image. In this example, you could take the N off NICOLE and slide it around to the other end to make ICOLEN. 
#Do it again to get COLENI, and so on. For the purpose of today's challenge, we'll say that the strings "nicole", "icolen", and "coleni" describe the same necklace.
#Generally, two strings describe the same necklace if you can remove some number of letters from the beginning of one, attach them to the end in their original ordering, and get the other string. 
#Reordering the letters in some other way does not, in general, produce a string that describes the same necklace.
#Write a function that returns whether two strings describe the same necklace.
#Optional Bonus 1
#If you have a string of N letters and you move each letter one at a time from the start to the end, you'll eventually get back to the string you started with, after N steps. 
# Sometimes, you'll see the same string you started with before N steps. For instance, if you start with "abcabcabc", you'll see the same string ("abcabcabc") 3 times over the course of moving a letter 9 times.
#Write a function that returns the number of times you encounter the same starting string if you move each letter in the string from the start to the end, one at a time.

#Completed by Dillon D'Ornellas

def same_letters(name1, name2):
    #check length of string
    if len(name1) != len(name2):
        return False
    #Rearrange the second name into the first for compare
    name1l = list(name1)
    name2l = list(name2)
    temp = []
    for x in name1l:
        i=0
        for y in enumerate(name2l):
            if y[1] == x:
                i+=1
                #print(y[0])
                let = y[1]
                name2l.pop(y[0])
                temp.append(let)
        if i == 0:
            return False
    if name1l == temp:
        return True
    else:
        return False

def same_necklace(str1, str2):
    #check for equal length
    if len(str1) != len(str2):
        return False
    #check for starting character
    if len(str1) != 0:
        start = str1[0]
    #Check for two empty strings condition
    elif len(str1) == 0 and len(str2) == 0:
        return True
    #search through str2
    for x in enumerate(str2):
        temp = []
        #find starting value from list1, cut at starting point and compare
        if x[1] == start:
            temp = str2[x[0]:] + str2[:x[0]]
            if temp == str1:
                return True
    return False

def repeats(str1):
    i=0
    n = len(str1)
    if n==0:
        i+=1
        return i
    new_list = list(str1)
    for x in range(n):
        new_list.insert(0, new_list.pop())
        if new_list == list(str1):
            i+=1
    return i

print(repeats("abc"))
print(repeats("abcabcabc"))
print(repeats("abcabcabcx"))
print(repeats("aaaaaa"))
print(repeats("a"))
print(repeats(""))
print(same_necklace("nicole", "lenico"))
print(same_necklace("nicole", "coneli"))
print(same_necklace("aabaaaaabaab", "aabaabaabaaa"))
print(same_necklace("abc", "cba"))
print(same_necklace("xxyyy", "xxxyy"))
print(same_necklace("xyxxz", "xxyxz"))
print(same_necklace("x", "x"))
print(same_necklace("x", "xx"))
print(same_necklace("x", ""))
print(same_necklace("", ""))
