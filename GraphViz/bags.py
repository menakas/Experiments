import sys 
from collections import deque

target = 'shinygold'
E = {}
defined = set()

##colors added for printing dot file
colors = {}
colors['lightred'] = '#ff7276'
colors['darkorange'] = '#dc582a'
colors['darkred'] = '#9b1003'
colors['darkyellow'] = '#ffcc00'
colors['darkgreen'] = '#006400'
colors['darkblue'] = '#1338be'
colors['darkviolet'] = '#9400d3'
colors['brightwhite'] = '#fdfeff'
colors['mutedyellow'] = '#e0d268'
colors['shinygold'] = '#dfaf37'
colors['darkolive'] = '#556b2f'
colors['fadedblue'] = '#879eb0'
colors['vibrantplum'] = '#9c50b6'
colors['dottedblack'] = '#aaaaaa'

def compress( text ):
    text = text.strip()
    words = text.split(' ')
    out = ''
    for word in words:
        while any([word.startswith(d) for d in '0123456789']):
            word = word[1:]
        if 'bag' in word:
            continue
        out += word
    return out

##Graph for the dot file
print('digraph G { \
node[shape=box] \n')

	
for line in sys.stdin:
    line = line.strip()
    (container,contents) = line.split(' contain ')
    container = compress(container)

    ##logic for printing dot file
    if container not in defined:
        print(container, '[fillcolor=\"',colors[container],'\",style=\"filled\"]\n')
        defined.add(container)

    bags = contents.split(',')
    for bag in bags:
        bag = compress(bag)
        if bag == 'noother':
            break

        ##logic for printing dot file
        if bag not in defined:
            print(bag, '[fillcolor=\"',colors[bag],'\",style=\"filled\"]\n')
            defined.add(bag)

        if bag not in E:
             E[bag] = []
        print(container, '->' ,bag)
        E[bag].append(container)

SEEN = set()
Q = deque([target])
while Q:
    ##print(Q)
    x = Q.popleft()
    ##print(x)
    if x in SEEN:
        continue
    SEEN.add(x)
    ##print("Seen", SEEN)
    for y in E.get(x,[]):
          Q.append(y)

       
##print(len(SEEN)-1)

##Close the graph in the dot file
print('}')
 
