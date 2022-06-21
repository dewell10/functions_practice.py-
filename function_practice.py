def hello():
    print("Hello New Python Programmer, welcome ")
hello()

def pack(a,b,c):
    mylist = []
    mylist.append(a)
    mylist.append(b)
    mylist.append(c)
    return mylist
print(pack(1,2,3))


def eat_lunch(lunchbox):
  if len(lunchbox) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(lunchbox)):
      if i == 0:
        print(f"First I eat {lunchbox[0]}")
      else:
        print(f"Next I eat {lunchbox[i]}")



eat_lunch([])
eat_lunch(["chicken","rice","veggies",])