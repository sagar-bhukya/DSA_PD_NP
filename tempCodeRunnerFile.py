new_data = {'Roll_No': [115,112,119], 'Name_of_Student': ['Arjun','pavan','ashok'], 'Telugu': [92,50,88], 'English': [87,90,40], 'Maths': [79,50,40], 'Science': [84,50,80], 'Social': [88,88,90]}
new_df = pd.DataFrame(new_data)
# Append the new DataFrame to the existing one
dfr = dfr._append(new_df)  # Avoid duplicate indexing
print('---------\n',dfr)

print("removing duplicates========================")
print('knowing duplicate->df.duplicate()->returns boolen value')
dp=dfr.duplicated()
print('duplicate\n',dp)#false