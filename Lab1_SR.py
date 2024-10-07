import string
from numpy import double
import pandas as pd
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *
private_token = 'cdhqt3TDOQES08ADHiT7t8F8HEEcBAXpGK8o368p3J6uOFaCgibr8vZz0KCTqeaa'

client = RecombeeClient(
  'politehnica-university-of-bucharest-sisteme-recomandare-lab',
  private_token,
  region=Region.EU_WEST
)

# upload id produse
df = pd.read_csv('imdb_top_1000.csv', nrows=101)
for index, row in df.iterrows():
    client.send(AddItem(str(index)))

# salvare proprietăți produse
client.send(AddItemProperty("Poster_Link", 'string'))
client.send(AddItemProperty("Series_Title", 'string'))
client.send(AddItemProperty("Released_Year", 'int'))
client.send(AddItemProperty("Certificate", 'string'))
client.send(AddItemProperty("Runtime", 'string'))
client.send(AddItemProperty("Genre", 'string'))
client.send(AddItemProperty("IMDB_Rating", 'double'))
client.send(AddItemProperty("Overview", 'string'))
client.send(AddItemProperty("Meta_score", 'double'))
client.send(AddItemProperty("Director", 'string'))
client.send(AddItemProperty("Star1", 'string'))
client.send(AddItemProperty("Star2", 'string'))
client.send(AddItemProperty("Star3", 'string'))
client.send(AddItemProperty("Star4", 'string'))
client.send(AddItemProperty("No_of_Votes", 'int'))
client.send(AddItemProperty("Gross", 'string'))

#  salvare valori proprietăți produse
for index, row in df.iterrows():
    try:
        client.send(SetItemValues(str(index), row
            )
        )
    except APIException as e:
        print(str(index))
        print(e)