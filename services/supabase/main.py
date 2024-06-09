import supabase
import os
from env import *
# import authData

create_client = supabase.create_client
Client = supabase.Client

url: str = SUPABASE_URL
key: str = SUPABASE_KEY

# data = supabase.table("")





# print(url)
client: Client = create_client(url, key, )
client.schema_name("SIEM")

attack_sources = client.table("attack_sources").select("*").execute()

assert len(attack_sources['data']) > 0

if supabase:
    print("Connected to Supabase successfully!")
    print("Data:", attack_sources['data'])
    # print("Schema Name:", schema_name)
else:
    print("Failed to connect to Supabase.")