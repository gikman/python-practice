def naive_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

def binary_search(arr, target, low=None, high=None):
  if low is None:
    low = 0
  if high is None:
    high = len(arr) - 1
  if high < low:
    return -1

  mid = (low + high) // 2

  if arr[mid] == target:
    return mid
  elif target < arr[mid]:
    return binary_search(arr, target, low, mid-1)
  else:
    return binary_search(arr, target, mid+1, high)

if __name__=='__main__':
  arr = [1, 3, 5, 10, 12]
  target = 10
  print(naive_search(arr, target))
  print(binary_search(arr, target))
  print(len(arr))
