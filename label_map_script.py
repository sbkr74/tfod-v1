import os 
main_loc = os.path.join('TensorFlow','workspace','training_demo')
label_file = 'label_map.pbtxt'
path_file = os.path.join(main_loc,'annotations',label_file)
labels = [{'name':'hi', 'id':1}, {'name':'ok', 'id':2}, {'name':'iloveyou', 'id':3}, {'name':'peace', 'id':4}, {'name':'call', 'id':5}]

with open(path_file, 'w') as f:
    for label in labels:
        f.write('item { \n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')