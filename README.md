    2020.05.21
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
    
    
    所以接下来的想法如下：
    1.定位句子：先切分阅读内容，并标注答案所在的句子（第几个句子）。见location&mark
