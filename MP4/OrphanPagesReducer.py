#!/usr/bin/env python3
import sys

#TODO
# pages = defaultdict(list)
mydict = {} 
orphans = []
for line in sys.stdin:
  # TODO
  line = line.strip()
  person, orphan = line.split('\t') #parent is str 
  
  # print(person,orphan)
  if int(orphan) == 0:
    orphans.append(int(person))
  # for key in mydict:
  # if len(mydict[key]) == 0:
    
for x in sorted(orphans):
  print(x)
# print(sorted(orphans))


  # pages['parent'] = parent  #create a list and then add the value to the list and then append or extend to form a dict 
  # pages['child'] = child    #loop through 
  # pages[parent].append(child)
  

# for p in pages:
#   if p[parent] = p[child]
#     pass 
#     #self link and not orphan 
#   for p[parent] in  

#TODO
# print(xx) print as final output

# 385744: 421957 3250680 3446893 5166549
