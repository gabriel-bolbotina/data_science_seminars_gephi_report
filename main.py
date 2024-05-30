import pandas as pd

# Load the dataset
nodes = pd.read_csv('/Users/gabrielbolbotina/Documents/CTI/Master/Erasmus/Data science seminars/Gephi report/painters_1300-1800-2.csv', sep = ";")

print(nodes.head())
# Create a DataFrame for edges
edges = []
counter = 0

for i, painter1 in nodes.iterrows():
    counter += 1
    for j, painter2 in nodes.iterrows():
        if i >= j:
            continue
        # Example criteria: overlapping lifespan
        if (painter1['nationalityLabel'] == painter2['nationalityLabel']) and (painter1['Period'] == painter2['Period']):
            edges.append([painter1['painterLabel'], painter2['painterLabel'], 'undirected', 1])
    if counter > 500:
      break

# Convert to DataFrame
edges_df = pd.DataFrame(edges, columns=['Source', 'Target', 'Type', 'Weight'])

# Save to CSV
edges_df.to_csv('edges.csv', index=False)

print(nodes.head())
