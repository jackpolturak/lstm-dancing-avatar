
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
    curve.bevel_depth = 0.035
    

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

o0 = bpy.data.objects['Icosphere']
o1 = bpy.data.objects['Icosphere.001']
o2 = bpy.data.objects['Icosphere.002']
o3 = bpy.data.objects['Icosphere.003']
o4 = bpy.data.objects['Icosphere.004']
o5 = bpy.data.objects['Icosphere.005']
o6 = bpy.data.objects['Icosphere.006']
o7 = bpy.data.objects['Icosphere.007']
o8 = bpy.data.objects['Icosphere.008']
o9 = bpy.data.objects['Icosphere.009']
o10 = bpy.data.objects['Icosphere.010']
o11 = bpy.data.objects['Icosphere.011']
o12 = bpy.data.objects['Icosphere.012']
o13 = bpy.data.objects['Icosphere.013']
o14 = bpy.data.objects['Icosphere.014']
o15 = bpy.data.objects['Icosphere.015']
o16 = bpy.data.objects['Icosphere.016']
o17 = bpy.data.objects['Icosphere.017']
o18 = bpy.data.objects['Icosphere.018']
o19 = bpy.data.objects['Icosphere.019'] 
o20 = bpy.data.objects['Icosphere.020']
o21 = bpy.data.objects['Icosphere.021']
o22 = bpy.data.objects['Icosphere.022']
o23 = bpy.data.objects['Icosphere.023']
o24 = bpy.data.objects['Icosphere.024']
o25 = bpy.data.objects['Icosphere.025']
o26 = bpy.data.objects['Icosphere.026']
o27 = bpy.data.objects['Icosphere.027']
o28 = bpy.data.objects['Icosphere.028']
o29 = bpy.data.objects['Icosphere.029']
o30 = bpy.data.objects['Icosphere.030']
o31 = bpy.data.objects['Icosphere.031']
o32 = bpy.data.objects['Icosphere.032']


#Center square
obj = hookCurve(o12,o11, bpy.context.collection, 1)
obj1 = hookCurve(o11,o23, bpy.context.collection, 3)
obj2 = hookCurve(o12,o24, bpy.context.collection, 4)
obj3 = hookCurve(o24,o23, bpy.context.collection, 5) 

#Right leg + foot
obj4 = hookCurve(o23,o25, bpy.context.collection, 6)
obj5 = hookCurve(o25,o27, bpy.context.collection, 7)
obj6 = hookCurve(o27,o31, bpy.context.collection, 8)
obj7 = hookCurve(o27,o29, bpy.context.collection, 9)
obj8 = hookCurve(o31,o29, bpy.context.collection, 10)


#Left leg +foot 
obj9 = hookCurve(o24,o26, bpy.context.collection, 11)
obj10 = hookCurve(o28,o26, bpy.context.collection, 12)
obj11 = hookCurve(o28,o30, bpy.context.collection, 13)
obj12 = hookCurve(o28,o32, bpy.context.collection, 14)
obj13 = hookCurve(o32,o30, bpy.context.collection, 15)


#right arm + hand
obj14 = hookCurve(o12,o14, bpy.context.collection, 16)
obj15 = hookCurve(o16,o14, bpy.context.collection, 17)
obj16 = hookCurve(o16,o18, bpy.context.collection, 18)
obj17 = hookCurve(o16,o22, bpy.context.collection, 19)
obj18 = hookCurve(o16,o20, bpy.context.collection, 20)
obj19 = hookCurve(o18,o20, bpy.context.collection, 21)


#left arm + hand
obj20 = hookCurve(o11,o13, bpy.context.collection, 22)
obj21 = hookCurve(o13,o15, bpy.context.collection, 23)
obj22 = hookCurve(o15,o21, bpy.context.collection, 24)
obj23 = hookCurve(o15,o17, bpy.context.collection, 25)
obj24 = hookCurve(o17,o19, bpy.context.collection, 26)
obj25 = hookCurve(o15,o19, bpy.context.collection, 27)