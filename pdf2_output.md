# LLM for CARE：理论框架

## 目录
- [引言](#引言)
- [页面内容](#页面内容)
- [参考文献](#参考文献)
- [图片](#图片)

## 引言
本文档提取自 理论框架，包含相关理论框架或论文整理信息。

## 页面内容

### 第 1 页
评论（3） 理论框架\_LLMForCARE（基于BDI意图 模型） 嵌⼊BDI理论的CARE模型场景 演讲版本 ⼈机交互的不同模式：


| 评论（3） 理论框架_LLMForCARE（基于BDI意图 模型） 嵌⼊BDI理论的CARE模型场景 演讲版本 ⼈机交互的不同模式： | 评论（3） |
| --- | --- |
|  |  |



### 第 2 页
指令交互、⽣成式交互、主动式交互➡根本⽬标：为⼈类服务 要什么服务（意图）、为什么要（需求） Price在1990年研究中介绍了ATIS（AirTravelInformationService）数据集，这是⾸个 ⼴泛使⽤的意图识别和槽填充数据集，包含航空领域的⽤⼾查询（如“找⻜往波⼠顿的航 班”）。论⽂定义了「意图识别」为从语⾳输⼊中提取⽤⼾⽬标的任务，并提出了基于规 则的⾃然语⾔理解（NLU）系统。  H90-1020.pdf 2000年代初，随着统计和机器学习的发展，意图识别被重新定义为分类任务，强调从输 ⼊特征到意图标签的映射。  optimizing-svms-for-complex-call-classification.pdf 意图识别的意图VS.BDI意图模型的意图VS.⽤⼾需求 • 意图识别的意图：从⽤⼾显性输⼊（如语⾳、⽂本、⾏为）中直接解析出的、原⼦化 的短期⽬标，通常对应具体的操作指令或服务请求。 • BDI意图模型的意图：智能体（Agent）基于⾃⾝信念（Belief）和愿望（Desire）， 通过理性推理⽣成的、可承诺执⾏的内部⽬标，反映智能体的⾃主决策能⼒。 • 需求（⼼理学）：指个体为满⾜⽣理（⻝物）、⼼理（⾃尊）或社会⽬标（权⼒）⽽ 产⽣的内在动机或渴望。 • ⽤⼾需求：⽤⼾希望解决的实际问题或期望达到的终极⽬标，可能是显性的（直接表 达）或隐性的（需推理挖掘）。 BDI模型源⾃哲学和认知科学中的理性主体理论，最早由Bratman在1987年于 《Intention,Plans,andPracticalReason》中提出，⽤于描述⼈类决策过程，并阐述了 意图作为理性⾏为的核⼼，认为⼈类⾏为由三个核⼼⼼理状态驱动：


| 指令交互、⽣成式交互、主动式交互➡根本⽬标：为⼈类服务 要什么服务（意图）、为什么要（需求） Price在1990年研究中介绍了ATIS（AirTravelInformationService）数据集，这是⾸个 ⼴泛使⽤的意图识别和槽填充数据集，包含航空领域的⽤⼾查询（如“找⻜往波⼠顿的航 班”）。论⽂定义了「意图识别」为从语⾳输⼊中提取⽤⼾⽬标的任务，并提出了基于规 则的⾃然语⾔理解（NLU）系统。  H90-1020.pdf 2000年代初，随着统计和机器学习的发展，意图识别被重新定义为分类任务，强调从输 ⼊特征到意图标签的映射。  optimizing-svms-for-complex-call-classification.pdf 意图识别的意图VS.BDI意图模型的意图VS.⽤⼾需求 • 意图识别的意图：从⽤⼾显性输⼊（如语⾳、⽂本、⾏为）中直接解析出的、原⼦化 的短期⽬标，通常对应具体的操作指令或服务请求。 • BDI意图模型的意图：智能体（Agent）基于⾃⾝信念（Belief）和愿望（Desire）， 通过理性推理⽣成的、可承诺执⾏的内部⽬标，反映智能体的⾃主决策能⼒。 • 需求（⼼理学）：指个体为满⾜⽣理（⻝物）、⼼理（⾃尊）或社会⽬标（权⼒）⽽ 产⽣的内在动机或渴望。 • ⽤⼾需求：⽤⼾希望解决的实际问题或期望达到的终极⽬标，可能是显性的（直接表 达）或隐性的（需推理挖掘）。 BDI模型源⾃哲学和认知科学中的理性主体理论，最早由Bratman在1987年于 《Intention,Plans,andPracticalReason》中提出，⽤于描述⼈类决策过程，并阐述了 意图作为理性⾏为的核⼼，认为⼈类⾏为由三个核⼼⼼理状态驱动： |  |
| --- | --- |



### 第 3 页
• 信念(Belief):个体对世界的认知和理解 • 愿望(Desire):个体希望达到的⽬标状态 • 意图(Intention):为实现⽬标⽽承诺执⾏的⾏动计划 1991年，美国计算机科学家与认知科学家MichaelP.Georgeff、澳⼤利亚计算机科学家 AnandS.Rao⾸次将BDI理论形式化为AI中的智能体架构，提出了基于逻辑的BDI模型， ⽤于模拟和实现智能体（agents）的主动推理过程。  ModelingRationalAgentswithinaBDI-Architecture.pdf 具有共情的负责任、可以促进⼈⼼智提升的⼼理⼤模型 CARE初版 安全地 共情（Empathy）地为⼈类实现⽬标 主体与外界相处： 主体与环境 主体与客体（他⼈/社会） 主体与⾃⼰ 主体=⼈：视、听、嗅、味、触 主体=机器：视、听、触、环境信息（时间、空间等）、上下⽂ ⽤⼾画像：⽣理特征、⼼理特征、社会特征 过滤系统：意图信号？过滤原则 《MGC:AModalMappingCouplingandGate-DrivenContrastive LearningApproachforMultimodalIntentRecognition》 信号？过滤原则 • 来源:ScienceDirect,2025 骆家怡 5⽉14⽇17:36 • 链接:https://www.sciencedirect.com/science/article/pii/S003132032400734X[] 什么过滤原则？意图信号的定义 (https://www.sciencedirect.com/science/article/abs/pii/S0957417425012539) ⻆⾊库A：原始⻆⾊设定 信念库（belief）：环境信息（上下⽂等）、⽤⼾信息（不包含⽤⼾画像）和智能体⾃⾝ 信息（⾃⾝⻆⾊设定）的集合 原始⻆⾊设定  骆家怡 5⽉14⽇17:37 定义⼀个⻆⾊需要包含哪些信息 愿望（desire）：想要实现的⽬标 ⽤⼾需求：⽤⼾画像+信念库（belief），⽤⼾在特定情境下基于⽣理、⼼理和社会因素 所表达或隐含的期望、⽬标或问题解决的需求。期望达到的⽬标（显性、隐性）


| • 信念(Belief):个体对世界的认知和理解 • 愿望(Desire):个体希望达到的⽬标状态 • 意图(Intention):为实现⽬标⽽承诺执⾏的⾏动计划 1991年，美国计算机科学家与认知科学家MichaelP.Georgeff、澳⼤利亚计算机科学家 AnandS.Rao⾸次将BDI理论形式化为AI中的智能体架构，提出了基于逻辑的BDI模型， ⽤于模拟和实现智能体（agents）的主动推理过程。  ModelingRationalAgentswithinaBDI-Architecture.pdf 具有共情的负责任、可以促进⼈⼼智提升的⼼理⼤模型 CARE初版 安全地 共情（Empathy）地为⼈类实现⽬标 主体与外界相处： 主体与环境 主体与客体（他⼈/社会） 主体与⾃⼰ 主体=⼈：视、听、嗅、味、触 主体=机器：视、听、触、环境信息（时间、空间等）、上下⽂ ⽤⼾画像：⽣理特征、⼼理特征、社会特征 过滤系统：意图信号？过滤原则 《MGC:AModalMappingCouplingandGate-DrivenContrastive LearningApproachforMultimodalIntentRecognition》 信号？过滤原则 • 来源:ScienceDirect,2025 骆家怡 5⽉14⽇17:36 • 链接:https://www.sciencedirect.com/science/article/pii/S003132032400734X[] 什么过滤原则？意图信号的定义 (https://www.sciencedirect.com/science/article/abs/pii/S0957417425012539) ⻆⾊库A：原始⻆⾊设定 信念库（belief）：环境信息（上下⽂等）、⽤⼾信息（不包含⽤⼾画像）和智能体⾃⾝ 信息（⾃⾝⻆⾊设定）的集合 原始⻆⾊设定  骆家怡 5⽉14⽇17:37 定义⼀个⻆⾊需要包含哪些信息 愿望（desire）：想要实现的⽬标 ⽤⼾需求：⽤⼾画像+信念库（belief），⽤⼾在特定情境下基于⽣理、⼼理和社会因素 所表达或隐含的期望、⽬标或问题解决的需求。期望达到的⽬标（显性、隐性） | 信号？过滤原则 骆家怡 5⽉14⽇17:36 什么过滤原则？意图信号的定义 原始⻆⾊设定 骆家怡 5⽉14⽇17:37 定义⼀个⻆⾊需要包含哪些信息 |
| --- | --- |



### 第 4 页
认知系统：⽬标优先级（艾森豪威尔） 意图资源库（intentions）：⼀系列的⽂本、语⾳、动作 ⻆⾊库B：⼀系列可以扮演的⻆⾊信息 反馈信息库：视、听、触、环境信息（时间、空间等） 列可以扮演的⻆⾊信息 ⾃我决定理论（Self-DeterminationTheory,SDT）是由⼼理学家RichardM.Ryan和 骆家怡 5⽉14⽇17:54 EdwardL.Deci提出的⼀种关于⼈类动机和⼈格的理论，⾸次系统阐述于2000年的论⽂ 定义⼀个⻆⾊需要包含哪些信 息？需要多少数量的⻆⾊？ 《Self-DeterminationTheoryandtheFacilitationofIntrinsicMotivation,Social Development,andWell-Being》（AmericanPsychologist,55(1),68-78）。SDT聚焦 于⼈类⾏为的动机来源，强调内在动机（IntrinsicMotivation）和⼼理需求对个体⾏为、 ⼼理健康和幸福感的作⽤。SDT的核⼼假设是，⾃主性（Autonomy）、能⼒ （Competence）、关联（Relatedness）是⼈类普遍的⼼理需求，适⽤于不同⽂化、 年龄、性别和场景（Ryan&Deci,2000）。  ryan2000.pdf SDT提出三种基本⼼理需求，是⼈类动机和⼼理健康的基⽯： 1. ⾃主性（Autonomy）：个体感到⾏为的⾃主性和⾃我控制，⾏动基于内在价值或兴 趣，⽽⾮外部压⼒或控制。 ◦ ⽰例：在学习中，学⽣因对知识的兴趣⽽⾃发学习（⾃主性⾼），⽽⾮仅为考试 分数（⾃主性低）。 ◦ 作⽤：满⾜⾃主性需求增强内在动机，促进⾏为坚持和⼼理满⾜。 ◦ 反例：过度控制（如强制任务）削弱⾃主性，导致动机下降或⼼理压⼒。 2. 能⼒（Competence）： ◦ 定义：个体感到能够有效完成任务、应对挑战或掌握技能，体验⾃我效能。 ◦ ⽰例：学⽣通过练习掌握数学公式，感到能⼒提升。 ◦ 作⽤：满⾜能⼒需求增强信⼼和成就感，推动个体追求新挑战。 ◦ 反例：任务过难或缺乏反馈可能挫败能⼒感，导致放弃。 3. 关联（Relatedness）： ◦ 定义：个体渴望与他⼈（或系统）建⽴有意义的情感连接，体验归属感、被理解 和⽀持。 ◦ ⽰例：学⽣在学习⼩组中感到被⽀持，建⽴归属感。 ◦ 作⽤：满⾜关联需求促进情感健康和社会连接，增强动机和幸福感。 ◦ 反例：孤独或缺乏⽀持可能导致情绪低落或疏离感。 5.13更新版（整理给AI） 我的理论框架是基于BDI模型的意图识别框架（经典的智能体理论），旨在通过⼈⼯智能 实现对⼈类意图的精准识别，并⽣成共情、安全且可以帮助⼈类实现⽬标（包含任务导向 ⽬标、情感导向⽬标、⼼理导向⽬标及个性化导向⽬标）的输出。这是我对于未来⼈机交


| 认知系统：⽬标优先级（艾森豪威尔） 意图资源库（intentions）：⼀系列的⽂本、语⾳、动作 ⻆⾊库B：⼀系列可以扮演的⻆⾊信息 反馈信息库：视、听、触、环境信息（时间、空间等） 列可以扮演的⻆⾊信息 ⾃我决定理论（Self-DeterminationTheory,SDT）是由⼼理学家RichardM.Ryan和 骆家怡 5⽉14⽇17:54 EdwardL.Deci提出的⼀种关于⼈类动机和⼈格的理论，⾸次系统阐述于2000年的论⽂ 定义⼀个⻆⾊需要包含哪些信 息？需要多少数量的⻆⾊？ 《Self-DeterminationTheoryandtheFacilitationofIntrinsicMotivation,Social Development,andWell-Being》（AmericanPsychologist,55(1),68-78）。SDT聚焦 于⼈类⾏为的动机来源，强调内在动机（IntrinsicMotivation）和⼼理需求对个体⾏为、 ⼼理健康和幸福感的作⽤。SDT的核⼼假设是，⾃主性（Autonomy）、能⼒ （Competence）、关联（Relatedness）是⼈类普遍的⼼理需求，适⽤于不同⽂化、 年龄、性别和场景（Ryan&Deci,2000）。  ryan2000.pdf SDT提出三种基本⼼理需求，是⼈类动机和⼼理健康的基⽯： 1. ⾃主性（Autonomy）：个体感到⾏为的⾃主性和⾃我控制，⾏动基于内在价值或兴 趣，⽽⾮外部压⼒或控制。 ◦ ⽰例：在学习中，学⽣因对知识的兴趣⽽⾃发学习（⾃主性⾼），⽽⾮仅为考试 分数（⾃主性低）。 ◦ 作⽤：满⾜⾃主性需求增强内在动机，促进⾏为坚持和⼼理满⾜。 ◦ 反例：过度控制（如强制任务）削弱⾃主性，导致动机下降或⼼理压⼒。 2. 能⼒（Competence）： ◦ 定义：个体感到能够有效完成任务、应对挑战或掌握技能，体验⾃我效能。 ◦ ⽰例：学⽣通过练习掌握数学公式，感到能⼒提升。 ◦ 作⽤：满⾜能⼒需求增强信⼼和成就感，推动个体追求新挑战。 ◦ 反例：任务过难或缺乏反馈可能挫败能⼒感，导致放弃。 3. 关联（Relatedness）： ◦ 定义：个体渴望与他⼈（或系统）建⽴有意义的情感连接，体验归属感、被理解 和⽀持。 ◦ ⽰例：学⽣在学习⼩组中感到被⽀持，建⽴归属感。 ◦ 作⽤：满⾜关联需求促进情感健康和社会连接，增强动机和幸福感。 ◦ 反例：孤独或缺乏⽀持可能导致情绪低落或疏离感。 5.13更新版（整理给AI） 我的理论框架是基于BDI模型的意图识别框架（经典的智能体理论），旨在通过⼈⼯智能 实现对⼈类意图的精准识别，并⽣成共情、安全且可以帮助⼈类实现⽬标（包含任务导向 ⽬标、情感导向⽬标、⼼理导向⽬标及个性化导向⽬标）的输出。这是我对于未来⼈机交 | 列可以扮演的⻆⾊信息 骆家怡 5⽉14⽇17:54 定义⼀个⻆⾊需要包含哪些信 息？需要多少数量的⻆⾊？ |
| --- | --- |



### 第 5 页
互的思考，⽬标是让机器不仅能理解⼈类的需求、主动识别⼈类意图，还能以贴⼼的⽅式 主动提供帮助。 我会从框架结构、核⼼模块、模块逻辑三个部分进⾏阐述我的理论框架： 1、框架结构：包含输⼊端、处理/思考过程、输出端。 输⼊：感知信息库（视觉、听觉、触觉） 处理/思考过程：过滤/处理/思考过程系统 输出：⼀系列执⾏⽅案（⽂本、语⾳、动作） 2、核⼼模块： 感知信息库（输⼊模块）：多模态数据采集和预处理系统。包括视觉（图像、视频）、听 觉（语⾳、⾳调）、触觉（触控反馈、压⼒）、环境信息（如时间、地点）。 过滤系统：从感知信息库的原始多模态数据中筛选出⾼质量、与⽤⼾意图和情感相关的安 全数据，同时剔除⽆关、噪声或敏感信息，并确保隐私保护。固定格式：who、when、 where、what、how ⽤⼾画像库：动态存储和管理模块，⽤于收集、整理和更新⽤⼾的⽣理特征、⼼理特征及 社会特征信息。 ⻆⾊库A：原始⻆⾊设定、上⼀次⻆⾊及维持时⻓（不低于xxmin） 信念库：智能体具有的关于环境信息（上下⽂）、⽤⼾信息和智能体⾃⾝信息（⾃⾝⻆⾊ 设定）的集合。构建Agent对⽤⼾当前状态和需求的理解。 ⽤⼾需求：⽤⼾在特定情境下基于⽣理、⼼理和社会因素所表达或隐含的期望、⽬标或问 题解决的需求，通常通过多模态交互数据显性或隐性地传达。输⼊：Agent信念库的存储 数据（特征编码、⽤⼾画像、⻆⾊设定）；输出：结构化的⼀组显性需求描述、⼀组隐性 需求描述 欲望库：智能体想要实现的⽬标或状态，反映Agent的主动⽀持意图。输⼊：Agent信念 库的存储数据（特征编码、⽤⼾画像、⻆⾊设定）；输出：两组⽬标状态 认知系统：采⽤艾森豪威尔矩阵评估⽤⼾需求和desire的优先级。 第⼀象限（重要且紧急）：包含对⽤⼾当前⽬标（任务、情感、⼼理）⾄关重要且需要⽴ 即响应的desire或需求，以避免负⾯后果（如情绪恶化、健康⻛险）或抓住关键机会（如 考试成功）。通常由显性需求主导，如⽤⼾直接表达的即时需求（“我好累”“胸⼝ 痛”）。也包括⾼强度隐性需求，如强烈多模态线索（哭泣、颤抖⾳调）表明的危机性需 求（如情绪崩溃）。 第⼆象限（重要但不紧急）：需求或desire对⽤⼾⻓期⽬标（⼼理健康、学业提升、健康 管理）有显著贡献，但⽆需⽴即处理，可计划性实施。通常由隐性需求驱动的，也可能包 括显性表达的⾮紧急⻓期⽬标（如“我想改善健康”）。 第三象限（不重要但紧急）：需要快速响应但对⽤⼾核⼼⽬标（任务、情感、⼼理）贡献 较低的desire或需求，通常是次要任务或临时兴趣。可能由显性需求（如临时请求）或次 要隐性需求（如临时偏好）主导。 第四象限（不重要且不紧急）：包含对⽤⼾核⼼⽬标贡献最⼩且⽆需⽴即处理的desire或 需求，通常是背景信息、低相关性偏好或潜在兴趣。通常由隐性需求主导，涉及个性化或 ⾮核⼼⽬标。少数显性需求为⾮核⼼兴趣（如“我喜欢听⾳乐”）。 意图资源库：智能体承诺执⾏的动作或计划，是desire的具象化。最明显的性质是它将导 致⾏为，是⼀系列有序列的⾏动步骤。输⼊：根据艾森豪威尔矩阵判断排列好的需求集合 （显性、隐性）与Desire集合。输出：可执⾏的4个Plans，每个包含⽂本、动作、语⾳ 语调指令，按艾森豪威尔矩阵优先级排序 ⻆⾊库B：影响意图Intention⽣成 输出模块：⽂本、动作和语⾳，与⽤⼾互动。所有输出都经过安全校验，确保符合伦理底 线。


| 互的思考，⽬标是让机器不仅能理解⼈类的需求、主动识别⼈类意图，还能以贴⼼的⽅式 主动提供帮助。 我会从框架结构、核⼼模块、模块逻辑三个部分进⾏阐述我的理论框架： 1、框架结构：包含输⼊端、处理/思考过程、输出端。 输⼊：感知信息库（视觉、听觉、触觉） 处理/思考过程：过滤/处理/思考过程系统 输出：⼀系列执⾏⽅案（⽂本、语⾳、动作） 2、核⼼模块： 感知信息库（输⼊模块）：多模态数据采集和预处理系统。包括视觉（图像、视频）、听 觉（语⾳、⾳调）、触觉（触控反馈、压⼒）、环境信息（如时间、地点）。 过滤系统：从感知信息库的原始多模态数据中筛选出⾼质量、与⽤⼾意图和情感相关的安 全数据，同时剔除⽆关、噪声或敏感信息，并确保隐私保护。固定格式：who、when、 where、what、how ⽤⼾画像库：动态存储和管理模块，⽤于收集、整理和更新⽤⼾的⽣理特征、⼼理特征及 社会特征信息。 ⻆⾊库A：原始⻆⾊设定、上⼀次⻆⾊及维持时⻓（不低于xxmin） 信念库：智能体具有的关于环境信息（上下⽂）、⽤⼾信息和智能体⾃⾝信息（⾃⾝⻆⾊ 设定）的集合。构建Agent对⽤⼾当前状态和需求的理解。 ⽤⼾需求：⽤⼾在特定情境下基于⽣理、⼼理和社会因素所表达或隐含的期望、⽬标或问 题解决的需求，通常通过多模态交互数据显性或隐性地传达。输⼊：Agent信念库的存储 数据（特征编码、⽤⼾画像、⻆⾊设定）；输出：结构化的⼀组显性需求描述、⼀组隐性 需求描述 欲望库：智能体想要实现的⽬标或状态，反映Agent的主动⽀持意图。输⼊：Agent信念 库的存储数据（特征编码、⽤⼾画像、⻆⾊设定）；输出：两组⽬标状态 认知系统：采⽤艾森豪威尔矩阵评估⽤⼾需求和desire的优先级。 第⼀象限（重要且紧急）：包含对⽤⼾当前⽬标（任务、情感、⼼理）⾄关重要且需要⽴ 即响应的desire或需求，以避免负⾯后果（如情绪恶化、健康⻛险）或抓住关键机会（如 考试成功）。通常由显性需求主导，如⽤⼾直接表达的即时需求（“我好累”“胸⼝ 痛”）。也包括⾼强度隐性需求，如强烈多模态线索（哭泣、颤抖⾳调）表明的危机性需 求（如情绪崩溃）。 第⼆象限（重要但不紧急）：需求或desire对⽤⼾⻓期⽬标（⼼理健康、学业提升、健康 管理）有显著贡献，但⽆需⽴即处理，可计划性实施。通常由隐性需求驱动的，也可能包 括显性表达的⾮紧急⻓期⽬标（如“我想改善健康”）。 第三象限（不重要但紧急）：需要快速响应但对⽤⼾核⼼⽬标（任务、情感、⼼理）贡献 较低的desire或需求，通常是次要任务或临时兴趣。可能由显性需求（如临时请求）或次 要隐性需求（如临时偏好）主导。 第四象限（不重要且不紧急）：包含对⽤⼾核⼼⽬标贡献最⼩且⽆需⽴即处理的desire或 需求，通常是背景信息、低相关性偏好或潜在兴趣。通常由隐性需求主导，涉及个性化或 ⾮核⼼⽬标。少数显性需求为⾮核⼼兴趣（如“我喜欢听⾳乐”）。 意图资源库：智能体承诺执⾏的动作或计划，是desire的具象化。最明显的性质是它将导 致⾏为，是⼀系列有序列的⾏动步骤。输⼊：根据艾森豪威尔矩阵判断排列好的需求集合 （显性、隐性）与Desire集合。输出：可执⾏的4个Plans，每个包含⽂本、动作、语⾳ 语调指令，按艾森豪威尔矩阵优先级排序 ⻆⾊库B：影响意图Intention⽣成 输出模块：⽂本、动作和语⾳，与⽤⼾互动。所有输出都经过安全校验，确保符合伦理底 线。 |  |
| --- | --- |



### 第 6 页
反馈感知信息库：输出后所得到的⽤⼾的⽂本/语⾳/动作等的反馈信息。 3、模块逻辑 通过感知信息库收集视觉、听觉、触觉的信息，收集到的数据经过过滤系统对数据进⾏清 洗，收集到的数据同时更新⽤⼾画像库。结合过滤系统的信息、⽤⼾画像库的信息与机器 ⼈⻆⾊库A（原始的⻆⾊设定或上⼀次的⻆⾊设定）整合到agent的信念系统当中，基于 agent的信念库分析⽤⼾的需求、⽣成agent的desire，再通过agent的认知系统判断⽤⼾ 的需求优先级，⽣成⼀系列的意图资源库当中的plans。同时，也会有⼀个⻆⾊库B的信 息匹配当前的plans输出最合适的满⾜⽤⼾需求的回应。同时，输出的内容也会更新 agent的信念库和⻆⾊库A。我希望⽤过上述这个流程实现对⽤⼾的情况主动识别并提供 帮助，并且我希望机器⼈通过这个流程输出的内容是符合逻辑的、符合安全底线的、可以 促进⽤⼾⽬标完成的（包含任务导向⽬标、情感导向⽬标、⼼理导向⽬标及个性化导向⽬ 标）。 框架结构 输⼊：感知信息库（视觉、听觉、触觉） 处理/思考过程：过滤系统 输出：⼀系列执⾏⽅案（⽂本、语⾳、动作） 核⼼模块 感知信息库 过滤系统 ⽤⼾画像库 ⻆⾊库A 信念库 ⽤⼾需求 欲望 认知系统 意图资源库 ⻆⾊库B 模块逻辑 没办法下载的论⽂： 1、标题:PromptLearningforMultimodalIntentRecognitionwithModalAlignment Perception 论⽂链接：https://link.springer.com/article/10.1007/s12559-024-10328-7 摘要：多模态意图识别分析是在现实世界的多模态环境中通过语⾳、肢体动作、语调和 其他模态理解⽤⼾意图的关键任务。然⽽，由于模态内和跨模态意图的隐藏性，⼤多数现


| 反馈感知信息库：输出后所得到的⽤⼾的⽂本/语⾳/动作等的反馈信息。 3、模块逻辑 通过感知信息库收集视觉、听觉、触觉的信息，收集到的数据经过过滤系统对数据进⾏清 洗，收集到的数据同时更新⽤⼾画像库。结合过滤系统的信息、⽤⼾画像库的信息与机器 ⼈⻆⾊库A（原始的⻆⾊设定或上⼀次的⻆⾊设定）整合到agent的信念系统当中，基于 agent的信念库分析⽤⼾的需求、⽣成agent的desire，再通过agent的认知系统判断⽤⼾ 的需求优先级，⽣成⼀系列的意图资源库当中的plans。同时，也会有⼀个⻆⾊库B的信 息匹配当前的plans输出最合适的满⾜⽤⼾需求的回应。同时，输出的内容也会更新 agent的信念库和⻆⾊库A。我希望⽤过上述这个流程实现对⽤⼾的情况主动识别并提供 帮助，并且我希望机器⼈通过这个流程输出的内容是符合逻辑的、符合安全底线的、可以 促进⽤⼾⽬标完成的（包含任务导向⽬标、情感导向⽬标、⼼理导向⽬标及个性化导向⽬ 标）。 框架结构 输⼊：感知信息库（视觉、听觉、触觉） 处理/思考过程：过滤系统 输出：⼀系列执⾏⽅案（⽂本、语⾳、动作） 核⼼模块 感知信息库 过滤系统 ⽤⼾画像库 ⻆⾊库A 信念库 ⽤⼾需求 欲望 认知系统 意图资源库 ⻆⾊库B 模块逻辑 没办法下载的论⽂： 1、标题:PromptLearningforMultimodalIntentRecognitionwithModalAlignment Perception 论⽂链接：https://link.springer.com/article/10.1007/s12559-024-10328-7 摘要：多模态意图识别分析是在现实世界的多模态环境中通过语⾳、肢体动作、语调和 其他模态理解⽤⼾意图的关键任务。然⽽，由于模态内和跨模态意图的隐藏性，⼤多数现 |  |
| --- | --- |



### 第 7 页
有⽅法在挖掘和整合多模态意图信息⽅⾯仍然存在局限性。本⽂提出了⼀种基于模态对⻬ 感知的快速学习(PMAP)⽅法来应对这些挑战。⾸先，为了挖掘深层语义信息，构建意图 模板进⾏快速学习以增强⽂本表⽰。然后，利⽤跨模态对⻬感知来消除模态差异，同时从 ⾮⽂本模态中挖掘⼀致的隐藏意图信息。通过多模态语义交互，对⽂本在语义空间中的位 置进⾏微调，从⽽有效地聚合来⾃多个模态的意图细节。  PromptLearningforMultimodalIntentRecognitionwithModalAlignment Perception.pdf 2、标题:Graphandtextmulti-modalrepresentationlearningwithmomentum distillationonElectronicHealthRecords 论⽂链接：https://doi.org/10.1016/j.knosys.2024.112373 代码链接：https://github.com/deepEMR/GTMMRL 摘要：电⼦健康记录(EHR)在现代医疗保健系统中的出现和⼴泛采⽤产⽣了⼤量数据， 这些数据有可能显著改善患者的治疗效果。然⽽，由于EHR数据量巨⼤且本⾝就很复 杂，⽬前对医疗代码中隐藏的图形结构和⾮结构化⽂本之间的多模态关系的研究忽视了固 有的差异和不⼀致。为了解决这⼀重⼤差距，本⽂引⼊了⼀种预训练⽅法，称为基于电⼦ 健康记录的动量蒸馏的图形和⽂本多模态表⽰学习(GTMMRL)。这种⽅法使⽤⼤型开源 EHR数据集MIMIC-III进⾏预训练，解决了标签嘈杂且不可靠的问题。采⽤了五个精⼼挑 选的代理任务，每个任务都通过教师模型⽣成的伪⽬标来指导学⽣模型的学习，这是学⽣ 模型的指数移动平均值，从⽽减轻了过度拟合的趋势。  Graphandtextmulti-modalrepresentationlearningwithmomentumdistillation onElectronicHealthRecords.pdf 3、Self-determinationtheory:Amacrotheoryofhumanmotivation,development, andhealth. • DOI:10.1037/A0012801 • CorpusID:260685560 Deci&Ryan(2008)的后续研究扩展了SDT的应⽤，证明需求满⾜在⼯作、教育、健康 和休闲场景中的⼀致性，⽀持框架的泛化⽬标。  Self-determinationtheory-Amacrotheoryofhumanmotivation,development, andhealth.pdf 4、Ntoumanis,N.,Ng,J.Y.Y.,Prestwich,A.,Quested,E.,Hancox,J.E.,Thøgersen- Ntoumani,C.,Deci,E.L.,Ryan,R.M.,Lonsdale,C.,&Williams,G.C.(2021).Ameta- analysisofself-determinationtheory-informedinterventionstudiesinthehealth domain:Effectsonmotivation,healthbehavior,physical,andpsychologicalhealth. HealthPsychologyReview,15(2),214‒244 回顾了基于SDT的健康领域⼲预研究，分析了⾃主性、能⼒和关联需求满⾜对动机、健 康⾏为、⼼理健康和⽣理健康的影响。研究发现，SDT⼲预在健康领域（如吸烟戒断、 体重控制、体育活动）中⼀致促进⾃主动机和健康⾏为（p.216）。  Ameta-analysisofself-determinationtheory-informedinterventionstudiesin thehealthdomain-effectsonmotivation,healthbehavior,physical,and psychologicalhealth.pdf 5、Vansteenkiste,M.,Niemiec,C.P.,&Soenens,B.(2010).Thedevelopmentofthe fivemini-theoriesofself-determinationtheory:Anhistoricaloverview,emerging trends,andfuturedirections.InT.C.Urdan&S.A.Karabenick(Eds.),TheDecade Ahead:TheoreticalPerspectivesonMotivationandAchievement(Advancesin MotivationandAchievement,Vol.16)(pp.105‒165).EmeraldGroupPublishing Limited.


| 有⽅法在挖掘和整合多模态意图信息⽅⾯仍然存在局限性。本⽂提出了⼀种基于模态对⻬ 感知的快速学习(PMAP)⽅法来应对这些挑战。⾸先，为了挖掘深层语义信息，构建意图 模板进⾏快速学习以增强⽂本表⽰。然后，利⽤跨模态对⻬感知来消除模态差异，同时从 ⾮⽂本模态中挖掘⼀致的隐藏意图信息。通过多模态语义交互，对⽂本在语义空间中的位 置进⾏微调，从⽽有效地聚合来⾃多个模态的意图细节。  PromptLearningforMultimodalIntentRecognitionwithModalAlignment Perception.pdf 2、标题:Graphandtextmulti-modalrepresentationlearningwithmomentum distillationonElectronicHealthRecords 论⽂链接：https://doi.org/10.1016/j.knosys.2024.112373 代码链接：https://github.com/deepEMR/GTMMRL 摘要：电⼦健康记录(EHR)在现代医疗保健系统中的出现和⼴泛采⽤产⽣了⼤量数据， 这些数据有可能显著改善患者的治疗效果。然⽽，由于EHR数据量巨⼤且本⾝就很复 杂，⽬前对医疗代码中隐藏的图形结构和⾮结构化⽂本之间的多模态关系的研究忽视了固 有的差异和不⼀致。为了解决这⼀重⼤差距，本⽂引⼊了⼀种预训练⽅法，称为基于电⼦ 健康记录的动量蒸馏的图形和⽂本多模态表⽰学习(GTMMRL)。这种⽅法使⽤⼤型开源 EHR数据集MIMIC-III进⾏预训练，解决了标签嘈杂且不可靠的问题。采⽤了五个精⼼挑 选的代理任务，每个任务都通过教师模型⽣成的伪⽬标来指导学⽣模型的学习，这是学⽣ 模型的指数移动平均值，从⽽减轻了过度拟合的趋势。  Graphandtextmulti-modalrepresentationlearningwithmomentumdistillation onElectronicHealthRecords.pdf 3、Self-determinationtheory:Amacrotheoryofhumanmotivation,development, andhealth. • DOI:10.1037/A0012801 • CorpusID:260685560 Deci&Ryan(2008)的后续研究扩展了SDT的应⽤，证明需求满⾜在⼯作、教育、健康 和休闲场景中的⼀致性，⽀持框架的泛化⽬标。  Self-determinationtheory-Amacrotheoryofhumanmotivation,development, andhealth.pdf 4、Ntoumanis,N.,Ng,J.Y.Y.,Prestwich,A.,Quested,E.,Hancox,J.E.,Thøgersen- Ntoumani,C.,Deci,E.L.,Ryan,R.M.,Lonsdale,C.,&Williams,G.C.(2021).Ameta- analysisofself-determinationtheory-informedinterventionstudiesinthehealth domain:Effectsonmotivation,healthbehavior,physical,andpsychologicalhealth. HealthPsychologyReview,15(2),214‒244 回顾了基于SDT的健康领域⼲预研究，分析了⾃主性、能⼒和关联需求满⾜对动机、健 康⾏为、⼼理健康和⽣理健康的影响。研究发现，SDT⼲预在健康领域（如吸烟戒断、 体重控制、体育活动）中⼀致促进⾃主动机和健康⾏为（p.216）。  Ameta-analysisofself-determinationtheory-informedinterventionstudiesin thehealthdomain-effectsonmotivation,healthbehavior,physical,and psychologicalhealth.pdf 5、Vansteenkiste,M.,Niemiec,C.P.,&Soenens,B.(2010).Thedevelopmentofthe fivemini-theoriesofself-determinationtheory:Anhistoricaloverview,emerging trends,andfuturedirections.InT.C.Urdan&S.A.Karabenick(Eds.),TheDecade Ahead:TheoreticalPerspectivesonMotivationandAchievement(Advancesin MotivationandAchievement,Vol.16)(pp.105‒165).EmeraldGroupPublishing Limited. |  |
| --- | --- |



### 第 8 页
这篇综述回顾了SDT的五个⼦理论（认知评价理论、有机整合理论、因果取向理论、基 本需求理论、⽬标内容理论），并讨论了其在教育、健康、⼯作、运动（休闲）等领域的 应⽤。 ⽂中明确提到，三⼤需求的满⾜在不同场景中⼀致促进⾃主动机、幸福感和绩效（p. 126）。例如： • 教育：⾃主⽀持的教师增强学⽣内在动机和学业表现（p.130）。 • ⼯作：⾃主⽀持的管理⻛格提⾼员⼯的参与度和幸福感（p.132）。 • 健康：⽀持⾃主性的⼲预促进健康⾏为的内化（如戒烟、运动坚持，p.134）。 • 休闲（运动）：满⾜⾃主性和关联需求的运动环境提⾼参与者的内在动机（p. 136）。  THEDEVELOPMENTOFTHEFIVEMINI-THEORIESOFSELF-DETERMINATION THEORY-ANHISTORICALOVERVIEW,EMERGINGTRENDS,ANDFUTURE DIRECTIONS.pdf 6、Ryan,R.M.,&Deci,E.L.(2017).Self-DeterminationTheory:BasicPsychological NeedsinMotivation,Development,andWellness.NewYork,NY:TheGuilfordPress. 这本书是SDT的全⾯总结，整合了Deci&Ryan(2008)及后续研究，详细讨论了三⼤需 求在教育、⼯作、健康、运动（休闲）、⼼理治疗等领域的应⽤。 书中明确指出，⾃主性、能⼒和关联需求的满⾜在不同场景中⼀致促进⾃主动机、幸福感 和⾏为坚持（第10章：教育；第11章：⼯作；第12章：健康；第13章：运动）。 休闲场景（如运动、游戏）被视为内在动机的关键领域，需求满⾜显著提⾼参与度和⼼理 健康（第13章）。 提供了⼤量实证研究⽀持，证明需求的普适性和跨场景⼀致性（第3章：基本需求理 论）。  Self-DeterminationTheory.pdf 7、（⽆法下载）《MGC:AModalMappingCouplingandGate-DrivenContrastive LearningApproachforMultimodalIntentRecognition》 • 来源:ScienceDirect,2025 • 链接:https://www.sciencedirect.com/science/article/pii/S003132032400734X[] (https://www.sciencedirect.com/science/article/abs/pii/S0957417425012539) 提出了⼀种基于模态映射耦合和⻔控驱动的对⽐学习策略（MGC），⽤于多模态意图识 别，处理⽂本、⾳频和视频模态。  MGC-Amodalmappingcouplingandgate-drivencontrastivelearningapproach formultimodalintentrecognition.pdf 8、（⽆法下载）《Human-in-the-LoopMultimodalIntentDetection》 来源:DigitalCommons,KennesawStateUniversity,2025 链接:https://digitalcommons.kennesaw.edu/[] (https://digitalcommons.kennesaw.edu/masterstheses/54/) 提出了⼀种统⼀框架MMIU，⽤于多模态意图分类和分布外（OOD）检测，融合语⾳、⽂ 本、⼿势和⾯部表情数据。 ⽤⼾需求： • 核⼼需求：明确表达且⾼优先级的意图（如紧急情绪⽀持、关键任务请求）。


| 这篇综述回顾了SDT的五个⼦理论（认知评价理论、有机整合理论、因果取向理论、基 本需求理论、⽬标内容理论），并讨论了其在教育、健康、⼯作、运动（休闲）等领域的 应⽤。 ⽂中明确提到，三⼤需求的满⾜在不同场景中⼀致促进⾃主动机、幸福感和绩效（p. 126）。例如： • 教育：⾃主⽀持的教师增强学⽣内在动机和学业表现（p.130）。 • ⼯作：⾃主⽀持的管理⻛格提⾼员⼯的参与度和幸福感（p.132）。 • 健康：⽀持⾃主性的⼲预促进健康⾏为的内化（如戒烟、运动坚持，p.134）。 • 休闲（运动）：满⾜⾃主性和关联需求的运动环境提⾼参与者的内在动机（p. 136）。  THEDEVELOPMENTOFTHEFIVEMINI-THEORIESOFSELF-DETERMINATION THEORY-ANHISTORICALOVERVIEW,EMERGINGTRENDS,ANDFUTURE DIRECTIONS.pdf 6、Ryan,R.M.,&Deci,E.L.(2017).Self-DeterminationTheory:BasicPsychological NeedsinMotivation,Development,andWellness.NewYork,NY:TheGuilfordPress. 这本书是SDT的全⾯总结，整合了Deci&Ryan(2008)及后续研究，详细讨论了三⼤需 求在教育、⼯作、健康、运动（休闲）、⼼理治疗等领域的应⽤。 书中明确指出，⾃主性、能⼒和关联需求的满⾜在不同场景中⼀致促进⾃主动机、幸福感 和⾏为坚持（第10章：教育；第11章：⼯作；第12章：健康；第13章：运动）。 休闲场景（如运动、游戏）被视为内在动机的关键领域，需求满⾜显著提⾼参与度和⼼理 健康（第13章）。 提供了⼤量实证研究⽀持，证明需求的普适性和跨场景⼀致性（第3章：基本需求理 论）。  Self-DeterminationTheory.pdf 7、（⽆法下载）《MGC:AModalMappingCouplingandGate-DrivenContrastive LearningApproachforMultimodalIntentRecognition》 • 来源:ScienceDirect,2025 • 链接:https://www.sciencedirect.com/science/article/pii/S003132032400734X[] (https://www.sciencedirect.com/science/article/abs/pii/S0957417425012539) 提出了⼀种基于模态映射耦合和⻔控驱动的对⽐学习策略（MGC），⽤于多模态意图识 别，处理⽂本、⾳频和视频模态。  MGC-Amodalmappingcouplingandgate-drivencontrastivelearningapproach formultimodalintentrecognition.pdf 8、（⽆法下载）《Human-in-the-LoopMultimodalIntentDetection》 来源:DigitalCommons,KennesawStateUniversity,2025 链接:https://digitalcommons.kennesaw.edu/[] (https://digitalcommons.kennesaw.edu/masterstheses/54/) 提出了⼀种统⼀框架MMIU，⽤于多模态意图分类和分布外（OOD）检测，融合语⾳、⽂ 本、⼿势和⾯部表情数据。 ⽤⼾需求： • 核⼼需求：明确表达且⾼优先级的意图（如紧急情绪⽀持、关键任务请求）。 |  |
| --- | --- |



### 第 9 页
• 次要需求：间接表达或⾮紧急的意图（如偏好确认、⼀般咨询）。 • 其他需求：潜在或低优先级的意图（如环境调整、探索性交互）。 认知系统：基于需求集合（核⼼、次要、其他需求）和Desire集合，通过艾森豪威尔矩阵 评估优先级。当Desire与核⼼需求⼀致时，系统执⾏合并逻辑，优化资源分配。 • Desire与核⼼需求⼀致性检查： ◦ ⽐较Desire集合和核⼼需求集合，识别内容重叠（如Desire“⽤⼾感到被理解”与 核⼼需求“情绪⽀持”⼀致）。 ◦ 若⼀致，合并为单⼀⾼优先级任务，标注为“核⼼需求主导，Desire增强”，避免 重复处理。 ◦ 合并任务继承核⼼需求的紧急性和重要性，Desire提供辅助优化（如更共情的表达 ⽅式）。 • 艾森豪威尔矩阵评估： ◦ 将需求和Desire（包括合并任务）按重要性和紧急性分为四象限： ▪ 第⼀象限（重要且紧急）：核⼼需求及合并任务（如情绪危机⽀持）。 ▪ 第⼆象限（重要但不紧急）：核⼼需求中的⻓期⽬标、次要需求的优化⽬标。 ▪ 第三象限（不重要但紧急）：次要需求中的即时请求、部分Desire（如即时体 验增强）。 ▪ 第四象限（不重要且不紧急）：其他需求、部分低优先级Desire。 ◦ 优先级排序： ▪ ⽤⼾需求（核⼼、次要、其他）优先于⾮合并Desire。 ▪ 合并任务优先级等同于核⼼需求，置于第⼀或第⼆象限。 ▪ 核⼼需求优先于次要需求，次要需求优先于其他需求。 ▪ ⾮合并Desire作为辅助，填充需求未覆盖的场景或增强体验。


| • 次要需求：间接表达或⾮紧急的意图（如偏好确认、⼀般咨询）。 • 其他需求：潜在或低优先级的意图（如环境调整、探索性交互）。 认知系统：基于需求集合（核⼼、次要、其他需求）和Desire集合，通过艾森豪威尔矩阵 评估优先级。当Desire与核⼼需求⼀致时，系统执⾏合并逻辑，优化资源分配。 • Desire与核⼼需求⼀致性检查： ◦ ⽐较Desire集合和核⼼需求集合，识别内容重叠（如Desire“⽤⼾感到被理解”与 核⼼需求“情绪⽀持”⼀致）。 ◦ 若⼀致，合并为单⼀⾼优先级任务，标注为“核⼼需求主导，Desire增强”，避免 重复处理。 ◦ 合并任务继承核⼼需求的紧急性和重要性，Desire提供辅助优化（如更共情的表达 ⽅式）。 • 艾森豪威尔矩阵评估： ◦ 将需求和Desire（包括合并任务）按重要性和紧急性分为四象限： ▪ 第⼀象限（重要且紧急）：核⼼需求及合并任务（如情绪危机⽀持）。 ▪ 第⼆象限（重要但不紧急）：核⼼需求中的⻓期⽬标、次要需求的优化⽬标。 ▪ 第三象限（不重要但紧急）：次要需求中的即时请求、部分Desire（如即时体 验增强）。 ▪ 第四象限（不重要且不紧急）：其他需求、部分低优先级Desire。 ◦ 优先级排序： ▪ ⽤⼾需求（核⼼、次要、其他）优先于⾮合并Desire。 ▪ 合并任务优先级等同于核⼼需求，置于第⼀或第⼆象限。 ▪ 核⼼需求优先于次要需求，次要需求优先于其他需求。 ▪ ⾮合并Desire作为辅助，填充需求未覆盖的场景或增强体验。 |  |
| --- | --- |



## 图片

![理论框架 图片 1](images/理论框架/理论框架_image_1.png)

![理论框架 图片 2](images/理论框架/理论框架_image_2.png)

![理论框架 图片 3](images/理论框架/理论框架_image_3.png)

![理论框架 图片 4](images/理论框架/理论框架_image_4.png)

![理论框架 图片 5](images/理论框架/理论框架_image_5.png)

![理论框架 图片 6](images/理论框架/理论框架_image_6.png)

![理论框架 图片 7](images/理论框架/理论框架_image_7.png)


## 参考文献

1. **Prompt Learning for Multimodal Intent Recognition with Modal Alignment Perception** - [DOI](https://doi.org/10.1016/j.knosys.2024.112373)
   - 讨论多模态意图识别的 PMAP 方法。
2. **Self-determination Theory: A Macrotheory of Human Motivation, Development, and Health** - [DOI](https://doi.org/10.1037/A0012801)
   - Deci & Ryan (2008) 关于自我决定理论的应用。
3. **A Meta-analysis of Self-determination Theory-informed Intervention Studies**，作者：Ntoumanis et al. (2021)
   - 分析健康领域的自我决定理论干预。
4. **The Development of the Five Mini-theories of Self-determination Theory**，作者：Vansteenkiste et al. (2010)
   - 自我决定理论的历史概览。