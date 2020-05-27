#  2020.05.21
    今天突发奇想，用github来跟踪一下自己的这几年的职业生涯，特别是解决nlp的问题。
    nlp的基本脉络：
      1.早先基于句法分析等语言学逻辑上的处理。
      2.w2v，lstm出来之后的引入语言相关性、序列性的信息的处理。
      3.2018年bert出现之后引领的transform方法（坐标表示）的数学逻辑引起的语言相关的底层逻辑更新。这里不同于lstm用模型结构来表现语序，而是用词序向量的方式。
      4.以致最新albert。借鉴百度ernie的连续词屏蔽预测、借鉴卷积网络的“因式分解”，借鉴又创新改造卷积网络的不同层参数共享，以及上下句的预测。

    最有趣的问题当然是squad，中国英语高中阅读理解；我想起来了我小学时候我爸经过我们县图书馆发现的英语补习班，由此开启了小江老师给我补习英语的六七年时光，县图书馆、她在北门的家（去她家必须要经过一个完全漆黑的走道），她在六中后面西门的家，她大着肚子的新苗幼儿园，因为喜欢丰寅而跟我们一起补习英语的夏毛，还有我妈以带来了好几个学生为由，便宜了我五十块的学费，我爸妈这部分另外再讲了，太多有趣的事了，哈哈哈哈哈

    我2019年中和两位同事一起处理过类似squad的问题，当时是直接采用别人写的pytorch改的，改动有限，效果一般；但理解了squad的基本逻辑：按长度将阅读内容切片，和问题组成句子，预测答案在阅读内容的起始位置和终止位置。
    这次我准备换个思路，先定位到句子，然后再找到答案位置。
    1.定位句子：通过文本相似来锁定答案所在句子。观察没有答案的问题是否有区分度。
    2.找到答案，通过预测0、1来定位答案，有答案的位置预测值为1，不是答案的位置预测值为0.
    
   
 # squad
 一、定位句子
    
    先切分阅读内容，并标注答案所在的句子（第几个句子）。见location&mark。已完成。
    发现问题：1.引号内可能出现句子，需把引号内当成一个词，不做切割。
             2.学到了pep8规范，学到了squad的问答句格式。
             3.检查一个问题的所有答案是否都在同一句中：train-v2.0.json一问一答，dev-2.0.json一问多答。
             4.问题有特点： when,who，what+指定词。所以词性很重要。
             
 二、baseline效果（05.25）
    
    固有的albert处理squad结果跑出来结果如何？
    
 三、尝试预测改为0,1（05.25）
 
 四、分析问题、答案词性与问题答案相似度（05.25）  
    
# 2019年的cal阅读理解冠军方案：
    模型图：    
![Image text](https://raw.githubusercontent.com/xiaochang129/nlp/master/image/calsquad.jpg)

结构：

    bert+词性特征
    highway layers(类似残差短连接)
    双向GRU
    多层感知机
    start pro ,end pro   第一个位置预测不可回答，第二个位置预测yes,第三个位置预测no
数据增强方案

     1.基于全部民事/刑事文书/去年法研杯数据fine-tune。效果有很大提升。
     2.在不可回答问题上，通过命名实体识别来替换人名/地名/交换问题位置增加数据量。
     3.在可回答问题上，通过seq2seq模型生成更多类似问题。
阈值调整

    在竞赛中，通过调整是否可回答的阈值解决不平衡数据集的问题。
数据处理方案

    实际中，将刘x6这种统一替换成刘甲这种情况。方便训练。
    
    
    
            
# 文本分类
#关于文本分类的一种方法（2020.05.22）
 
    使用lstm来提取行特征，
    跟其他行交互（attention/lstm/bilstm等），concate行位置特征
    可以再bilstm行特征
    softmax
#我的方法优化

    思路1.bilstm的多页输出，样本平衡，更多特征提取：本页字数、篇幅，查看
    
    思路2：采用单页分类，根据单页确定是否是头单页、中尾页的特点，采用上页的尾部空白大小、字多少，本页特点（头几行的字多少，空白大小），下部区域空白多少，下页头几行特点，空白大小。
