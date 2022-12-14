# >>> Bounds Prework Assignment <<<

#Question 1:
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. 

def hello_name(username):
    print("hello_" + username.upper())
    

print("\nQ1:")

user = input("\nPlease enter a username:\t")
hello_name(user)


#Question 2: 
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for n in range(100):
        m = n%2
        if m == 1:
            n = str(n)
            print(n, end=" ")
        else:
            continue
    return None

print("\nQ2:")

first_odds()
print(first_odds())


#Question 3: 
#Please write a python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. 

def max_num_in_list(a_list):
    v = a_list[0] 
    for n in a_list:
        if n >= v: 
            v = n 
        else:
            continue 
    print(v)
    return v 

print("\nQ3:")

listo = [1,8,5,2,7,3,65,2,34,9]
max_num_in_list(listo)


#Question 4: 
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 400. 
#The return should be boolean Type (true/falsse)

def is_leap_year(a_year):
    y = a_year 
    if (y % 4) == 0:
        if (y % 400) != 0:
            a = True
        else:
            a = False
    else:
        a = False 
    return a 

print("\nQ4:")

print(is_leap_year(2004))
print(is_leap_year(2005))



#Question 5: 
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers,
#but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    a = True
    v = a_list[1]
    for n in a_list:
        if (n == v) or (n > v) :
            a = False 
            break
        elif n < v: 
            m = n + 1
            if m == v:
                v = v + 1
                a = True 
            else:
                a = False 
                break
    return a 

print("\nQ5:")

listo = [1,2,3,4,5,6,7,8,9]
lista = [1,5,9,7,3,4] 

print(is_consecutive(listo))
print(is_consecutive(lista))
