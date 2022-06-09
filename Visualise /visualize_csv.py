#This code is intended to be ran within blnders embed interpeter
import pandas as pd
import bpy


dataset = "/Users/jackpolturak/Documents/GitHub/csv-transfer/Kab7_GENERATED.csv"
df = pd.read_csv(dataset)
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

df = df*5
print(df)  

number_cols = len(df.columns) 
dimensions = 3 
n_joints = int(number_cols/dimensions)

col_count = 0
for i in range(33):
    postions = df.iloc[:, col_count:col_count+dimensions]
    print(postions)
 
    # CREATE ONJECT HERE RADIUS = 0.08
    cube = bpy.ops.mesh.primitive_ico_sphere_add(radius=0.1)
    object = bpy.context.active_object
    
    # in here add modifier to add subdivision surface

    for index, row in postions.iterrows():
        loc = (float(row[0]), float(row[2]), -float(row[1])-2)
        fn = index
        object.location = loc
        
        object.keyframe_insert(data_path="location", frame=fn)
        print(fn)
        # print(loc) 
        #ASSIGN KEY FRAME VALUES HERE


    #GO to next couple of cols for next itteration
    col_count += dimensions


