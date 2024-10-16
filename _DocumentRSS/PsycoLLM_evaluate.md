# 各模型对比

| 模型名称                                                  | 回答质量(0~10评分,越大质量越高) | 备注                                                         |
| --------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------ |
| prompt+qwen-max                                           | 6~7                             | 比较像人，但最大的问题是当聊天轮数到达20附近的时候会出现一些重复的内容。 |
| MindChat-Baichuan-13B                                     | 4.5                             | 回复格式是共情+提建议，而且生成文本很长（100以上），让人看不下去。 |
| mechat                                                    | 5                               | 回复格式是共情+提建议，但生成文本长度不会太长。              |
| soul chat2.0                                              | 8                               | 未自行组织实验测试，该评分仅参考了官方样例。                 |
| emoLLM                                                    |                                 |                                                              |
| [emohaa](https://github.com/LLM-Red-Team/emohaa-free-api) |                                 |                                                              |

# Mind Chat

## 开发机构

华东理工大学

## 开源链接

## https://modelscope.cn/models/X-D-Lab/MindChat-Qwen-7B-v2

## 特色

MindChat能以更加**共情**、**引导**的方式与用户**沟通**，区别于各自竞品所表现出的“问答”方式。

## 模型版本

模型名称合并后的权重MindChat-Qwen-7B[ModelScope](https://modelscope.cn/models/X-D-Lab/MindChat-Qwen-7B-v2/summary) / [HuggingFace](https://huggingface.co/X-D-Lab/MindChat-Qwen-7B-v2) / OpenXLabMindChat-InternLM-7B[ModelScope](https://modelscope.cn/models/X-D-Lab/MindChat-7B/summary) / [HuggingFace](https://huggingface.co/X-D-Lab/MindChat-7B) / [OpenXLab](https://openxlab.org.cn/models/detail/thomas-yanxin/MindChat-InternLM-7B)MindChat-Baichuan-13B[ModelScope](https://modelscope.cn/models/X-D-Lab/MindChat-Baichuan-13B/summary) / [HuggingFace](https://huggingface.co/X-D-Lab/MindChat-baichuan-13B) / OpenXLab

## 数据来源

采用了经过人工清洗的约20万条的高质量多轮心理对话数据进行训练, 涵盖工作、家庭、学习、生活、社交、安全等多个方面。

开源链接中给出的部分训练数据链接失效，获取不到他的训练数据，并且也没有更多数据集构建的信息。

## 效果

轮数用户MindChat1总感觉自己学习很差, 想努力, 但是又控制不住想玩游戏我明白你的感受, 你觉得自己学习不好, 但是总是控制不住想玩游戏. 我想问问你, 你玩游戏的时候是什么感觉呢? 有没有什么特别喜欢的游戏?2我平常特别喜欢玩一些端游来打发时间, 玩游戏的时候很纠结, 明明自己成绩落后, 学习任务还没完成但还是想玩我明白你的感受. 你可能需要认真思考一下, 玩游戏对你来说是不是真的值得投入这么多时间和精力. 学习落后是很正常的事情, 但不要让游戏成为你逃避现实的工具. 你可以尝试制定一个计划, 把玩游戏的时间留给自己, 同时也要合理分配学习任务, 让自己更加充实.3在学习上总感觉自己学的很吃力, 不知道该怎么办, 觉得自己学习能力太差了, 心里很失落我理解你的感受. 每个人的学习能力都是不同的, 不要过分苛求自己. 你可以先尝试找到适合自己的学习方法, 比如寻找学习伙伴, 向老师请教, 或者参加一些学习小组. 同时, 也不要忘记给自己一些休息的时间, 保持身心健康. 学习是一个长期的过程, 不要过于急躁, 慢慢来, 你会越来越好的.4我确实不该把精力都是投入在游戏这些娱乐上, 但是我已经落后很多了, 我现在再去开始学习, 以我这么差的学习能力我还有机会学好吗虽然你现在的学习状态很糟糕, 但并不是没有机会. 学习是一个长期的过程, 只要你持之以恒, 坚持不懈, 就一定会有所进步. 同时, 也不要忘记, 学习的过程也需要一定的动力和动机. 你可以找一些自己感兴趣的学习方向, 或者设定一些小目标, 让自己更有动力去完成. 不要轻易放弃, 相信自己, 你一定可以做到.5可是我很焦虑, 以前落后太多了, 现在不知道从哪里开始焦虑是很正常的情绪, 不要害怕它. 你可以先想想自己目前的学习状态, 列出自己需要学习的科目和内容, 然后按照优先级和难易程度进行排序. 接着, 你可以尝试分解每个科目和内容, 把它们分成小目标, 一步一步地去完成. 这样, 你就可以更有针对性地进行学习, 不会感到太紧张和不知所措. 同时, 也不要忘记给自己一些奖励, 比如看一部电影, 吃一顿美食等等, 让自己更有动力去完成目标.6也就是我现在主要的问题是太焦虑了是吗? 我只要好好的去做, 成绩还是可以提高的对吗是的, 焦虑是一种很常见的情绪, 它会让你感到很不安, 但是它并不会影响你真正地提高成绩. 你可以试着把焦虑的情绪转化成动力, 让它成为你学习的一部分. 同时, 也不要忘记给自己一些时间, 不要过分压抑自己的情绪, 让自己保持一个积极的心态. 只要你持之以恒, 相信自己, 你一定可以取得更好的成绩.7非常谢谢你, 我会好好努力的我不用客气, 我很高兴能帮到你. 我相信你一定可以克服困难, 取得好成绩. 加油! 如果有任何需要帮助的地方, 随时都可以找我聊天.

以上是MindChat-Baichuan-13B的部分测试对话案例，更多对话案例可以在https://modelscope.cn/models/X-D-Lab/MindChat-Baichuan-13B中找到。

对话案例存在以下问题：

1、一轮对话中提的问题太多。比如第1轮对话中，问了两个问题，这是两个可以挖掘的方向，应该先问其中一个问题，等待这个问题相关信息挖掘完毕后再问出第二个问题。

2、回答过于偏向于帮助用户解决问题。心理咨询应该是先安抚情绪，最后再提出问题解决方案，上面模型的回复基本都在教用户怎么解决问题，这是会容易引起用户反感的。

# Soul Chat2.0

## 开发机构

华南理工大学未来技术学院-广东省数字孪生人重点实验室

## 链接

| 模型名字                            | 地址                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| YIRONGCHEN/SoulChat2.0-Llama-3-8B   | https://modelscope.cn/models/YIRONGCHEN/SoulChat2.0-Llama-3-8B |
| YIRONGCHEN/SoulChat2.0-Qwen2-7B     | https://modelscope.cn/models/YIRONGCHEN/SoulChat2.0-Qwen2-7B |
| YIRONGCHEN/SoulChat2.0-Llama-3.1-8B | https://modelscope.cn/models/YIRONGCHEN/SoulChat2.0-Llama-3.1-8B |

## 数据

https://modelscope.cn/datasets/YIRONGCHEN/PsyDTCorpus

有4760个多轮对话数据，字数在2500万左右，质量尚可。

## 效果

![img](https://nkux9tib08.feishu.cn/space/api/box/stream/download/asynccode/?code=OTY4ZjY2YzRhYzhhOGY1YzYzYmNiYjMwZTM2ZWY4NjdfczBKUHVHMWNSNHNxYldNZTNja0pQR0hxU2RHa2k2RXpfVG9rZW46TTV4UGI5MnlXb0xpUVd4UVhFbGNuZm5DbnpoXzE3MjkwODg3NDE6MTcyOTA5MjM0MV9WNA)

# 灵心（Soul Chat1.0）

## 链接

https://modelscope.cn/studios/YIRONGCHEN/SoulChat

## 数据

https://modelscope.cn/datasets/YIRONGCHEN/SoulChatCorpus

质量较差，数据集中模型的回答不如prmopt+qwen-max的，但是数据量比较大，包含258354个多轮对话，总共1517344轮。

## 效果

作者的接口没搭好，无法验证，效果应该不会太好，因为他的训练数据质量比较差。

# Emo LLM

## 链接

体验：https://aistudio.baidu.com/community/app/63335/webUI

模型：https://modelscope.cn/models/chg0901/EmoLLM-Llama3-8B-Instruct3.0

## 数据

没有开源训练数据

## 效果

（后续更新）

# Me Chat

## 开发机构

浙江大学

## 链接

模型：https://huggingface.co/qiuhuachuan/MeChat

论文：https://arxiv.org/pdf/2305.00450

## 数据

![img](https://nkux9tib08.feishu.cn/space/api/box/stream/download/asynccode/?code=MmQ3ODM1M2I2ZTExY2M3N2NiOGNhNmI5NTgzZGZiYTlfV3NGWHZHVXFEUTQxZ0FRQXN1bUJSMld0MFY3RlJjUUxfVG9rZW46V1N1TmJwemw0b0RVSzF4T3NLYmNHTmpNbmNnXzE3MjkwODg3NDE6MTcyOTA5MjM0MV9WNA)

论文中提到了一种名为smile的数据集构建方法，核心想法是重写单论对话构建的数据，并给出了一些数据清洗的技巧。

问题提问：太差。

## 效果：

![img](https://nkux9tib08.feishu.cn/space/api/box/stream/download/asynccode/?code=YWZiNDllYWVjYjBiY2QzM2NlODhiZWMzNjMwYzdiMTZfWDduellxRTVYVzJSMWdFZ0ZwemI4SzJaWWloM3ZxNW9fVG9rZW46Wm9PTGJVYTNVb090RWx4SkhiMmNVVjRXbkY5XzE3MjkwODg3NDE6MTcyOTA5MjM0MV9WNA)

咨询师还是比较像ai，它一直在给建议，但是生成文本的长度不算太长，这一点是可取的。

# 巧板

## 开发机构

哈工大社会计算与信息检索研究中心（SCIR)情感计算组

## 链接

https://github.com/HIT-SCIR-SC/QiaoBan/blob/main/data/child_chat_100.json

## 数据

https://github.com/HIT-SCIR-SC/QiaoBan/blob/main/data/child_chat_100.json

100条生成数据，主要关于儿童心理陪伴的。