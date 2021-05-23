import pandas as pd
import pandas_usaddress

# load dataframe
df = pd.read_csv('test_file.csv')

# initiate usaddress
# df = pandas_usaddress.tag(df, ['street1', 'street2', 'city', 'state'], granularity='single', standardize=True)

df = pandas_usaddress.tag(df, ['address_field'])

# send output to csv
df.to_csv('parsed_output.csv')
