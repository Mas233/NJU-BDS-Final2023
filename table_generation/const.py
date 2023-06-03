# model name constants:
davinci_3 = 'text-davinci-003'
davinci_2 = 'text-davinci-002'
curie = 'text-curie-001'
babbage = 'text-babbage-001'
ada = 'text-ada-001'

# path and file constants:
table = ".\\tables\\"
chosen = "..\\chosen.txt"
key = "C:\\key.txt"
txt = "txt"
csv = "csv"

# request constants:
requirements = "Generate tables from a passage following these requirements: " \
               "(1)The first table should include columns \"Team\",\"History Wins\"\"History Loses\" \"Score\" with name \"OVERALL\";" \
               "(2)The second table should include columns \"Team\", \"Player\", \"Points\", \"Rebounds\", \"Assists\",\"Steals\",\"Blocks\" with name \"PLAYERS\";" \
               "(3)Show the results in csv format." \
               "(4)Use \"N\A\" for unclear data." \
               "Here's the passage:"
