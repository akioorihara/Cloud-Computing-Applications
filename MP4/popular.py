import sys

mydict = {}
orphans = []
for line in sys.stdin:
  # TODO
  line = line.strip()
  fromPage, toPage = line.split(':')
  toPage = toPage.strip().split(" ")

  try:
    x = set(toPage.remove(fromPage))
  except:
    x = set(toPage)
  if fromPage not in mydict:
    mydict[fromPage] = set()

  mydict[fromPage].update(x)

  for child in toPage:
    if child not in mydict:
      mydict[child] = set()

for key in mydict:
  print('%s\t%s' % (key, len(mydict[key]) ))

