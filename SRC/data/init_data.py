import string
import os
import re


source_files = {0: "data/contents.txt"}

id_file = 1 

sentences_data = []

data_for_search = {}



def get_sentences_data():
    return sentences_data


def get_source_files():
    return source_files


def init_source_files(parent):
    global id_file
    
    for file_name in os.listdir(parent):
        
        if file_name.endswith(".txt"):
            source_files[id_file] = "".join((parent, "/", file_name))
            id_file += 1
        
        else:
            current_path = "".join((parent, "/", file_name))
            if os.path.isdir(current_path):
                init_source_files(current_path)


def remove_space_of_begin(sentence):
    while(sentence and sentence[0] == ' '): 
        sentence = sentence[1:]
    
    return sentence


def get_dict_of_sentences(sentence, id_src, num_line):
    sentence = remove_space_of_begin(sentence)
    return {"sentence": sentence, "src": id_src, "line": num_line}


def read_from_files():  
    for id, name in list(source_files.items())[:1]:
        global sentences_data

        with open(name) as file:
            sentences = file.read().split("\n")

        for num_line, sentence in enumerate(sentences):
            dict_sentence = get_dict_of_sentences(sentence, id, num_line)

            if dict_sentence["sentence"] != "":
                sentences_data += [dict_sentence]


def get_sub_sentences(sentence):
    return [sentence[i:j] for i in range(0, len(sentence)) for j in range(i + 1, len(sentence) + 1)]


def ignore_punctuation_and_spaces(str):
    str = str.lower()
    exclude = set(string.punctuation)
    str = ''.join(ch for ch in str if ch not in exclude)        
    str = str.split(' ')
    return ' '.join([c for c in str if c != ''])
    

def init_data_for_search():
    for index, item in enumerate(sentences_data):
        sub_sentences = get_sub_sentences(item["sentence"])
    
        for sub in sub_sentences:
            sub = ignore_punctuation_and_spaces(sub)

            if sub not in data_for_search:
                data_for_search[sub] = {index}
            else:
                data_for_search[sub].add(index)
                

    for sub in data_for_search.keys():
        data_for_search[sub] = sorted(data_for_search[sub], 
            key=lambda k: sentences_data[k]["sentence"])


def init_meta_data():
    init_source_files("data/technology_texts")
    read_from_files()
    init_data_for_search()


# if __name__ == "__main__":
    # init_source_files("data/technology_texts")
    # print(source_files)

    # init_meta_data()
    # print(f'{sentences_data} \n')
    # print(f'{data_for_search["C server"]} \n')

    # for i in data_for_search["C server"]:
    #     print(f'{sentences_data[i]} \n')