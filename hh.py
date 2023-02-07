# def combs(a):
#     if len(a) == 0:
#         return [[]]
#     cs = []
#     for c in combs(a[1:]):
#         cs += [c, c+[a[0]]]
#     return cs

# a = [1, 2, 3, 4, 5, 6]
# print(combs(a))

# from itertools import chain, combinations
# def powerset(iterable):
#   s = list(iterable)
#   return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
# nums = [1,2,3,4,5]
# print(powerset(nums))

# r =[]
# for i in range(len(r)+1):
#     for j in range(len(r)+1):
#         t1 = tuple(set(r[:i] + r[:j]))
#         t2 = tuple(set(r[i:] + r[j:]))
#         t3 = tuple(set(r[i:] + r[:j]))
#         t4 = tuple(set(r[:i] + r[j:]))
#         t5 = tuple(set(r[i:j]))

#         # print(t)
#         r.append(t1)
#         r.append(t2)
#         r.append(t3)
#         r.append(t4)
#         r.append(t5)
        

# print(set(r))




# file = open('wiki_MLLKh.txt', 'w')
# idx = 0
# string = "Machine learning (ML) is a field of inquiry devoted to understanding and building methods that learn, that is, methods that leverage data to improve performance on some set of tasks.[1] It is seen as a part of artificial intelligence."

# for i in range(len(string)):
#     inp = int(input("Enter a number: "))
#     if idx + inp > len(string):
#         file.write(string[i*inp:])
#         break
#     part_string = string[idx:idx + inp]
#     idx += inp
#     file.write(part_string + '\n')
# file.close()


# string = 'The discipline of machine learning employs various approaches to teach computers to accomplish tasks where no fully satisfactory algorithm is available. In cases where vast numbers of potential answers exist, one approach is to label some of the correct answers as valid. This can then be used as training data for the computer to improve the algorithm(s) it uses to determine correct answers. For example, to train a system for the task of digital character recognition, the MNIST dataset of handwritten digits has often been used.'
# d = {}
# idx = 0
# for i in range(len(string)):
#     if string[i] == '.':
#         d[idx] = string[:i] + '.'
#         idx+=i
# print(d)

'''AS LIST'''
# from string import ascii_lowercase as alpha
# string = 'The discipline of machine learning employs various approaches to teach computers to accomplish tasks where no fully satisfactory algorithm is available. In cases where vast numbers of potential answers exist, one approach is to label some of the correct answers as valid. This can then be used as training data for the computer to improve the algorithm(s) it uses to determine correct answers. For example, to train a system for the task of digital character recognition, the MNIST dataset of handwritten digits has often been used.'
# result = enumerate(string.split('. '))
# for k, v in result:
#   print(alpha[k], v)


'''AS DICT'''
# from string import ascii_lowercase as alpha
# string = 'The discipline of machine learning employs various approaches to teach computers to accomplish tasks where no fully satisfactory algorithm is available. In cases where vast numbers of potential answers exist, one approach is to label some of the correct answers as valid. This can then be used as training data for the computer to improve the algorithm(s) it uses to determine correct answers. For example, to train a system for the task of digital character recognition, the MNIST dataset of handwritten digits has often been used.'
# d = dict(zip(alpha, string.split('. ')))
# print(d)
''''mmm'''


# d = {str(i): sentence + '.' for i, sentence in enumerate(string.split('.')) if sentence}



            