# 1.Right angled triangle
# * 
# * * 
# * * *
# * * * *
# * * * * *
# * * * * * *
for i in range(1,7):
    print('* '*i)
# or
for i in range(0,7):
    for j in range(0,i+1):
        print(" *", end=" ")
    print()

# 2.Inverted right angled triangle
# * * * * * * * 
# * * * * * * 
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range (7,0,-1):
    print('* '*i)
# or
for i in range(7,0,-1):
    for j in range(1,i+1):
        print(" *", end=" ")
    print()

# 3.Pyramid pattern
# * 
# * * * 
# * * * * *         
# * * * * * * *     
# * * * * * * * * * 

for i in range(1,11,2):
    print("* " *i)


# 4.Pyramid
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
for i in range(1,6):
    for j in range(5-i):
        print(" ", end=" ")
    for j in range(1, 2*i):
        print("*", end=" ")
    print()

# 5.Inverted pyramid pattern
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * *
#       * * *
#         *
for i in range (5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()
        

# 6. inverted pyramid
# * * * * * * * * * * 
# * * * * * * * * 
# * * * * * *
# * * * *
# * *

for i in range(10,0,-2):
    print('* '*i)

# 7. Diamond pattern
# * 
# * * 
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(1,7):
    print('* ' *i)
for j in range(5,0,-1):
    print('* '*j)

# 8. Square pattern
# * * * * * 
# *       * 
# *       *
# *       *
# * * * * *
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

# 9. Full square
# * * * * * 
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
for i in range(5):
    print('* * * * * ')
# or
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

# 10.Square parallel bar pattern
# *       * 
# *       * 
# *       *
# *       *
# *       *

for i in range(5):
    for j in range(5):
        if j==0 or j==4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 11.Square Plus Pattern
#     *     
#     *     
# * * * * *
#     *
#     *

for i in range(5):
    for j in range(5):
        if i==5//2 or j==5//2:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

# 12.Cross Pattern
# *       * 
#   *   *   
#     *
#   *   *
# *       *
for i in range(5):
    for j in range(5):
        if i==j or i+j==4:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()


# 13. hallo right angle trangle
# *  
# *  *  
# *     *
# *        *
# *           *
# *  *  *  *  *  *
for i in range(1,7):
    for j in range(1, i+1):
        if j==1 or j==i or i==6:
            print('* ', end=' ')
        else:
            print('  ', end=' ')
    print()

# 14. hallo inverted right angle trangle
# *  
# *  *  
# *     *
# *        *
# *           *
# *  *  *  *  *  *
for i in range(7,0,-1):
    for j in range(1, i+1):
        if j==1 or j==i or i==7:
            print('* ', end=' ')
        else:
            print('  ', end=' ')
    print()

# 15.Non fill Diamond
# *  
# *  *
# *     *
# *        *
# *           *
# *              *
# *  *  *  *  *  *  *
# *              *
# *           *
# *        *
# *     *
# *  *
# * 
for i in range(1,7):
    for j in range(1, i+1):
        if j==1 or j==i :
            print('* ', end=' ')
        else:
            print('  ', end=' ')
    print()
for i in range(7,0,-1):
    for j in range(1, i+1):
        if j==1 or j==i or i==7:
            print('* ', end=' ')
        else:
            print('  ', end=' ')
    print()

# 16.right angle trangle by using numbers
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6

for i in range(0,7):
    print(' '.join(str(x) for x in range(1,i+1)))
# or
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# 17.inverse right angle trangle by numbers
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(7,0,-1):
    print(' '.join(str(x) for x in range(1,i+1)))
# or
for i in range(5,0,-1):
    for j in range(1, i+1):
        print(j,end=" ")
    print()

# 18.Diamond pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
for i in range(0,7):
    print(' '.join(str(x) for x in range(1,i+1)))
for j in range(7,0,-1):
    print(' '.join(str(x) for x in range(1,j+1)))
# or 
for i in range(0,8):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(6,0,-1):
    for j in range(1, i+1):
        print(j,end=" ")
    print()

#19.Numeric pattern
# 1 
# 2 1       
# 3 2 1     
# 4 3 2 1   
# 5 4 3 2 1 

for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
        i-=1
    print()

#20.floyd'd trangle
# 1 
# 2 3 
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
num=1
for i in range(1,6):
    for j in range(1,i+1):
        print(num, end=' ')
        num+=1
    print()

# 21.Hollow pyramid pattern
#         * 
#       *   * 
#     *       *
#   *           *
# * * * * * * * * *
for i in range(1,6):
    for j in range(5-i):
        print(' ',end=' ')
    for j in range(2*i-1):
        if j==0 or j==2 * i-2 or i ==5:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()



# 22.Hollow Inverted pyramid
# * * * * * * * * * 
#   *           * 
#     *       *
#       *   *
#         *

for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(1, 2*i):
        if j==1 or i==5 or j==2*i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# 23.Hollow diamond pattern
#         * 
#       *   * 
#     *       *
#   *           *
# *               *
#   *           *
#     *       *
#       *   *
#         *
n=5
for i in range(1, n+1):
    for j in range(5-i):
        print(' ',end=' ')
    for j in range(2*i-1):
        if j==0 or j==2 * i-2:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(n-1,0,-1):
    for j in range(5-i):
        print(' ', end=' ')
    for j in range(2*i-1):
        if j==0 or j==2*i-2 or i==5:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()

# 24.hallow daimaond
#         1 
#       2   2 
#     3       3
#   4           4
# 5 5 5 5 5 5 5 5 5
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(2*i-1):
        if j == 0 or j==2*i-2 or i ==5:
            print(i,end=' ')
            
        else:
            print(' ', end=' ')
    print()

# 25.Hallow diamond numbers
#         1 
#       2   2 
#     3       3 
#   4           4 
# 5               5 
#   4           4 
#     3       3 
#       2   2 
#         1

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(2*i-1):
        if j == 0 or j==2*i-2:
            print(i,end=' ')
            
        else:
            print(' ', end=' ')
    print()

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(2*i-1):
        if j == 0 or j==2*i-2:
            print(i,end=' ')
            
        else:
            print(' ', end=' ')
    print()


# 26.     1 
#   4           4 
#     3       3
#       2   2
#         1
#       2   2
#   4           4
#     3       3
#       2   2
#         1
#     3       3
#   4           4
#     3       3
#       2   2
#         1
#   4           4
#   4           4
#     3       3
#       2   2
#         1
# 5               5
#   4           4
#     3       3
#       2   2
#         1

n=5
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end=' ')
        
    for j in range(2 * i - 1):
        if j==0 or j== 2 * i - 2:
            print(i, end=' ')
        else:
            print(' ',end=' ')
    print()
    
    for i in range(n - 1, 0,  -1):
        for j in range(n - i):
            print(' ',end=' ')
        for j in range(2 * i -  1):
            if j == 0 or j == 2 * i - 2:
                print(i,end=' ')
                
            else:
                print(' ', end=' ')
        print()

