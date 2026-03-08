from src.ingestion.worldbank import fetch_indicator

df = fetch_indicator("PT", "NY.GDP.MKTP.CD")

print(df.head())
print(df.tail())
print(df.shape)