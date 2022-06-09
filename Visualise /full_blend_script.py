import pandas as pd



dataset = "/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Pose data/CSVs/data.csv"
df = pd.read_csv(dataset)
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)


# print(df*10)







number_cols = len(df.columns)
dimensions = 2
n_joints = int(number_cols/dimensions)

col_count = 0
for i in range(n_joints):
    postions = df.iloc[:, col_count:col_count+2]
    print(postions)

    # CREATE ONJECT HERE
    cube = bpy.ops.mesh.primitive_ico_sphere_add(radius=0.005)
    object = bpy.context.active_object
    

    for index, row in postions.iterrows():
        loc = (float(row[0]), float(row[1]), float(0))
        fn = index
        object.location = loc
        
        object.keyframe_insert(data_path="location", frame=fn)
        print(fn)
        # print(loc)
        #ASSIGN KEY FRAME VALUES HERE


    #GO to next couple of cols for next itteration
    col_count +=2



import bpy

def hookCurve(o1, o2, scn, link_number):
    curve = bpy.data.curves.new("link", 'CURVE')
    spline = curve.splines.new('BEZIER')

    spline.bezier_points.add(1)
    p0 = spline.bezier_points[0]
    p1 = spline.bezier_points[1]
    p0.co = o1.location
    p0.handle_right_type = 'VECTOR'
    p1.co = o2.location
    p1.handle_left_type = 'VECTOR'

    obj = bpy.data.objects.new(f"link{link_number}", curve)

    m0 = obj.modifiers.new("alpha", 'HOOK')
    m0.object = o1
    m1 = obj.modifiers.new("beta", 'HOOK')
    m1.object = o2

    scn.objects.link(obj)
    
    #SET CRUVE TO ACTIVE
s
    bpy.context.view_layer.objects.active = obj

    # using anything in bpy.ops is a giant pain in the butt
    bpy.ops.object.mode_set(mode='EDIT')
    
#    curve_name = curve.name 
#    
    curve.bevel_depth = 0.3
    

    # the mode_set() invalidated the pointers, so get fresh ones
    p0 = curve.splines[0].bezier_points[0]
    p1 = curve.splines[0].bezier_points[1]

    p0.select_control_point=True
    bpy.ops.object.hook_assign(modifier="alpha")

    p0.select_control_point = False
    p1.select_control_point = True
    bpy.ops.object.hook_assign(modifier="beta")
    
    bpy.ops.object.mode_set(mode="OBJECT")

    return obj

o1 = bpy.data.objects['Icosphere.001']
o2 = bpy.data.objects['Icosphere.002']
o3 = bpy.data.objects['Icosphere.003']
o4 = bpy.data.objects['Icosphere.004']


obj = hookCurve(o2,o1, bpy.context.collection, 3)
obj1 = hookCurve(o4,o3, bpy.context.collection, 4)



import bpy

def hookCurve(o1, o2, scn, link_number):
    curve = bpy.data.curves.new("link", 'CURVE')
    spline = curve.splines.new('BEZIER')

    spline.bezier_points.add(1)
    p0 = spline.bezier_points[0]
    p1 = spline.bezier_points[1]
    p0.co = o1.location
    p0.handle_right_type = 'VECTOR'
    p1.co = o2.location
    p1.handle_left_type = 'VECTOR'

    obj = bpy.data.objects.new(f"link{link_number}", curve)

    m0 = obj.modifiers.new("alpha", 'HOOK')
    m0.object = o1
    m1 = obj.modifiers.new("beta", 'HOOK')
    m1.object = o2

    scn.objects.link(obj)
    
    #SET CRUVE TO ACTIVE

    bpy.context.view_layer.objects.active = obj

    # using anything in bpy.ops is a giant pain in the butt
    bpy.ops.object.mode_set(mode='EDIT')
    
#    curve_name = curve.name 
#    
    curve.bevel_depth = 0.3
    

    # the mode_set() invalidated the pointers, so get fresh ones
    p0 = curve.splines[0].bezier_points[0]
    p1 = curve.splines[0].bezier_points[1]

    p0.select_control_point=True
    bpy.ops.object.hook_assign(modifier="alpha")
    p0.select_control_point = False
    
    p1.select_control_point = True
    bpy.ops.object.hook_assign(modifier="beta")
    p1.select_control_point = False
    
    bpy.ops.object.mode_set(mode="OBJECT")

    return obj

o1 = bpy.data.objects['Icosphere.001']
o2 = bpy.data.objects['Icosphere.002']
o3 = bpy.data.objects['Icosphere.003']
o4 = bpy.data.objects['Icosphere.004']
o5 = bpy.data.objects['Icosphere.005']
o6 = bpy.data.objects['Icosphere.006']

obj = hookCurve(o2,o1, bpy.context.collection, 3)
obj1 = hookCurve(o4,o3, bpy.context.collection, 4)
obj2 = hookCurve(o5,o6, bpy.context.collection, 5)


o = bpy.data.objects['Icosphere']
o2 = bpy.data.objects['Icosphere.011']
o3 = bpy.data.objects['Icosphere.013']
o3 = bpy.data.objects['Icosphere.013']