import pandas as pd

# url = 'https://en.wikipedia.org/wiki/History_of_Python'

url = 'https://www.pse.pl/obszary-dzialalnosci/rynek-energii/ceny-i-ilosc-energii-na-rynku-bilansujacym'

# url = 'https://www.gismeteo.pl/weather-warsaw-3196/10-days'
dfs = pd.read_html(url)


# Get first table                                                                         
# df = dfs[0]

# Extract columns                                                                                                
# df2 = df[['Version','Release date']]
# print(df2)


# df2.to_excel('python.xlsx')

# print(len(dfs))

print(dfs[2])

dfs[2].to_excel('test111.xlsx')