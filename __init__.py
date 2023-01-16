from difPy.dif import dif

if _name_ == "_main_":
    search = dif("/mnt/e/ProiectPython/Photos")
    
  
    print()
    print("What search criteria do we use?:")
    for key, value in search.stats.items():
        print(key, end=" --- ")
        try:
            for j in value:
                print(j, end="")
        except:
            print(value, end="")
        
        print()
        
    print()
    print("A list of duplicates/similar images that have the lowest quality:" )
    for key, value in search.result.items():
        print("ID ===> " + key, end="")
        print(" : ", end="")
        for i in value['duplicates']:
            print("PATH ===> " + i, end=" ")
        print()
    
    print()
    
    
    # Putem modifica parmaetrii de cautare dupa cum dorim
    search = dif("/mnt/e/ProiectPython/Photos", recursive=False, similarity="low", px_size=1000, show_progress=True, show_output=True, delete=False)
    
    print()
    
    print("PICHUNTER ==> PYTHON STRONG")