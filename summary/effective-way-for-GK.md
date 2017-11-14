Which is the Effective Way for Gaokao: Information Retrieval or Neural Network?
===================
By Shangmin Guo, Xiangrong, Shizhu He, Kang Liu and Jun Zhao
Reference: [EACL 2017 Paper][2] 

### Abstract
National Higher Education Entrance Examination, which is commonly knowns as Gaokao, is designed to be difficult enough to distinguish excellent high school students in China. The paper described Gaokao History Multiple Choice Questions(GKHMC) and proposed three approaches to address them. Approaches include **Information Retrieval(IR)**, **Neural Network(NN)** and the **combination of IR and NN**. Results show that IR performs better at Entity Questions(EQs), while NN performs better at Sentence Questions(SQs). The combination method achieves state-of-art performance, showing the necessity to apply hybrid method when encountering real-world scenarios.


### Motivation: Difficult History Multiple Choice Questions
Answering real world questions in various subjects it increasingly getting attentions. An ambitious [Project Halo][3] was proposed to create a "digital" Aristotle which can encompass most of the worlds'  scientific knowledge as well as solve hard problems. Important trials include solving mathematic and chemistry questions. In terms of the history questions, there are some NLP attempts for yes-no questions: determining the correctness of the original position [(Kanayama et al., 2012)][4] and recognizing textual entailment between a description in Wikipedia and each options[(Miyao et al,. 2012)][5]. Nevertheless, none of these approaches can solve difficult history multiple choice questions as shown in Figure 1, which require a huge amount of background knowledge. 

![](https://github.com/ztlbells/cs269-nlp-4-ml/blob/master/summary/F1a.png?raw=true)
![](https://github.com/ztlbells/cs269-nlp-4-ml/blob/master/summary/F1b.png?raw=true)
*Figure 1: Examples of history questions. EQ means all of the candidates are entities, which SQ means candidates are parts of the sentence.*

This paper is not the first to solve Gaokao questions, but the former approaches based on information retrieval did not fit well and suffer from limited knowledge resources in their systems. Therefore, works introduced in this paper are mainly focus on solving difficult GKHMC and proposing new approaches to improve accuracy.

### Datasets: Questions and Resources
All of the questions are from Gaokao all over the country in 2011 - 2015. Questions with graphs are filtered out since solving them requires techniques beyond NLP. The remaining questions are manually tagged as EQs or SQs. The question dataset is in XML format and available [here][1]. Numbers of different kinds of collected multiple-choice questions are listed as below. 

| Question Type | Candidate Type | Count|
| :--: | :----: | :---: |
| EQ | Entity Question | 160 |
| SQ | Sentence Question | 584 |
| ALL | Whatever | 744 |

Wide diversity of resources including Baidu Encyclopedia, textbooks and over 50,000 practice questions are also collected, which is in XML format as well and available [here][6].

### Approaches: IR, NN and Combination


[1]: https://github.com/IACASNLPIR/GKHMC/blob/master/data/Gaokao744.xml
[2]: http://www.aclweb.org/anthology/E17-1011
[3]: https://www.aaai.org/ojs/index.php/aimagazine/article/view/1783/1681
[4]: http://www.aclweb.org/anthology/C12-1084
[5]: https://dl.acm.org/citation.cfm?id=2382595
[6]: https://github.com/IACASNLPIR/GKHMC/blob/master/data/tiku.xml
