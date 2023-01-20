# CTR Prediction and LTR Models

## Content

>- 🈳: 暂时懒得写
>- ☑️: 已完成    
>- 🕣: 已完成但有一些问题/进行中    
>- 🚫:未完成

|Model|Year|Journal|Paper|State|
|:-:|:-:|:-:|:-:|:-:|
|FM|2010|ICDM|[Factorization machines](https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf)|🕣|
|FFM|2016|Recsys|[Field-aware Factorization Machines for CTR Prediction](https://www.andrew.cmu.edu/user/yongzhua/conferences/ffm.pdf)|🚫|
|WideDeep|2016|DLRS|[Wide&Deep Learning for Recommender Systems](https://arxiv.org/abs/1606.07792)|🕣|
|DeepFM|2017|IJCAI|[DeepFM: A Factorization-Machine based Neural Network for CTR Prediction](https://arxiv.org/abs/1703.04247)|🕣|
|DCN|2017|KDD|[Deep&Cross Network for Ad Click Predictions](https://arxiv.org/abs/1708.05123)|🕣|
|DCNv2|2020|WWW|[DCN V2: Improved Deep & Cross Network and Practical Lessons for Web-scale Learning to Rank Systems](https://arxiv.org/pdf/2008.13535.pdf)|🕣|
|NFM|2017|SIGIR|[Neural Factorization Machines for Sparse Predictive Analytics](https://dl.acm.org/doi/abs/10.1145/3077136.3080777)|🕣|
|AFM|2017|IJCAI|[Attentional Factorization Machines: Learning the Weight of Feature Interactions via Attention Networks](https://arxiv.org/abs/1708.04617)|🕣|
|xDeepFM|2018|KDD|[xDeepFM: Combining Explicit and Implicit Feature Interactions for Recommender Systems]()|🚫|
|FiBiNet|2019|Recsys|[FiBiNET: Combining Feature Importance and Bilinear feature Interaction for Click-Through Rate Prediction](https://arxiv.org/pdf/1905.09433.pdf)|🚫|
|AutoInt|2019|CIKM|[AutoInt: Automatic Feature Interaction Learning via Self-Attentive Neural Networks](https://arxiv.org/abs/1810.11921)|🚫|
|DIN||🚫|
|DIEN||🚫|
|ESMM||🚫|


## Log

- 2023-01-20: 基本框架设计
  - 数据: `./data`目录下, 采用`data_utils.load_data`读入, `data_utils.preprocess_data`预处理, `data_utils.DataCenter`进行存储与载入, 半私有化数据类型推理, 输入数据分为连续型与类别型(暂定, 时间戳等数据类型后续再考虑)
  - 模型: `./models`目录下, 将模型分为多种Layer进行拼接, Layer保存在`./models/layers`内
  - 训练: `./utils/trainer`目录下, 深度模型采用`trainer.DeepCTRTrainer`训练