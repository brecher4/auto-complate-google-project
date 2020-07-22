import string
from data.init_data import data_for_search, get_sentences_data


def character_replacement(substr, num_sentences):
    num_suitables = 0
    suitable_completions = []
    for i in range(0,len(substr),-1):
        for char in string.printable:

            corrction_str = substr[:i] + char + substr[i + 1:]
            place = data_for_search.get(corrction_str, None)
            
            if place:
                index_begin = place["begin"]
                index_end = place["end"]
                
                index_end = index_begin + num_sentences if num_suitables > num_sentences else index_end                
                num_suitables += index_end - index_begin

                nonlocal suitable_completions
                suitable_completions = get_sentences_data()[index_begin:index_end]
                num_sentences -= num_suitables
            
            if num_suitables > num_sentences:
                break

        if num_suitables > num_sentences:
                break


def deleting_character(substr, num_sentences):
    return []


def adding_character(substr, num_sentences):
    return []


def get_completions_with_correction(substr, num_sentences):
    correction_list = []
    correction_list += character_replacement(substr, num_sentences)
    correction_list += deleting_character(substr, num_sentences)
    correction_list += adding_character(substr, num_sentences)

    correction_list = sorted(correction_list, key=lambda k: k["score"], reverse=True)
    len_correction_list = len(correction_list)
    index_end = 5 if len_correction_list > 5 else len_correction_list
    
    return correction_list[:index_end]
