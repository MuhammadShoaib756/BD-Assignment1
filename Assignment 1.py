#Name: Muhammad Shoaib
#Reg: L1f16bscs0162
#Subject: PBD
#Section: C
#Assignment: 1






#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question: 1
import math

def rotation(n):
  rotations = list()
  for i in range( len( str(n) ) ):
    m = int( str(n)[i:] + str(n)[:i] )
    rotations.append(m)
  return rotations

def primeCheck(num):
    # If given number is greater than 1 
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        return True
    else:
        return False


def checkManyPrime(List):
    allDone = False
    length = len(List)
    for x in range(length):
        check = primeCheck(List[x])
        if check == True:
            allDone = True
        else:
            return False
    return True

List = list()

for i in range(0, 10000):
    List.append(i+1)

AllPrimeList = list()
List2Count = 0
for x in range(0, 10000):
    check = primeCheck(List[x])
    if check == True:
        AllPrimeList.append(List[x])


circular_prime = list()
circular_prime_check = int(0)
for x in range(0, 100000):
    rotaion_list = rotation(x)
    check = checkManyPrime(rotaion_list)
    if check == True:
        circular_prime.append(x)
        circular_prime_check += 1

print("there are ",circular_prime_check," circular primes")
print(circular_prime)            


# In[ ]:


def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    
    # Print all prime numbers
    count = int(0)
    List_prime = list()
    for p in range(2, n+1): 
        if prime[p]:
            List_prime.append(p)
    return List_prime
            
def rotation(n):
  rotations = list()
  for i in range( len( str(n) ) ):
    m = int( str(n)[i:] + str(n)[:i] )
    rotations.append(m)
  return rotations

def primeCheck(num):
    # If given number is greater than 1 
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        return True
    else:
        return False
    
def checkManyPrime(List):
    allDone = False
    length = len(List)
    for x in range(length):
        check = primeCheck(List[x])
        if check == True:
            allDone = True
        else:
            return False
    return True    
    

    
    
n = 1000000
print("Following are the prime numbers smaller",) 
print("than or equal to", n)
List_of_prime = SieveOfEratosthenes(n)
print(List_of_prime)

length_Prime = len(List_of_prime)
circular_prime = list()
circular_prime_check = int(0)
for x in range(length_Prime):
    rotaion_list = rotation(List_of_prime[x])
    print(rotaion_list)
    check = checkManyPrime(rotaion_list)
    if check == True:
        circular_prime.append(List_of_prime[x])
        circular_prime_check += 1
        
print("there are ",circular_prime_check," circular primes")
print(circular_prime)

length_of_cir_prime  = len(circular_prime)
print("the lenght is: ",length_of_cir_prime)


# In[ ]:


# Question 2


# In[ ]:


def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

primes = sieve(1000000)


length = 0


largest = 0


lastj = len(primes)

for i in range(len(primes)):
    for j in range(i+length, lastj):
        sol = sum(primes[i:j])
        if sol < 1000000:
            if sol in primes:
                length = j-i
                largest = sol
        else:
            lastj = j+1
            break

print(largest)


# In[4]:


# Question 3


# In[5]:


rm_prime = list()

def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

def leftCheck(num):
    length = len(str(abs(num)))
    length2 = length -1
    power = 10**length2
    flag = True
    num2 = num
    for x in range(length2):
        if num2 in rm_prime:
            flag = True
            print("true")
        else: 
            flag = False
        
        num2 = num2 % power
        power = power / 10
        print(num2, ",", power)
    return flag
    
    

Prime_number = sieve(1000000)

rm_prime = Prime_number[4:]

rm_prime_len = len(rm_prime)

print(leftCheck(23))

# for prime in rm_prime:
#     flag = True
#     leftCheck(prime)
    
    
# leftCheck()
# print(rm_prime)


# In[6]:


# Question 4


# In[11]:


def is_lychrel(n):
 
    for i in range(50):
        number = n + int(str(n)[::-1])
        if str(number) == str(number)[::-1]:
            return False
        n = number
    return True

counter = 0

for i in range(10001):
    if is_lychrel(i):
        counter += 1

print(counter)


# In[12]:


# Question 5


# In[13]:


class CircularQueue(): 
  
    def __init__(self, size): 
        self.size = size 
          
        self.queue = [None for i in range(size)]  
        self.front = self.rear = -1
  
    def enqueue(self, data): 
          
        if ((self.rear + 1) % self.size == self.front):  
            print(" Queue is Full\n") 
              
        elif (self.front == -1):  
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data 
        else: 
              
            self.rear = (self.rear + 1) % self.size  
            self.queue[self.rear] = data 
              
    def dequeue(self): 
        if (self.front == -1): 
            print ("Queue is Empty\n") 
              
        elif (self.front == self.rear):  
            temp=self.queue[self.front] 
            self.front = -1
            self.rear = -1
            return temp 
        else: 
            temp = self.queue[self.front] 
            self.front = (self.front + 1) % self.size 
            return temp 
  
    def display(self): 
      
        if(self.front == -1):  
            print ("Queue is Empty") 
  
        elif (self.rear >= self.front): 
            print("Elements in the circular queue are:",  
                                              end = " ") 
            for i in range(self.front, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print () 
  
        else: 
            print ("Elements in Circular Queue are:",  
                                           end = " ") 
            for i in range(self.front, self.size): 
                print(self.queue[i], end = " ") 
            for i in range(0, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print () 
  
        if ((self.rear + 1) % self.size == self.front): 
            print("Queue is Full") 
  
# Driver Code 
ob = CircularQueue(5) 
ob.enqueue(14) 
ob.enqueue(22) 
ob.enqueue(13) 
ob.enqueue(-6) 
ob.display() 
print ("Deleted value = ", ob.dequeue()) 
print ("Deleted value = ", ob.dequeue()) 
ob.display() 
ob.enqueue(9) 
ob.enqueue(20) 
ob.enqueue(5) 
ob.display() 


# In[14]:


# Question 6


# In[15]:


from queue import Queue 
  
class Stack: 
      
    def __init__(self): 
          
        self.q1 = Queue() 
        self.q2 = Queue()  
              
        self.curr_size = 0
  
    def push(self, x): 
        self.curr_size += 1
  
        self.q2.put(x)  
  
       
        while (not self.q1.empty()): 
            self.q2.put(self.q1.queue[0])  
            self.q1.get() 
  
        self.q = self.q1  
        self.q1 = self.q2  
        self.q2 = self.q 
  
    def pop(self): 
  
        if (self.q1.empty()):  
            return
        self.q1.get()  
        self.curr_size -= 1
  
    def top(self): 
        if (self.q1.empty()): 
            return -1
        return self.q1.queue[0] 
  
    def size(self): 
        return self.curr_size 
  
# Driver Code  
if __name__ == '__main__': 
    s = Stack() 
    s.push(1)  
    s.push(2)  
    s.push(3)  
  
    print("current size: ", s.size()) 
    print(s.top())  
    s.pop()  
    print(s.top())  
    s.pop()  
    print(s.top())  
  
    print("current size: ", s.size()) 


# In[ ]:




