i = 0
# while 0 <= i < len(lines):
#     instr, *l = lines[i].split()

#     #print(i, instr, l, reg)
#     #input()

#     if l[0][0] in '-0123456789':
#         a = int(l[0])
#     else:
#         a = l[0]
#         if a not in reg:
#             reg[a] = 0
    
#     if len(l) == 2:
#         if l[1][0] in '-0123456789':
#             b = int(l[1])
#         else:
#             b = reg[l[1]]

#     if instr == "snd":
#         if l[0][0] in '-0123456789':
#             sound = a
#         else:
#             sound = reg[a]        
#     elif instr == "set":
#         reg[a] = b
#     elif instr == "add":
#         reg[a] += b
#     elif instr == "mul":
#         reg[a] *= b
#     elif instr == "mod":
#         reg[a] %= b
#     elif instr == "rcv":
#         if b != 0:
#             print(sound)
#             rcv = sound
#             break
#     elif instr == "jgz":
#         if l[0][0] in '-0123456789':
#             if a > 0:
#                 i += b
#                 continue
#         else:
#             if reg[a] > 0:
#                 i += b
#                 continue
#     i += 1

# print(rcv)