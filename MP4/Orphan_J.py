import sys
import re

mydict = {}
orphans = []
fromPages = set()
toPages = set()
for line in sys.stdin:
    # TODO
    line = line.strip()
    fromPage, toPage = line.split(':')
    toPage = toPage.strip().split(" ")

    fromPages.add(int(fromPage))
    if fromPage in toPage:
        toPage.remove(fromPage)

    for x in toPage:
        toPages.add(int(x))

    #toPages.discard(fromPage)

orphans = fromPages.difference(toPages)
# for key in sorted(orphans):
#     print('%s' % (key))

for key in orphans:
  print('%s\t%s' % (key, 0))