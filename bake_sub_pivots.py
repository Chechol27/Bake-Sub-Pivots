import bpy
from mathutils import Vector


class BakeSubPivots(bpy.types.Operator):

    bl_idname = "object.bake_sub_pivots"
    bl_label = "Bake Sub Pivots"
    bl_options = {'UNDO'}

    layer_names = ["PosXY", "PosZNX", "NYZ"]

    @staticmethod
    def calculate_pivot_from_vertex_indices(context: bpy.types.Context, obj: bpy.types.Object) -> (Vector, Vector):
        scene = context.scene
        settings = scene.bake_sub_pivot_settings
        origin_vertex_indices = [settings.BSP_origin_vertex_indices_0, settings.BSP_origin_vertex_indices_1]
        normal_vertex_indices = [settings.BSP_normal_vertex_index]
        new_pivot: Vector = Vector((0, 0, 0))
        normal: Vector = Vector((0, 0, 0))
        for v_id in origin_vertex_indices:
            new_pivot += obj.data.vertices[v_id].co / len(origin_vertex_indices)
        for v_id in normal_vertex_indices:
            normal += obj.data.vertices[v_id].normal / len(normal_vertex_indices)
        return new_pivot, normal

    @staticmethod
    def calculate_pivot_from_object_pivot(obj: bpy.types.Object) -> (Vector, Vector):
        new_pivot = obj.matrix_world.to_translation().xzy
        normal = Vector((0, 0, 0))
        all_normals = [v.normal for v in obj.data.vertices]
        for n in all_normals:
            normal += n / len(all_normals)
        return new_pivot, normal.xzy

    def execute(self, context: bpy.types.Context):
        selected_objects = context.selected_objects
        baking_mode = context.scene.bake_sub_pivot_settings.BSP_bake_mode
        for obj in selected_objects:
            if baking_mode == "VERTICES_MAJOR":
                new_pivot, normal = BakeSubPivots.calculate_pivot_from_vertex_indices(context, obj)
            else:
                new_pivot, normal = BakeSubPivots.calculate_pivot_from_object_pivot(obj)

            print(f"Sub Pivot: {new_pivot}")
            print(f"Rotation Axis: {normal}")

            uv_layer_names = [layer.name for layer in obj.data.uv_layers]
            for layer_name in self.layer_names:
                if layer_name in uv_layer_names:
                    obj.data.uv_layers.remove(obj.data.uv_layers[layer_name])

            pos_xy = obj.data.uv_layers.new(name=self.layer_names[0])
            pos_z_n_x = obj.data.uv_layers.new(name=self.layer_names[1])
            n_yz = obj.data.uv_layers.new(name=self.layer_names[2])
            new_pivot *= Vector((-1, -1, 1))
            normal *= Vector((-1, -1, 1))
            for loop in obj.data.loops:
                pos_xy.data[loop.index].uv = new_pivot.xz
                pos_z_n_x.data[loop.index].uv = (new_pivot.y, normal.x)
                n_yz.data[loop.index].uv = normal.zy
        bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
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