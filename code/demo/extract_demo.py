import os
import re

import sys

sys.path.append("/home/lys/实体关系抽取/open-entity-relation-extraction-master/code")
print(sys.path)
#sys.path.append("..")# 先跳出当前目录
from code.core.extractor import Extractor
from code.core.nlp import NLP
#from ..core.nlp import NLP


if __name__ == '__main__':
    input_path = '../../data/st.txt'  # 输入的文本文件
    output_path = '../../data/test_knowledge_triple.json'  # 输出的处理结果Json文件
    if os.path.isfile(output_path):
        os.remove(output_path)
    # os.mkdir(output_path)

    print('Start extracting...')
    # 实例化NLP(分词，词性标注，命名实体识别，依存句法分析)
    nlp = NLP()
    num = 1  # 知识三元组

    with open(input_path, 'r', encoding='utf-8') as f_in:
        # 分句，获得句子列表
        origin_sentences = re.split('[。？！；]|\n', f_in.read())
        # 遍历每一篇文档中的句子
        for origin_sentence in origin_sentences:
            if " " in origin_sentence:
                origin_sentence = re.sub(" ", "", origin_sentence)
            # 原始句子长度小于6，跳过
            if (len(origin_sentence) < 6):
                continue
            print('*****')
            # print(origin_sentence)
            # 分词处理
            lemmas = nlp.segment(origin_sentence)
            # 词性标注
            words_postag = nlp.postag(lemmas)
            #print(words_postag)

            # 命名实体识别
            words_netag = nlp.netag(words_postag)
            # 依存句法分析
            sentence = nlp.parse(words_netag)
            #print("ieguo:",sentence.to_string())

            extractor = Extractor()
            num = extractor.extract(origin_sentence, sentence, output_path, num)
