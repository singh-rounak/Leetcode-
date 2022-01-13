  arr.sort()
  a = len(arr)
  sum_ = 0
  for i in range(a):
    for j in range(i+1, a):
      k = j + 1
      l = a - 1
      while k < l:
        sum_ = arr[i]+ arr[j]+ arr[k]+ arr[l]
        if sum_ == s:
          return  [arr[i],arr[j],arr[k],arr[l]]
        
        elif sum_ < s:
          k += 1
    
        else:
          l -= 1
  return []