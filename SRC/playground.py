# page = {}

# input = "hello big"

# sentences_sort = [{sentence: page}]

# data{key: place}

# place = {"bagin":index,"end" : index}

# #algoritm

# place = data[input]

# return 


# sentence1 = "Hello"
# sentence2 = "Hi"

# sorce = {1: "completion.py"}

# sentences_sort = [{"sentence": "Hello", "src": 1}, {"sentence": "Hi", "src": 1}]

# data = {
#     "H": {
#         "begin": 0,
#         "end": 2
#     },

#     "He": {
#         "begin": 0,
#         "end": 1
#     }, 

#     "Hel": {
#         "begin": 0,
#         "end": 1
#     }, 

#     "Hell": {
#         "begin": 0,
#         "end": 1
#     }, 

#     "Hello": {
#         "begin": 0,
#         "end": 1
#     }, 

#     "Hi": {
#         "begin": 1,
#         "end": 2
#     }
# }


# import glob


# list_ = []

# for filename in glob.glob('data/technology_texts/...../*/*.txt'):
#    list_ += [filename]

# print(list_, len(list_))

# import os

# i = 0

# def scan_folder(parent):
#     # iterate over all the files in directory 'parent'
#     for file_name in os.listdir(parent):
#         if file_name.endswith(".txt"):
#             # if it's a txt file, print its name (or do whatever you want)
#             global i
#             print(i,file_name)
#             i += 1
#         else:
#             current_path = "".join((parent, "/", file_name))
#             if os.path.isdir(current_path):
#                 # if we're checking a sub-directory, recall this method
#                 scan_folder(current_path)

# scan_folder("data/technology_texts")

# import string
# print(string.printable.replace('a',''), len(string.printable.replace('a','')))

#TREI
# page = {}
# input = "hello big"
# sentences_sort = [{sentence: page}]
# trie = {key: node}
# node = {"next":node,
#         "begin": index
#         "end": index}
# # while()
# # {
# # }
# node = trie[input[0]] # arrive to node
# node["next"][input[1]]
# #
# #
# #arrived to end
# suitable_sen = 


# import shelve

# s = shelve.open('t.db')
# try:
#     s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
# finally:
#     s.close()


# s = shelve.open('t.db')
# try:
#     existing = s['key1']
# finally:
#     s.close()

# print(existing)