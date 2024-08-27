from bpy.types import Panel

class BakeSubPivotsPanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "VFX Utils"

class BakeSubPivotsMenu(Panel, BakeSubPivotsPanel):
    bl_label = "Bake Sub-Pivots"

    def draw(self, context):
        scn = context.scene

        layout = self.layout
        layout.label(text="Main Element: "+context.active_object.name)

class BakeSubPivotsOptionsMenu(Panel, BakeSubPivotsPanel):
    bl_label = "Baking Options"
    bl_parent_id = "BakeSubPivotsMenu"

    def draw(self, context):
        scn = context.scene

        layout = self.layout
        layout.label(text="Pivot vertex indices")
        layout.prop(scn.bake_sub_pivot_settings, "BSP_bake_mode", text="Pivot Resolution Mode")
        if scn.bake_sub_pivot_settings.BSP_bake_mode == "VERTICES_MAJOR":
            row = layout.row()
            row.prop(scn.bake_sub_pivot_settings, "BSP_origin_vertex_indices_0", text="V0")
            row.prop(scn.bake_sub_pivot_settings, "BSP_origin_vertex_indices_1", text="V1")
            layout.prop(scn.bake_sub_pivot_settings, "BSP_normal_vertex_index", text="Normal Index")
        layout.operator("object.bake_sub_pivots", text="Bake Sub Pivots From Selected Meshes")

classes = [BakeSubPivotsMenu, BakeSubPivotsOptionsMenu]
def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)