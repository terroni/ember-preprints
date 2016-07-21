import json
from pprint import pprint

delim = "_"
master_list = []

def dfs(tree):
    # Prime the pump
    stack = []
    stack.append(tree)
    while len(stack) > 0:
        current = stack.pop()

        # Add to master list
        master_list.append(current['text'][0])

        # Append child nodes
        if 'nodes' in current:
            for node in current['nodes']:
                # Prepend parent subjects to child subjects
                node['text'][0] = current['text'][0] + delim + node['text'][0]
                stack.append(node)

with open('top3levels.json') as data_file:
    data = json.load(data_file)

for tree in data['tree']:
    dfs(tree)

master_list = sorted(master_list)

print(sorted(master_list))

print len(master_list)

for subject in master_list:
    if len(subject.split(delim)) > 3:
        print 'Improperly formatted: ' + subject
        exit(1)

output = open('top_3_levels_flat.json', 'w')
#
# output.write('{\n')
# output.write('\t"subjects": [')
# output.write('\t\t' + ',\n\t\t'.join(master_list) + '\n')
# output.write('\t]\n')
# output.write('}')

output.write(json.dumps({ "subjects": master_list } ))
