import bpy
import os

textures = bpy.data.textures
brushes = bpy.data.brushes

thumbnail_folder = "E:/Assets/Blender Library/Brushes/Gumroad_SeamsAndStiches/Thumbnails"

if "Base" in bpy.data.brushes:
    base = brushes["Base"]
    for texture in textures:
        new_brush = base.copy()
        new_brush.name = texture.name
        new_brush.texture = texture
        new_brush.use_custom_icon = True
        
        texture_filename = os.path.basename(texture.image.filepath)
        thumbnail_filename = os.path.splitext(texture_filename)[0] + '.jpg'
        thumbnail_path = os.path.join(thumbnail_folder, thumbnail_filename)
        
        new_brush.icon_filepath = thumbnail_path
