chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
   list3 = []

   for i in list1:
       list3.append(i)

   for j in list2:
       list3.append(j)
   
   return list3

print(merge_list(chunk_one, chunk_two))
