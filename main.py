# TASK 1
# registration/referal_ID  =  DIRSS3130
# Name = GOPALAKANNAN
# collage = "PAAVAI ENGINEERING COLLAGE"
#"REGEX DATA SCIENCE PATH TASK SUBMISSION"

print("TASK 1")
ID = "DIRSS3130"
Name = "GOPALAKANNAN"
collage = "PAAVAI ENGINEERING COLLAGE"

print("registration/referal_ID" +"    "+   ID)
print()
print("  Name  :" +"   "+Name)
print()
print(f"collage name :   {collage}")
print()
print("REGEX DATA SCIENCE PATH TASK SUBMISSION")




#class python_task1():
    #Q1: Inverted Pyramid pattern with the same digit
    #Q2: inverted half pyramid pattern with number
    #Q3: Alternate numbers pattern using while loop
    #Q4: Reverse Pyramid of Numbers
    #Q5: Print reverse number from 10 to 1
    #Q6: Pascal’s triangle pattern using numbers
    #Q7: Square pattern with numbers
    #Q8: Multiplication table pattern
    #Q9: Downward full Pyramid Pattern of star
    #Q10: full Pyramid Pattern of star
    #Q11: two pyramids of stars
    #Q12: Right start pattern of star
    #Q13: Left triangle pascal’s pattern
    #Q14: Pant style pattern of stars


class python_Task():
    

    def Q1():
         n = int(input("q1:"))
         for i in range(n):
             for j in range(n-i):
                print("5",end="")
             print()
    q1 = Q1()

    def Q2():
        n = int(input("q2:"))
        for i in range(n+1):
          for j in range(n+1-i):
              v= j
              print(v,end="")
          print()
    q2 =    Q2()

    def Q3():
        n = int(input("q3:"))
        v = 1
        for i in range(n):
            for j in range(i+1):
                  print(v,end="")
            print()
            v +=2
    q3 = Q3()

    def Q4():
        
        n=int(input("q4:"))
        for i in range(n+1):
             for j in range(i, 0, -1):
                print(j, end="")
             print("")
    q4 = Q4()

    def Q5():        
        start = 1
        stop = 2
        currentNumber = stop
        for row in range(2, 6):
           for col in range(start, stop):
               currentNumber -= 1
               print(currentNumber, end="")
           print("")
           start = stop
           stop += row
           currentNumber = stop
    q5 = Q5()


    def Q6():
        #_pascal_

        def triangle(size):
          for i in range(0, size):
             for j in range(0, i + 1):
                 print(decide_number(i, j), end=" ")
             print()


        def decide_number(n, k):
              num = 1
              if k > n - k:
                    k = n - k
              for i in range(0, k):
                  num = num * (n - i)
                  num = num // (i + 1)
              return num

        # set rows
        rows = 7
        triangle(rows)
    q6 = Q6()
    

    def Q7():
        rows = 5
        for i in range(1, rows + 1):
             for j in range(1, rows + 1):
                  if j <= i:
                       print(i, end=' ')
                  else:
                    print(j, end=' ')
             print()
    q7 = Q7()


    def Q8():
        rows = 8
        # rows = int(input("Enter the number of rows "))
        for i in range(1, rows + 1): #row start 1
             for j in range(1, i + 1): #col start 1
             # multiplication current column and row
                square = i * j
                print(i * j, end=" ")
             print()
    q8 = Q8()


    def Q9():       
        n=7
        for i in range(n):
             print(" " * i + " *" * (n-i))
    q9 = Q9()


    def Q10():  
        n=7
        for i in range(n):
            print(" " * (n-i) + " *" * i)
    q10 = Q10()


    def Q11():
        n=5
        for i in range(n):
             for j in range(i+1):
                  print("*",end="")
             print()
        print("")
        for i in range(n):
              for j in range(n-i):
                  print("*",end="")
        print()
    q11 = Q11()


    def Q12():
        n=5
        for i in range(n):
             for j in range(i):
                 print("*",end="")
             print()
        for i in range(n):
             for j in range(n-i):
                  print("*",end="")
             print()
    q12 = Q12()


    def Q13():
        rows = 5
        i = 1
        while i <= rows:
            j = i
            while j < rows:
              # display space
              print(' ', end=' ')
              j += 1
            k = 1
            while k <= i:
                print('*', end=' ')
                k += 1
            print()
            i += 1

        i = rows
        while i >= 1:
            j = i
            while j <= rows:
                print(' ', end=' ')
                j += 1
            k = 1
            while k < i:
                print('*', end=' ')
                k += 1
            print('')
            i -= 1
    q13 = Q13()

    

    def Q14():
        rows = 14
        print("*" * rows, end="\n")
        i = (rows // 2) - 1
        j = 2
        while i != 0:
            while j <= (rows - 2):
                 print("*" * i, end="")
                 print("_" * j, end="")
                 print("*" * i, end="\n")
                 i = i - 1
                 j = j + 2
    q14 = Q14()


ans = python_Task()
print(ans)



'''


print(ans.q1)
print(ans.q2)
print(ans.q3)
print(ans.q4)
print(ans.q5)
print(ans.q6)
print(ans.q7)
print(ans.q8)
print(ans.q9)
print(ans.q10)
print(ans.q11)
print(ans.q12)
print(ans.q13)
print(ans.q14)
print(ans.q15)
'''