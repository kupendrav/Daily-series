#1
# n = int(input("enter the number of times to print (hello world):- "))
# for i in range(n):
#     print(f"{i} : hello world")

#2
# n = int(input("enter the number: "))
# for i in range(1,n+1):
#     print(i)

#3
# n = int(input("enter the number:"))
# for i in range(n,0,-1):
#     print(i)

#4
# n = int(input("enter the number: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i

# print(sum)


#5
# n = int(input("enter the number: "))
# fact = 1
# for i in range(n,1,-1):
#     fact *= i
# print(fact)

#6
# numbers = list(map(int, input("enter the numbers separated by space: ").split()))
# even_sum = 0
# odd_sum = 0
# for i in numbers:
#     if i % 2 == 0:
#         even_sum += i
#     elif i %2 != 0:
#         odd_sum += i
#     else:
#         print("wrong input")

# print(f"sum of even numbers: {even_sum}")
# print(f"sum of odd numbers:{odd_sum}")


#7
# n = int(input("Enetr the number: "))
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)

#8
# n = int(input("Enetr the number: "))
# sum = 0
# for i in range(1,n+1):
#      if n%i == 0:
#         sum+=i

# print(sum)

#9
# a = int(input("Enter the number: "))
# b = int(input("Enter the exponent: "))
# power = a
# for i in range(b-1):
#     power = power * a

# print(power)

#10
# n = int(input("enter the number: "))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count = count + 1
# if count == 2:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not a prime number")

n = int(input("enter the number: "))

for i in range(2,n):
    if n % i ==0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")