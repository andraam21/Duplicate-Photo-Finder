from difPy.dif import dif

search = dif("/mnt/e/vs_code_structura_c/ProiectPython/Photos")
print("\n")

print("CRITERII DUPA CARE S-A REALIZAT CAUTAERA:")
for key, value in search.stats.items():
    print(key, value)
    
# print(search.stats)
print()
print("DUPLICATED PHOTOS \n" )
for key in search.result:
    print(search.result[key]['duplicates'])
    print()
    
print(search.result)