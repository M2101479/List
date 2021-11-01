List =  ["Mat" , "lap", "ball", "toy", "roll"]
List2 = [1 ,2, 3, 4, 5]
square = [number ** 2 for number in List2] 
List3 = zip(List, List2)
List3_list = list(List3)
List2.reverse()
List2.extend(List)

print(List3_list)
print(List2)
print(square)
