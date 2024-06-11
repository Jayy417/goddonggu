import tabula

dfs = tabula.read_pdf(
	"/Users/jeongjuho/Desktop/aaaaa.pdf", 
	pages="all", 
	stream=True
)
print(f"Data Type :{type(dfs)}")
print(f"Data Length: {len(dfs)}")
for index, table in enumerate(dfs):
  print(f"\nData Index: {index}")
  print(type(table))
  print(table.head())