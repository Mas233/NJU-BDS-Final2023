import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

for i in range(1,31):
    if i==15:continue
    path = '../../table_generation/tables/'+str(i)+'/PLAYERS.csv'
    df = pd.read_csv(path)
    values=[df['Points'],df['Rebounds'],df['Assists'],df['Steals'],df['Blocks']]
    labels=['Points','Rebounds','Assists','Steals','Blocks']
    colors = ['#F55050','#8250F5','#4980DF','#49DF80','#F0E653']
    player_name=df['Player']
    fig,ax=plt.subplots()
    x=np.arange(len(player_name))
    bar_width=0.3
    blank=0.3
    sets=df.drop('Team',axis=1).drop('Player',axis=1)
    for j,col in enumerate(sets.columns):
        ax.bar(x+j*(bar_width+blank),
               values[j],
               color=colors[j],
               bottom=0,
               width=bar_width,
               label=labels[j])
    ax.set_xticks(x + bar_width*(len(sets.columns) - 1)/2)
    ax.set_xticklabels(player_name)

    plt.ylim(bottom=0)
    plt.xlabel('PlayerName')
    plt.ylabel('Performances')
    plt.title('GameResult')

    for j, col in enumerate(sets.columns):
        ax.bar(x + j*(blank+bar_width)+0.08, values[j], width=bar_width,bottom=-0.05, color='black', alpha=0.2, zorder=2)
    plt.legend()
    plt.yticks([])
    fig.set_size_inches(18,12)
    plt.xticks(rotation=30)

    export_name=str(i)+'th_chart.png'
    plt.savefig(export_name,dpi=300)
