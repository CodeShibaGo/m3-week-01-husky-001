def age_difference(ages):
     ages.sort()
     print(ages)

     difference = ages[0],ages[-1]
     print(difference)
     return (difference)


age_difference([18, 25, 50, 35, 40])


