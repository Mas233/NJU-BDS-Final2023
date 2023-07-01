# Winner wins

- 简介：利用python清洗数据并计算`OVERALL`表有效数据中每场比赛双方的历史胜率以及当前比赛胜者，并总计胜率更高的队伍赢得本场比赛的概率。

- 分析方式：python、pandas

- 详细说明：
  
  - 对每一个OVERALL表，首先读入并建立DataFrame类型：
    
    ```python
        path = '../../table_generation/tables/'+str(i)+'/OVERALL.csv'
        df = pandas.read_csv(path)
    ```
  
  - 数据清洗：跳过无效数据的表
    
    ```python
    if not df['History Wins'].apply(pandas.to_numeric, errors='coerce').notna().all():
        continue
    ```
  
  - 计算胜率和当前胜者：
    
    ```python
    df['Win Rate'] = df.apply(calculate_win_rate, axis=1)
    df['Higher Win Rate Team'] = df.apply(lambda row: 'Team 1' if row['Win Rate'] > (1 - row['Win Rate']) else 'Team 2', axis=1)
    ```
  
  - 统计有效比赛数和有效比赛中历史胜率更高者获得胜利的总数
    
    ```python
    if df['Score'].values[0] >= df['Score'].values[1] and df['Higher Win Rate Team'].values[0]=='Team 1':
        higher_win_rate_wins+=1
    total_games += 1
    ```
  
  - 计算其占比的百分率并输出
    
    ```python
    overall_percentage = (higher_win_rate_wins / total_games) * 100
    print(f"Overall Percentage of games where the team with the higher win rate wins: {overall_percentage:.2f}%")
    ```

- 输出：     ![](C:\Users\Mad_Mas\AppData\Roaming\marktext\images\2023-07-01-02-02-55-image.png)

- 结论：
  
  更多的比赛胜者是历史胜率更高的队伍，但这种差异并不明显。
