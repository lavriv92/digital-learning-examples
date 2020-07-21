normal_dict = {
  'key1': 'value1',
  'key2': 'value2',
  'key3': 'value3'
}

inverted_dict = { v: k for k,v in normal_dict.items() }

print('Normal dict: ', normal_dict)
print('inverted dict: ', inverted_dict)