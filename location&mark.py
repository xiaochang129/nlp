# coding=utf-8
# Copyright 2020 The Xiao AI Team Authors.
#
#本段为经典函数，对英文段落进行分句。
#需要注意的是引号的优先级最高。
#1.先打印一下squad的句子看下
#the structure of squad context is
# {version:,data:[,{title:,paragraphs:[,{qas:[,{question:,
#                                              id:,
#                                              answers:[,{text:,answer_start:},]},
#                                              is_impossible:False
#                                              plausible_answers:[]],
#                                       context:"正文"},
#                                      ]
#                   },
#                 ]
# }


class ReadData(object):
    def __init__(self, path):
        self.path = path
        self.data = json.load(open(self.path, "r"))

    def context(self):
        context = ""
        print(len(self.data["data"]))
        for i in range(len(self.data["data"])):
            print(i)
            for j in range(len(self.data["data"][i]["paragraphs"])):
                context +="\n"+ self.data["data"][i]["paragraphs"][j]["context"]
        return context


if __name__ == "__main__":
    import json
    path2 = "D:\\算法工程师\\0.个人介绍与项目介绍\\nlp\\SQUAD\\train-v2.0.json"
    file = ReadData(path2)
    f=open("D:\\算法工程师\\0.个人介绍与项目介绍\\nlp\\SQUAD\\context.txt","w",encoding='utf-8')
    f.write(file.context())
