import bpy


class BakeSubPivots(bpy.types.Operator):

    bl_idname = "mesh.bake_sub_pivots"
    bl_label = "Bake Sub Pivots"
    bl_options= {'UNDO'}

    def execute(self, context):
        selected_object = context.selected_objects
        new_mesh_data = None


        return {'FINISHED'}



classes = (BakeSubPivots)
def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == '__main__':
    register()