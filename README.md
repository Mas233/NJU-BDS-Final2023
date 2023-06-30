# Text_To_Table
## 项目描述
本项目从含有多行文本资料的源文件中选取最长的固定N行，并将其输出至暂存文件中；
之后调取暂存文件中的数据，利用OpenAI的API将其转换为表格形式，并输出至目标文件中。本次项目中N=30.
## 项目输入输出
- 源文件：`rotowire.txt`
- 暂存文件：`chosen.txt`
- 目标目录：`table_generation/tables/{i}/` *(1<=i<=10)*
- 目标文件：
   - `src.txt`: 源文件中的文本
   - `res.txt`: 源文件中的文本转换为表格形式后的结果
   - `OVERALL.csv`: 比赛结果信息的表格形式
   - `PLAYER.csv`: 球员统计信息的表格形式

## 项目运行方式
- 运行根目录下的ttt.bat，或用命令行输入'ttt'。结果将保存在目标目录中。
- 若目标目录非空，请使用'ttt -f'强制重新生成表格。
## 备注
- 项目文件均采用硬编码，请勿轻易修改文件名、文件夹名、文件路径等。
- OpenAI密钥保存于"C:\\key.txt"文件中，请确认本环境拥有该文件且已储存密钥。或通过修改`table_generation/const.py`中的`key`变量来指定密钥文件的路径。
- 若出现OpenAI连接错误，请检查urllib3库版本是否高于1.25.11。若是，请使用`pip install urllib3==1.25.11`命令安装。

# Data_Analysis
用python和Pandas进行了两个分析
- `rebounds_points.py`：清洗数据后计算所有收集到的Points和Rebounds之间的协方差和相关系数
- `winner_wins.py`：清洗数据后计算历史胜率更高的队伍赢得当局比赛的比例
