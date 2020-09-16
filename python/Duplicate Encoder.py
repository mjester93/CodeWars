def duplicate_encode(word):
  final_array = []
  count = {}
  for s in word:
    if s.lower() in count:
      count[s.lower()] += 1
    else:
      count[s.lower()] = 1
    
    for s in word:
      if count[s.lower()] > 1:
        final_array.append(')')
      else:
        final_array.append('(')
            
    return "".join(final_array)
    
