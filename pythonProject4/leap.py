year=int(input("enter the current year"))
final=int(input("enter the final year"))
for y in(range(year,final)):
              if y%4==0 and y%100!=0 or y%400==0:
                    print(y)

