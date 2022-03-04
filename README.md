### Matplotlib 绘图与数据分析

#### 名词解释

**fixed acidity**: 固定酸度.

**volatile acidity**: 挥发性酸度, 太高的酸度会导致红酒味道变差.

**citric acid**: 柠檬酸, 少量的柠檬酸能增加红酒的鲜度.

**residual sugar**: 残糖,也即酒精发酵后未被发酵而残余的糖分.

**chlorides**: 氯化物, 红酒中的盐.

**free sulfur dioxide**: 游离二氧化硫, 能防止微生物和被氧化.

**total sulfur dioxide**: 总二氧化硫量, 包含游离二氧化硫和结合二氧化硫, 如果游离二氧化硫浓度超过 $\rm50ppm,$ 就能从红酒中感受到二氧化硫的味道.

**density**: 密度, 水的密度, 水减去酒精和糖的容量后计算得到.

**pH**: 酸碱度, 0 (酸) ~ 14 (碱).

**sulphates**: 硫酸盐, 会产生二氧化硫的添加剂, 有抗菌剂和抗氧化剂的作用.

**alcohol**: 酒精度.

**quality**: 评分.

#### 数据范围

|属性|平均值|最小值|最大值|
|-|-|-|-|
fixed acidity       |8.313222416812618  |4.6    |15.9
volatile acidity    |0.5312390542907177 |0.12   |1.58
citric acid         |0.26849387040280115|0.0    |1.0
residual sugar      |2.532618213660242  |0.9    |15.5
chlorides           |0.08694308231173353|0.012  |0.611
freesulfur dioxide  |15.601138353765323 |1.0    |68.0
total sulfur dioxide|45.916374781085814 |6.0    |289.0
density             |0.9967315148861652 |0.99007|1.00369
pH                  |3.3107880910683027 |2.74   |4.01
sulphates           |0.657661996497373  |0.33   |2.0
alcohol             |10.442323409223569 |8.4    |14.9
quality             |5.657618213660245  |3      |8

#### 数据集的不足

葡萄酒的质量集中于 4~7 之间, 缺少质量非常低或非常高的葡萄酒.

#### 工作

使用 **Kaggle** 的数据集 *Wine Quality Dataset* 和 **Python Matplotlib** 绘制了散点图, 柱状图, 分组柱状图, 直方图, 箱线图, 折线图, 饼图, Nightingale玫瑰图, 雷达图, 等高线图等.

对数据中各属性在总体和各个质量中的分别进行了简单的分析,对各属性两两之间的关系和与质量的关系进行了简单的分析.

#### 结论

酒精度数/硫酸盐/柠檬酸与品质大体呈正相关关系, 挥发性酸与品质大体呈负相关关系.

#### 数据来源

[Wine Quality Dataset](https://www.kaggle.com/yasserh/wine-quality-dataset)

#### 参考资料

[NumPy documentation](https://numpy.org/doc/stable/)

[Matplotlib 3.5.1 documentation](https://matplotlib.org/3.5.1/tutorials/index.html)

[Uda-DataAnalysis-pj02--红葡萄酒数据质量分析报告](http://road2ai.info/2017/12/14/Uda-DataAnalysis-pj02/)

#### License

MIT License
