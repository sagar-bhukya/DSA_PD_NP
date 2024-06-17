import pandas as pd
print('creating data frame------------')
print('1.load the csv file')
d=pd.read_csv('data.csv')
d1=pd.read_csv('strong.csv')
print('creating dataframe')
dfr=pd.DataFrame(d)
df1=pd.DataFrame(d1)
print(dfr)

print('2.using dictionary--')
di={'name':['a','b','c'],"roll":[1,2,3],'perc':[90.9,59.0,65.7]}
df=pd.DataFrame(di)
print(df)


print('indexing slicing, for large and small data--------------------')
#1head()
print('1.data_frame.head(how many do you want)-by default fetch first 5 records from the df')
dh=dfr.head()
print('head() first 5\n',dh)
dh1=dfr.head(2)
print('head(2) first 2 records\n',dh1)

#2.tail()
print('2.df.tail(how many do you want), by default fetch last 5')
dt=dfr.tail()
print('tail() from last 5 records\n',dt)
dt1=dfr.tail(3)
print('tail(3) from last 3 records\n',dt1)

#3describe()
print('3.df.describe() it does maths function for the dataframe like count,mean,std, min,max,perc')
ds=dfr.describe()
print('describe() does maths function\n',ds)

#4shape
print('4. df.shape-> it tells the (2,3)->(2rw,3cl)')
dsh=dfr.shape
print('shape of dataframe\n',dsh)# (20, 7)
dsh1=df1.shape
print('shape of large data\n',dsh1)# (3989, 12)

#5.indexing
print('indexing->  df[start:stop:step]')
ind=dfr[0:10:2]
print('indexing\n',ind)

#6df['with_column_name_access']
dc=dfr['Name_of_Student']
print('Name_of_Student->fetch column of records\n',dc)

#7df[[col1,col2]]- for 2 columns access
dc2=dfr[['Name_of_Student','English']]
print('fetch 2 columns of the records\n',dc2)

#8.make in to 2-D, for 2 columns 
d2d=dfr[['Name_of_Student','English']][0:10:1]
print('make that in 2-D format ex:a[][]\n',d2d)

#----------------------------------------------------------------------#
print('loc[]. stop value is included and column access by their name itself-------------')
print('1.df[row_number]')
dr=dfr.loc[4]
print('loc[2]->fetch only 2 row of all columns data\n',dr)


print('2.df[row_number,["column_name"]]')
drc=dfr.loc[2,["Name_of_Student"]]
print('data\n',drc)
drc2=dfr.loc[2,['Name_of_Student','English']]
print('for multiple columns of data fetching\n',drc2)

print('4.loc[start:stop]-=>stop included')
dl=dfr.loc[0:5]
print('0to5 values\n',dl)
print('4.loc[start:stop]->stop excluded')
dl1=dfr.iloc[0:5]
print('0to4 values\n',dl1)

print('5.df.loc[start:stop,"column_name"]')
dcn=dfr.loc[0:5,'Name_of_Student']
print('only column data of those row will display\n',dcn)
print('for two columns gives ->[]')
dcn1=dfr.loc[0:5,["Name_of_Student",'English']]
print('2 columns of data will print\n',dcn1)

print('range for the columns->df.loc[0:5,"col1":col..n]')
dcr=dfr.loc[0:5,"Name_of_Student":"Maths"]#after maths column not display
print('both row and column have range\n',dcr)



#iloc----------------------------------------------------
print('Dataframe: \n',dfr)
'''
Dataframe:
        c=0            c=1      c=2    c=3      c=4      c=5    c=6
rows Roll_No Name_of_Student  Telugu  English  Maths  Science  Social
0       101         sundeep      90       85     80       83      75
1       102         saradhi      50       60     75       54      64
2       103          ramesh      95       78     68       58      78
3       104          suresh      55       87     68       64      59
4       105         sathwik      88       84     98       73      81
5       106         abhiram      73       84     91       88      84
6       107        srinidhi      90       83     74       86      94
7       108         lakshmi      75       78     85       64      53
8       109          dinesh      84       85     76       94      54
9       110          harish      83       98     81       63      79
10      111          murali      85       86     92       75      35
11      112            vasu      50       54     64       87      45
12      113            kali      89       97     69       73      82
13      114            ramu      25       45     60       35      48
14      115         krishna       1       25     65       50      55
15      116            hari      78       89     95       67      58
16      117           pavan      59       52     68       68      70
17      118           ashok      85       86     98       78      44
18      119          govind      89       89     95       66      95
19      120         bhargav      72       78     86       64      72
'''
print('iloc[]->stop is excluded and column access by only number of the columns')
print('1.df.iloc[row_number,column_number]')
f1=dfr.iloc[2,1]
print('[2,1]\n',f1)

print('range for both column and row')
print('df.iloc[row-start:row-stop,col-start:col-stop]')
f2=dfr.iloc[0:3,1:4]
print('range for both\n',f2)

print('df.iloc[start:stop,column_number]')
f3=dfr.iloc[0:4,1]
print('column 1:\n',f3)

print('df.iloc[[row1,row2,row3....]]-> how many do you want.    should row numbers pass in [[]]')
f4=dfr.iloc[[1,2,3,4]]
print('fetch rows 1,2,3,4\n',f4)

print('df.iloc[:,[col1,col2,col3....]], gives all rows but col we have to give            col should give in [[]]')
f5=dfr.iloc[:,[1,2,4]]
print('all rows but column [1,2,4]',f5)

