import bpy


class BakeSubPivotsSettings(bpy.types.PropertyGroup):
    BSP_bake_mode: bpy.props.EnumProperty(
        name="Pivot resolve mode",
        items=(
            ("VERTICES_MAJOR", "Vertex Data", "Use existing vertices as anchor points"),
            ("PIVOT_MAJOR", "Pivot", "Use pivot as anchor point")
        )
    )
    BSP_origin_vertex_indices_0: bpy.props.IntProperty(name="Origin Vertex 1")
    BSP_origin_vertex_indices_1: bpy.props.IntProperty(name="Origin Vertex 2")
    BSP_normal_vertex_index: bpy.props.IntProperty(name="Rotation axis normal index")

def register():
    from bpy.utils import register_class
    register_class(BakeSubPivotsSettings)
    bpy.types.Scene.bake_sub_pivot_settings = bpy.props.PointerProperty(type=BakeSubPivotsSettings)

def unregister():
    from bpy.utils import unregister_class
    unregister_class(BakeSubPivotsSettings)
    del bpy.types.Scene.bake_sub_pivot_settings