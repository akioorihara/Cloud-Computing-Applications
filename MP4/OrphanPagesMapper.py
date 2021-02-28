#!/usr/bin/env python3
import sys
import re 

mydict = {}
orphans = set()
fromPages = set()
toPages = set()
for line in sys.stdin:
  # TODO
    line = line.strip()
    fromPage, toPage = line.split(':')
    toPage = toPage.strip().split(" ")
    if int(fromPage) == int(toPage[0]):
      orphans.add(int(fromPage))
      

    fromPages.add(int(fromPage))
    for x in toPage:
      if int(x) != int(fromPage):
        toPages.add(int(x))

    toPages.discard(int(fromPage))
# print(orphans)
# orphans = orphans.union(fromPages.difference(toPages))
orphans = fromPages.difference(toPages)
for key in orphans:
  print('%s\t%s' % (key, 0))

# # #!/usr/bin/env python3
# import sys
# import re 

# mydict = {}
# orphans = []
# for line in sys.stdin:
#   # TODO
#     line = line.strip()
#     fromPage, toPage = line.split(':')
#     toPage = toPage.strip().split(" ")
    
#     fromPage = int(fromPage) 
#     if fromPage not in mydict:
#      mydict[fromPage] = set()

#     for child in toPage:
#       if '\n' in child:
#         child = child.replace('\n', '')
#       child = int(child)
#       if child is fromPage:
#         # print("self link", fromPage, child)
#         continue
#       if child not in mydict: 
#         mydict[child] = set()
#         mydict[child].add(fromPage)
      
# for key in mydict:
#   print('%s\t%s' % (key, len(mydict[key]) ))









# # for key in mydict:
# #   if len(mydict[key]) == 0:
# #     orphans.append(int(key))


#   # print('%s\t%s' % ( , )) #pass this output to reducer

# # 385744: 421957 3250680 3446893 5166549 #this is a test purpose
