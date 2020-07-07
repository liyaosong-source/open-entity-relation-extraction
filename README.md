
# 基于依存句法分析，实现面向开放域文本的知识三元组抽取（实体和关系抽取）及知识库构建。


## 自己完成的代码(原基础上做了修改)

code/demo/extract_demo.py

code/core/nlp.py

code/core/extract.py


## Project Structure

```
knowledge_extraction/
|-- code/  # code directory
|   |-- bean/
|   |-- core/
|   |-- demo/  # procedure entry
|   |-- tool/
|-- data/ # data directory
|   |-- input_text.txt  # input text file
|   |-- knowledge_triple.json  # output knowledge triples file
|-- model/  # ltp models, can be downloaded from http://ltp.ai/download.html, select ltp_data_v3.4.0.zip
|-- resource  # dictionaries dirctory
|-- requirements.txt  # dependent python libraries
|-- README.md  # project description
```

## Requirements

This repo was tested on Python 3.5+. The requirements are:

- jieba>=0.39
- pyltp>=0.2.1

## Quickstart

```shell
cd ./code/demo/
python extract_demo.py
```
##result

见 test_knowledge_triple.json

例：

{"编号": 1, "句子": "云南省高级人民法院审判员郭婷婷认真学习着二中全会公报", "知识": ["郭婷婷", "认真学习", "二中全会公报"]}


{"编号": 3, "句子": "腾讯公司董事长杜兴明1996年在肯德基吃饭", "知识": ["杜兴明", "吃饭", "肯德基"]}
