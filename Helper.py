import bpy

# Clear existing mesh objects in the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Define campus layout (coordinates for buildings, roads, etc.)
# Replace these coordinates with the actual layout of your campus
campus_layout = [
    (0, 0, 0),   # Building 1
    (5, 0, 0),   # Building 2
    (0, 5, 0),   # Building 3
    (5, 5, 0),   # Building 4
]

# Create buildings in the scene
for i, coord in enumerate(campus_layout):
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=coord)
    building = bpy.context.active_object
    building.name = f"Building_{i+1}"

# Set up camera
bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(10, -10, 10), rotation=(1.0472, 0, 0))
camera = bpy.context.active_object

# Set up materials (you can customize this part based on your campus aesthetics)
material = bpy.data.materials.new(name="CampusMaterial")
material.use_nodes = False  # Disable default node-based shader
material.diffuse_color = (0.8, 0.8, 0.8, 1)  # Adjust the color as needed

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        obj.data.materials.append(material)

# Set up lighting
bpy.ops.object.light_add(type='SUN', radius=1, align='WORLD
