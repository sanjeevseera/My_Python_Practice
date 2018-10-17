"""
Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""

def newlist(lists,n):
    ls=[]
    for i in range(1,n+1):
        for l in lists:
            ls.append(l+str(i))
    return ls

lists=['p', 'q']
n=5
print(newlist(lists,n))


#my_list = ['p', 'q']
#n = 4
#new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
#print(new_list)
