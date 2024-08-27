import bpy
from mathutils import Vector


class BakeSubPivots(bpy.types.Operator):

    bl_idname = "object.bake_sub_pivots"
    bl_label = "Bake Sub Pivots"
    bl_options = {'UNDO'}


    def execute(self, context):
        selected_objects = context.selected_objects
        origin_vertex_indices = [3,4]
        normal_vertex_indices = [1]
        tangent_vertex_indices = [3,4]
        for obj in selected_objects:
            bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
            new_pivot: Vector
            normal: Vector
            new_pivot = Vector((0, 0, 0))
            for v_id in origin_vertex_indices:
                new_pivot += obj.data.vertices[v_id].co / len(origin_vertex_indices)
            normal = Vector((0, 0, 0))
            for v_id in normal_vertex_indices:
                normal += obj.data.vertices[v_id].normal / len(normal_vertex_indices)

            print(f"Sub Pivot: {new_pivot}")
            print(f"Rotation Axis: {normal}")
            pos_xy = obj.data.uv_layers.new(name="PosXY")
            pos_z_n_x = obj.data.uv_layers.new(name="PosZNX")
            n_yz = obj.data.uv_layers.new(name="NYZ")

            for loop in obj.data.loops:
                pos_xy.data[loop.index].uv = new_pivot.xz
                pos_z_n_x.data[loop.index].uv = (new_pivot.y, normal.x)
                n_yz.data[loop.index].uv = normal.zy
        bpy.ops.object.join()
        return {'FINISHED'}



classes = [BakeSubPivots]
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