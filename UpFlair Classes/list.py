# list = [] --- Single variable to store multile values
# Ordered, Mutable
# allow duplicate value & is hertrogeneou 

# lst =[1,2,'hello', True,1.2]
# print(lst)
# print(type(lst))

### Indeing And Slicing ###

# lst = [1,2,3,4,5]
# print(lst[1])
# print(lst[-2])
# print(lst[1:3])
# print(lst[:3])
# print(lst[1:])
# print(lst[-3:-1])
# print(lst.append(6))
# print(lst)
# lst[0]='Green'
# print(lst)

# l1=[1,2,3,4]
# l1[0:3]=['Red','Green','Blue','Yellow']
# print(l1)
# lst=['red','blacK','blue']
# lst[0:2] = "Green"
# lst[0:2] = ["Green"]
# lst[0:2] ['Green','Yellow']
# lst[0:1] = ["a","b","c",'Red']
# print(lst)

###Methos in List###
# print(lst.count('Red'))
# print(lst.index('Red'))   #Gives the index value of the first one apearing in the list

# lst.clear()
# print(lst)
# del lst
# print(lst)

lst=['Red','Green','Red','Blue','Yellow']
# lst2=lst.copy()  # copies all the data of lst in lst2 
# print(lst2)

# lst.append("Purple") # Adds only one item at the last of the list
# print(lst)

# lst.extend(["a",'b','c'])
# lst.insert(1,"Black")
# lst.pop(['Red']) # Not possible only works for Index value
# lst.pop(1)
# lst.remove('Red')
# lst.reverse()
# lst.sort()
# lst.sort(reverse = True)

print(lst[::-1])


