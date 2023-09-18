# ----- Recursion ----- #

import os

def task01():
    def is_palindrome_recursive(x):
    
        x = x.replace(' ', '').lower()
        if len(x) <= 1:
            return True
        
        # Vérifier si le premier et le dernier caractère sont identiques
        if x[0] == x[-1]:
            # Appeler récursivement la fonction sur la sous-chaîne en enlevant le premier et le dernier caractère
            return is_palindrome_recursive(x[1:-1])
        
        return False

    result = is_palindrome_recursive('Was it a car or a cat I saw')
    print(result)



def task02(path='/home/lukimperinetti/Documents/MSc-PrePool/', visited = set()):
    if path not in visited:
        for root,dirs,files in os.walk(path, topdown=True):
            print (root)
            print (dirs)
            print (files)
            for all in dirs:
                path = os.path.join(root, all)
                task02(path, visited)
    


# task01()
task02()
