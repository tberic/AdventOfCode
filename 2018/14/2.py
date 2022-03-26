recipe = "503761"

recipes = "37"
pos1 = 0
pos2 = 1

while True:    
    x = int(recipes[pos1]) + int(recipes[pos2])
    if x < 10:
        recipes += str(x)
    elif x >= 10:
        recipes += str(x//10)
        recipes += str(x%10)

    if recipe in recipes[-20:]:
        print(recipes.index(recipe))
        break

    pos1 = (pos1 + int(recipes[pos1]) + 1) % len(recipes)
    pos2 = (pos2 + int(recipes[pos2]) + 1) % len(recipes)