import pandas


def calculate_win_rate(row):
    return row['History Wins'] / (row['History Wins'] + row['History Loses'])


total_games = 0
higher_win_rate_wins = 0

for i in range(1,31):

    # read to dataframe
    path = '../../table_generation/tables/'+str(i)+'/OVERALL.csv'
    df = pandas.read_csv(path)

    # wash invalid data
    if not df['History Wins'].apply(pandas.to_numeric, errors='coerce').notna().all():
        continue

    df['Win Rate'] = df.apply(calculate_win_rate, axis=1)
    # Determine which team has a higher win rate for each game
    df['Higher Win Rate Team'] = df.apply(lambda row: 'Team 1' if row['Win Rate'] > (1 - row['Win Rate']) else 'Team 2', axis=1)
    # Count the number of games where the team with the higher win rate wins
    if df['Score'].values[0] >= df['Score'].values[1] and df['Higher Win Rate Team'].values[0]=='Team 1':
        higher_win_rate_wins+=1
    total_games += 1

# Calculate the overall percentage
overall_percentage = (higher_win_rate_wins / total_games) * 100

print(f"Overall Percentage of games where the team with the higher win rate wins: {overall_percentage:.2f}%")
