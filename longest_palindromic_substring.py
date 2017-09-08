import random
import time


###########################################
# brute force
# Time complexity : O(n^3)
# Space complexity : O(1)
###########################################
def longest_plaindrom1(myarr):
    maxpal = ""
    maxlen = 0
    for i in range(len(myarr)):
        for j in range(i+1,len(myarr)+1):
            #print(myarr[i:j])
            subarr = myarr[i:j]
            if isPalindrom(subarr) and len(subarr) >= maxlen:
                maxpal = subarr
                maxlen = len(subarr)
    return maxpal

###########################################
# Helper isPalindrom(arr)
# retruns True or Flase
###########################################
def isPalindrom(arr1):
    i = 0
    j = len(arr1) - 1
    while(i < j):
        if arr1[i] != arr1[j]:
            return False
        i += 1
        j -= 1
    return True

##################################################################################################
##################################################################################################

def longest_plaindrom2(myarr):
    pass

##################################################################################################
##################################################################################################
###########################################
# Expand Around Center
# Time complexity : O(n^2)
# Space complexity : O(1)
###########################################
def longest_plaindrom3(myarr):
    start = 0
    end = 0
    for i in range(len(myarr)):
        len1 = expandAroundCenter(myarr, i, i)
        len2 = expandAroundCenter(myarr, i, i + 1)
        maxlen = max(len1, len2)
        if maxlen > end - start:
            start = i - (maxlen - 1) / 2
            end = i + maxlen / 2
    
    return myarr[start: end + 1]

def expandAroundCenter(arr1, left, right):
    L = left
    R = right
    while L >= 0 and R < len(arr1) and arr1[L] == arr1[R]:
        L -= 1
        R += 1
    return R - L - 1
##################################################################################################
##################################################################################################
###########################################
# Manacher's Algorithm
# Time complexity : O(n)
# Space complexity : O(1)
###########################################
def longest_plaindrom4(myarr):
    pass

##################################################################################################
##################################################################################################

########################## Test  ####################################
longarr = []
list_size = 1000
for i in range(0, list_size):
    longarr.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

#print("Mystr: " + "".join(longarr))

print(longest_plaindrom1(longarr))
print(longest_plaindrom3(longarr))


print("Starting longest palindrom 1")
start = time.time()
print("Longest palindrom is: " + str(longest_plaindrom1(longarr)))
end = time.time()
print("Longest palindrom 1 done in: " + str(round(end-start, 3)))

'''
print("Starting longest palindrom 2")
start = time.time()
print("Longest palindrom is: " + longest_plaindrom2(myarr))
end = time.time()
print("Longest palindrom 2 done in: " + str(round(end-start, 3)))
'''
print("Starting longest palindrom 3")
start = time.time()
print("Longest palindrom is: " + str(longest_plaindrom3(longarr)))
end = time.time()
print("Longest palindrom 3 done in: " + str(round(end-start, 3)))
