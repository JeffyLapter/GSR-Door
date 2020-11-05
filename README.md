# GSR-Door
GaitSet Recognization Based Intellgent Door

### 项目架构：

![1604487914360](assets/1604487914360.png)

### 项目物理结构：

![1604487957267](assets/1604487957267.png)

### 主要分工：

王京首、王睿思：负责主控制模块与捕获模块开发

朱庆晨、李阳：负责步态识别模块开发、门锁机械结构设计、实验模型搭建

### 项目时间轴

1. 确定项目基本结构 √
2. 确定项目基础架构及各模块功能、确定分工
3. 撰写项目报告
4. 开发
5. 调试组装

### 项目基础结构（分模块）

1. #### 主控制模块

   用于项目模块间的协同，接收步态识别模块返回结果，启动开锁机等

   ##### 功能：

   ​	a. 初始化视频捕获与特征提取模块

   ​	b. 将视频捕获与特征提取模块返回的矩阵或特征数据送入步态识别模块 

   ​	c. 接收步态识别模块返回结果，根据结果确定是否启动开锁机

   

2. #### 视频捕获与特征提取模块

   用于捕获步态视频，并提取姿态数据，用作步态识别算法的输入

   ##### 功能：

   ​	a. 实时视频流检测是否有人经过

   ​	b. 检测到有人经过时启动捕获，提取行走时的步态特征。

   ​	c. 将步态特征提取并格式化(向量化)，返回给主控制模块

   

3. #### 步态识别模块

   用于识别并判断步态

   ##### 功能：

   ​	a. 接收主模块提供的 来自视频捕获与特征提取模块 的姿态数据（数据结构未定）

   ​	b. 多分类（算法）

4. #### 开锁机

   用于机械开锁

   ##### 功能：

   ​	a. 接收主模块提供的，来自步态识别模块 的返回值

   ​	b. 通过Ardunio+ULN2003启动28byj-48步进电机开锁或关锁。

##### 注：模块2与模块3可参考或使用https://github.com/AbnerHqC/GaitSet

### Reference:

##### https://github.com/AbnerHqC/GaitSet

##### https://github.com/luwanglin/GaitSet_learning

