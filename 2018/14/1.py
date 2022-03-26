nRecipes = 503761

recipes = [3, 7]
pos1 = 0
pos2 = 1

while len(recipes) < nRecipes + 10:
	#print(recipes, pos1, pos2)
	x = recipes[pos1] + recipes[pos2]
	if x < 10:
		recipes.append(x)
	elif x >= 10:
		recipes.append(x//10)
		recipes.append(x%10)

	pos1 = (pos1 + recipes[pos1] + 1) % len(recipes)
	pos2 = (pos2 + recipes[pos2] + 1) % len(recipes)

print("".join( map(str, recipes[nRecipes:nRecipes+10]) ))