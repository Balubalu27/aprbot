import argparse

import pandas as pd
import spacy


def read_file(file_path):
    """Возвращает текст из файла"""
    try:
        with open(file_path, 'r') as file:
            file_text = file.read()
        return file_text
    except FileNotFoundError:
        print('Указанного файла не существует, проверьте название/расположение файла.')
        exit(1)


def args_parse():
    """Парсит аргументы командной строки"""
    parser = argparse.ArgumentParser(description='Text to html')
    parser.add_argument('input_txt_file', type=str, help='Input txt file path')
    parser.add_argument('output_html_file', type=str, help='Output html file path')
    arguments = parser.parse_args()
    return arguments


def spacy_find_nums_and_propn(file_path):
    """Возвращает словарь из найденых в тексте файла чисел и имен собственных"""
    dict_of_tokens = {}
    nlp = spacy.load("en_core_web_sm")
    text = read_file(file_path)
    doc = nlp(text)

    for token in doc:
        if token.pos_ == 'PROPN' or token.pos_ == 'NUM':
            dict_of_tokens[token.text] = dict_of_tokens.get(token.text, 0) + 1
    return dict_of_tokens


def dict_to_html(token_dict, html_file_path):
    """Формирует html файл из словаря"""
    html_df = pd.DataFrame(token_dict.items(), columns=['entries', 'count'])
    html_text = html_df.to_html(index=False)
    with open(html_file_path, 'w') as html_file:
        html_file.write(html_text)
        print('* Html file created *')


def main():
    try:
        args = args_parse()
        nums_and_propn_dict = spacy_find_nums_and_propn(args.input_txt_file)
        dict_to_html(nums_and_propn_dict, args.output_html_file)
        print('** Success myprogram.py**')
    except Exception as ex:
        print('Во время выполнения программы произошла ошибка:', ex)


if __name__ == '__main__':
    main()
