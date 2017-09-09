import random
import time

steps = 0
##################################################################################################
##################################################################################################
##################################################################################################
# Helper isPalindrom(arr)
# retruns True or Flase
##################################################################################################
def isPalindrom(arr1):
    global steps
    i = 0
    j = len(arr1) - 1
    while(i < j):
        steps += 1
        if arr1[i] != arr1[j]:
            return False
        i += 1
        j -= 1
    return True

##################################################################################################
# brute force
# Time complexity : O(n^3)
# Space complexity : O(1)
##################################################################################################
def longest_plaindrom1(myarr):
    global steps 
    maxpal = ""
    maxlen = 0
    for i in xrange(len(myarr)):
        for j in xrange(i+1,len(myarr)+1):
            #subarr = myarr[i:j]
            steps += 1
            if isPalindrom(myarr[i:j]) and len(myarr[i:j]) > maxlen:
                maxpal = myarr[i:j]
                maxlen = len(myarr[i:j])
    return maxpal

##################################################################################################
##################################################################################################
##################################################################################################
# brute force
# Time complexity : O(n^3)
# Space complexity : O(1)
##################################################################################################
def longest_plaindrom2(myarr):
    global steps
    for i in xrange(len(myarr),0,-1):
        j = 0
        while j + i <= len(myarr):
            steps += 1
            #print myarr[j:j+i]
            if isPalindrom(myarr[j:j+i]):
                return myarr[j:j+i]
            j += 1

'''
def longest_plaindrom2(myarr):
    global steps
    for i in xrange(len(myarr),-1,-1):
        for j in xrange(len(myarr)-i):
            #print myarr[j:j+i]
            steps += 1
            if isPalindrom(myarr[j:j+i]):
                return myarr[j:j+i]
'''
##################################################################################################
##################################################################################################
##################################################################################################
# Expand Around Center
# Time complexity : O(n^2)
# Space complexity : O(1)
##################################################################################################
def longest_plaindrom3(myarr):
    global steps
    start = 0
    end = 0
    for i in xrange(len(myarr)):
        steps += 1
        len1 = expandAroundCenter(myarr, i, i)
        len2 = expandAroundCenter(myarr, i, i + 1)
        maxlen = max(len1, len2)
        if maxlen > end + 1 - start:
            start = i - (maxlen - 1) / 2
            end = i + maxlen / 2
    return myarr[start: end + 1]

def expandAroundCenter(arr1, left, right):
    global steps
    L = left
    R = right
    while L >= 0 and R < len(arr1) and arr1[L] == arr1[R]:
        steps += 1
        L -= 1
        R += 1
    return R - L - 1
##################################################################################################
##################################################################################################
##################################################################################################
# Manacher's Algorithm
# Time complexity : O(n)
# Space complexity : O(n)
##################################################################################################
def longest_plaindrom4(myarr):
    pass

##################################################################################################
##################################################################################################

########################## Test  #################################################################
longarr = []
list_size = 100
for i in range(0, list_size):
    longarr.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

#longarr = ['A','B','A','D','D','F','E','C','E','F']
#print("Mystr: " + "".join(longarr))

#print(longest_plaindrom1(longarr))
#print(longest_plaindrom2(longarr))
#print(longest_plaindrom3(longarr))

steps = 0
print("Starting longest palindrom 1")
start = time.time()
print("Longest palindrom is: " + str(longest_plaindrom1(longarr)))
end = time.time()
print("Longest palindrom 1 done in: " + str(round(end-start, 3)) + " seconds and in " + str(steps) + " stpes.")

steps = 0
print("Starting longest palindrom 2")
start = time.time()
print("Longest palindrom is: " + str(longest_plaindrom2(longarr)))
end = time.time()
print("Longest palindrom 2 done in: " + str(round(end-start, 3)) + " seconds and in " + str(steps) + " stpes.")

steps = 0
print("Starting longest palindrom 3")
start = time.time()
print("Longest palindrom is: " + str(longest_plaindrom3(longarr)))
end = time.time()
print("Longest palindrom 3 done in: " + str(round(end-start, 3)) + " seconds and in " + str(steps) + " stpes.")

