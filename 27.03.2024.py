text = input()
new_list = list(text)

def count_new_list(new_list):
  count = 0
  for i in new_list:
    count += 1
  return count
total = count_new_list(new_list)
print(total)