#PYTHON TASK
# ANSWER 1
#Find even numbers from given list
l = [10,501,22,37,100,999,87,351]
#set of even number
a = [i for i in l if i%2==0]
#set of odd number
b = [i for i in l if i %2!=0]
print(f"Even Numbers:{a}")
print(f"Odd number:{b}")

#Answer 2
# Find prime numbers for [10,501,22,37,100,999,87,351]
prime_list_number = []
not_prime_list_number = []
def prime_checker(mylist):
    for i in range(0, len(mylist)):
        a = mylist[i]
        is_prime = True
        for j in range(2,a):
            if a%j ==0:
                is_prime = False
        if is_prime:
            prime_list_number.append(a)
        else:
            not_prime_list_number.append(a)

prime_checker([10,501,22,37,100,999,87,351])
print(f"prime_list_number:{prime_list_number}")
#print(f"Number of prime numbers:{prime_list_number.count}")
print(f"not_prime_list_number:{not_prime_list_number}")

# Answer 3 
#Happy numbers are tose number whose digits when split and squared sum to 1, like 19=> 1*1+9*9= 82 
#82=> 8*8+2*2 = 68 => 6*6+8*8 = 100 
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

# List of numbers to check
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Checking which numbers are happy using map and split
happy_numbers = list(map(lambda x: str(x) if is_happy(x) else '', numbers))
happy_numbers = list(filter(None, happy_numbers))  # Remove empty strings

print("Happy numbers:", " ".join(happy_numbers))


#Answer 4
#sum of first snd last digit in a number
def sum_digit_last(n):
    n_str = str(abs(n))  # Consider only positive number, as integer is not iterable, convert it to string
    first_digit = int(n_str[0])
    last_digit = int(n_str[-1])
    return first_digit + last_digit

# For Example
num = 2574
print("Sum of first and last digit:", sum_digit_last(num))

#Answer 5
#Possible combinations of coins to make Rs. 10
def find_comb():
    solutions = [] #collect solutions in form of list
    
    # Loop through possible counts of ₹10 coins
    for ten in range(2):  # Max 1 Rs.10 coin (since 1 * 10 = 10)
        for five in range(3):  # Max 2 Rs. 5 coins (since 2 * 5 = 10)
            for two in range(6):  # Max 5 Rs. 2 coins (since 5 * 2 = 10)
                for one in range(11):  # Max 10 Re 1 coins (since 10 * 1 = 10)
                    if (ten * 10 + five * 5 + two * 2 + one * 1) == 10: #possible coins for 10
                        solutions.append((ten, five, two, one)) #adding on different solutions for Rs. 10
    
    return solutions

# Get all valid combinations
combinations = find_comb()

# Display the results
print("Ways to make Rs.10 coins:")
for i, (ten, five, two, one) in enumerate(combinations, 1): #(ten, five, two, one) gives solutions and enumerate will help in indexing while looping through solutions
    print(f"{i}. 10 coins: {ten}, 5 coins: {five}, 2 coins: {two}, 1 coins: {one}")


#Answer 6
#Find duplicates in three lists
l = [23, 34, 45, 46, 56, 67]
l1 = [34, 45, 67, 87, 89]
l2 = [45, 46, 67, 78, 89, 934]

# Find common elements in all three lists
duplicates = set(l) & set(l1) & set(l2)

print("Duplicates in all three lists:", list(duplicates))

#Answer 7
#python program to find first non-repeating elements in a given list of integers
numbers = [10, 501, 22, 37, 10, 999, 87, 351, 22, 10]
for a in numbers:
    if numbers.count(a) == 1:
        print(a)
        break
    else:
        None

#Answer 8
def min_and_sort(list):
    min_value = min(list)  # Find the minimum value
    sorted_list = sorted(list)  # Sort the list in ascending order
    return min_value, sorted_list

# Example list
ratings = [4, 302, 590, 28, 490, 349]

# Get the minimum rating and sorted list
min_rating, sorted_ratings = min_and_sort(ratings)

print("Minimum rated value:", min_rating)
print("Sorted list:", sorted_ratings)


#Answer 9
#Find a triplet in the list [10,20,30,9] to make a target value of 59.
def triplets(list, target):
    triplets = []
    n = len(list)
    # Sort the list
    list.sort()
    #for triplets we require three numbers, so we use n-2
    for i in range(n - 2): #range is n-2, because we are fixing i, and using two pointers from left and right
        left, right = i + 1, n - 1  # Two pointers
        while left < right:
            total = list[i] + list[left] + list[right]
            if total == target:
                triplets.append((list[i], list[left], list[right]))
                left += 1
                right -= 1  # Move pointers inward
            elif total < target:
                left += 1
            else:
                right -= 1
                
    return triplets

# Example list and target sum
numbers = [10,20,30,9]
target_sum = 59

# Find triplets
triplets = triplets(numbers, target_sum)
print("Triplets with sum 10:", triplets)


#Answer 10 
# from a list [4,2,-3,1,6] , find when the sublist componenets sum will be equal to zero
l =  [4,2,-3,1,6]
sl =[]
l.sort
num = len(l)
for i in range(num):  # Outer loop: start index of sublist
    sum_ = 0  # Reset sum for new sublist
    for j in range(i, num):  # Inner loop: end index of sublist
        sum_ += l[j]  # Add current element to sum
        if sum_ == 0:  # Check if sum is zero
            sl.append(l[i:j+1])  # Store the sublist

print(sl)




