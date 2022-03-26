i = 0
# for line in reversed(lines):
#     i += 1
#     words = line.strip().split()
#     if words[0] == "swap" and words[1] == "position":
#         x = int(words[2])
#         y = int(words[5])
#         s = swapPos(s, x, y)
#     elif words[0] == "swap" and words[1] == "letter":
#         a = words[2]
#         b = words[5]
#         s = swapLetter(s, a, b)
#     elif words[0] == "rotate" and (words[1] == "left" or words[1] == "right"):
#         x = int(words[2])
#         if words[1] == "left":
#             x = -x
#         s = rotate(s, x)
#     elif words[0] == "rotate" and words[1] == "based":
#         c = words[6]        
#         s = rotatePos(s, c)
#     elif words[0] == "reverse":
#         x = int(words[2])
#         y = int(words[4])
#         s = reverse(s, x, y)
#     elif words[0] == "move":
#         x = int(words[2])
#         y = int(words[5])
#         s = move(s, x, y)
#     #print(i, s)

# print(s)