import json
from pprint import pprint

num_levels = 3
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

# Top level doesn't have 'nodes' field
for tree in data['tree']:
    dfs(tree)

master_list = sorted(master_list)

print(sorted(master_list))
print len(master_list)

# Check for proper formatting of subjects
for subject in master_list:
    if len(subject.split(delim)) > num_levels:
        print 'Improperly formatted: ' + subject
        exit(1)

output = open('top_' + str(num_levels) + '_levels_flat.json', 'w')

output.write(json.dumps({ "subjects": master_list } ))