print('df.iloc[start:stop,[col-start:col-stop]]')
f6=dfr.iloc[0:4,[1,4,3]]
print(f6)



#sorting Dataframe------------------------------------------
print("1.df.sort_values(column_name)-> by default sorts in ascending order, if you want descending order, just give this parameter:ascending=False")
print('======Single column name')
s=dfr.sort_values('Name_of_Student')
print('Name_of_Student->by default ascending order\n',s)
s=dfr.sort_values('Name_of_Student',ascending=False)
print('Name_of_Student=> for descening order, just add ascending=False\n',s)
print('\n')
print('two or more but order follows the first column then second column')
s2=dfr.sort_values(['English','Maths','Telugu'])
print('ascending order\n',s2)
s2=dfr.sort_values(['English','Maths','Telugu'],ascending=False)
print('for descending order\n',s2)

#manipulating Dataframes--------------------------------------------
print('Adding ----------')
# unique column names not support if we give updated with latest column name
print("df['new_column']=defaultvalue")
dfr["Total"]=0
print('new column Total with deafult value=0 added at end of Dataframe\n',dfr)
print('dfr[new_column]=expression/condition')
dfr['Total']=dfr['Maths']+dfr['Telugu']+dfr['English']+dfr['Science']+dfr['Social']
print('addition of all subject of marks\n',dfr)

#get all column names 
print('get all column names')
# column_names = dfr.head(0).columns.tolist()
colum_names=dfr.columns.tolist()
print('column names\n',colum_names)

#get except roll_no and Name_of_Student column
print("get except roll_no and Name_of_Student column")
column_except=[col for col in dfr.columns if col not in ['Roll_No', 'Name_of_Student']]
print("except columns\n",column_except)
# Select only numeric columns (excluding 'Roll_No' and 'Name_of_Student')
numeric_columns = [col for col in dfr.columns if col not in ['Roll_No', 'Name_of_Student'] and pd.api.types.is_numeric_dtype(dfr[col])]  # Check for numeric data type
#to crate new column and add a expression to that
dfr['Sum'] = dfr[numeric_columns].sum(axis=1)
print('new\n',dfr)


print('2.Removing data or column name')
print("df.drop(columns='column_name')->temporary dropped if you want frop permanantely, inplace=True")
dfr['perc']='Pass/Fail'
print(dfr)
#now remove perc column
dd=dfr.drop(columns='perc')
print('perc coumn dropped\n',dd)
dd=dfr.drop(columns='perc',inplace=True)
print('permanent dropped\n',dd)#None returned
print(dfr)


#aadding new rows data to existing to csv file 
# Create a DataFrame with new row data
new_data = {'Roll_No': [115,112,119], 'Name_of_Student': ['Arjun','pavan','ashok'], 'Telugu': [92,50,88], 'English': [87,90,40], 'Maths': [79,50,40], 'Science': [84,50,80], 'Social': [88,88,90]}
new_df = pd.DataFrame(new_data)
# Append the new DataFrame to the existing one
dfr = dfr._append(new_df)  # Avoid duplicate indexing
print('---------\n',dfr)

print("removing duplicates========================")
print('knowing duplicate->df.duplicate()->returns boolen value')
dp=dfr.duplicated()
print('duplicate\n',dp)#false

print("drop_duplicates()-> temporary")
dpt=dfr.drop_duplicates()
print(dpt)

# print("drop_duplicates(inplace=True)->for permanent delete")
# dpp=dfr.drop_duplicates()
# print('removes permanant\n',dpp)

# Find duplicate values (excluding the first occurrence)
# duplicates = dfr[dfr["Name_of_Student"].duplicated(keep='first')]
duplicat=dfr["Name_of_Student"].duplicated(keep='first')
print(duplicat)#gives boolean values
duplicates=dfr[duplicat]# returns only True valus
print("dup\n",duplicates)
#know duplicates in a column 
print("know duplicates in a column\n",duplicates["Name_of_Student"].unique()) 



print("Handling with missing data------------in a sheet somewhere a cell of data not there we need to remove or delete that or fill-----")
print('df.dropna()-temporarily removing data')
da=dfr.dropna()
print("temporary dropna()\n",da)
da=dfr.dropna(inplace=True)
print("permanent drop data\n",da)


print("filling with defualt value")
dfa=dfr.fillna(78)
print("df.fillna.(default value\n",dfa)

print("Data handling and Conditional changes----")
print("df.loc[simple_condition] like:>/</==")
dc1=dfr.loc[dfr["Maths"]>80]
print("simple condition\n",dc1)
dc2=dfr.loc[(dfr["Maths"]>80) & (dfr["Maths"]<50)]
print("compound condition\n",dc2)

dcs=dfr.loc[dfr["Name_of_Student"].str.contains('n')]
print("contains function\n",dcs)
dcs2=dfr.loc[dfr["Name_of_Student"].str.startswith('a')]
print("startswith\n",dcs2)
dcs3=dfr.loc[dfr["Name_of_Student"].str.endswith('n')]
print("endswith\n",dcs3)


#Export Dataframe
print("df.to_excel(path.xlsx)")
dfr.to_excel('expo.xlsx')
print("df.to_excel(path.xlsx,index=False)-. without index values")
dfr.to_excel('without_index.xlsx',index=False)
print("df.to_csv(path) with index")
dfr.to_csv('with_csv_index.csv')
print("df.to_csv(path),index=False->without indexing")
dfr.to_csv('without_index_csv.csv',index=False)