# 27.
# 1                 1 
# 1 2             1 2 
# 1 2 3         1 2 3
# 1 2 3 4     1 2 3 4
# 1 2 3 4 5 1 2 3 4 5
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(2*(n-i)):
        print(' ', end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# 28. Butterfly
# 1                 1 
# 1 2             1 2 
# 1 2 3         1 2 3
# 1 2 3 4     1 2 3 4
# 1 2 3 4 5 1 2 3 4 5
# 1 2 3 4     1 2 3 4
# 1 2 3         1 2 3
# 1 2             1 2
# 1                 1

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(2*(n-i)):
        print(' ', end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
    
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(2*(n-i)):
        print(' ', end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# 29.
# 1                 1 
# 1 2             1 2 
# 1 2 3         1 2 3
# 1 2 3 4     1 2 3 4
# 1 2 3 4 5 1 2 3 4 5
# 1 2 3 4 5 1 2 3 4 5
# 1 2 3 4     1 2 3 4
# 1 2 3         1 2 3
# 1 2             1 2
# 1                 1

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(2*(n-i)):
        print(' ', end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
    
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(2*(n-i)):
        print(' ', end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# 30. 
# *                 * 
# * *             * * 
# * * *         * * * 
# * * * *     * * * * 
# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 * 

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    for j in range(2*(n-i)):
        print(' ', end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()
    
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print('*',end=' ')
    for j in range(2*(n-i)):
        print(' ', end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()

# 31.
# *                 * 
# * *             * * 
# * * *         * * * 
# * * * *     * * * * 
# * * * * * * * * * * 
# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 * 

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    for j in range(2*(n-i)):
        print(' ', end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()
    
for i in range(n,0,-1):
    for j in range(1,i+1):
        print('*',end=' ')
    for j in range(2*(n-i)):
        print(' ', end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()

# 32.
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
n=5
for i in range(1,n+1):
    
    for j in range(n-i):
        print(' ', end=' ')
        
    for j in range(2*i-1):
        print('*', end=' ')
        
    print()

# 33.
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

n=5
for i in range(n,0,-1):
    
    for j in range(n-i):
        print(' ', end=' ')
        
    for j in range(2*i-1):
        print('*', end=' ')
        
    print()

# 34.
#         * 
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(' ', end=' ')
        
    for j in range(2*i-1):
        print('*', end=' ')
    print()
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ', end=' ')
        
    for j in range(2*i-1):
        print('*', end=' ')
    print()

# 35.Alphabet Triangle
# A 
# A B 
# A B C
# A B C D
# A B C D E
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64 +j), end=" ")
    print()

# 36.Inverted Alphabet Triangle
# A B C D E F 
# A B C D E 
# A B C D
# A B C
# A B
# A
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(chr(64 +j), end=" ")
    print()

# 37.Alphabet Diamond
# A 
# A B 
# A B C
# A B C D
# A B C D E
# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A

for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64 +j), end=" ")
    print()
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(chr(64 +j), end=" ")
    print()

# 38.Pascals Triangle
#           1   
#         1   1   
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1

for i in range(5):
    num=1
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(i + 1):
        print(num, end="   ")
        num=num * (i-k)//(k+1)
    print()

# 39.Square Number Pattern 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()

# 40.Zig-Zag Number pattern
# 1 0 1 0 1 
# 0 1 0 1 0 
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1

for i in range(1,6):
    for j in range(1,6):
        if (i+j)%2==0:
            print("1", end=" ")
        else:
            print("0",end=" ")
    print()