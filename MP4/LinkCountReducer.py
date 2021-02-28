import sys

#TODO
total = {}
for line in sys.stdin:
  # TODO
    line = line.strip()
    page, count = line.split('\t', 1)
  
    if page not in total:
        total[page] = 0
    total[page] = total[page] + int(count)

# TODO
for x in total: 
    print('%s\t%s' % (x, total[x]))



# 385744: 421957 3250680 3446893 5166549