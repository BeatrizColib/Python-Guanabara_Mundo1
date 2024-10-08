side_01= float(input('Enter the first side: '))
side_02= float(input("Enter the second: "))
side_03= float(input('Enter the third side: '))

if side_01 < side_02 + side_03 and side_02 < side_01 + side_03 and side_03 < side_01 + side_02:
    print('It is possible to form a triangle with these sides')
else:
    print('It is not possible to form a triangle with these sides')