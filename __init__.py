bl_info = {
    "name": "Mesh Sub-pivots baker",
    "author": "Sergio Peñaloza",
    "version": (1, 0, 0),
    "location": "Mesh > VFX Utils > Bake Sub Pivots",
    "description": "Join loose geometry, Calculates virtual pivots, and store that data in a unified mesh's vertex buffer to avoid partilce-like behaviour in a non-particle renderer and save draw calls",
    "category": "Modeling",
    "doc_url": "https://github.com"
}

if "bpy" in locals():
    import importlib
    if "bake_sub_pivots" in locals():
        importlib.reload(bake_sub_pivots)


from . import bake_sub_pivots


def register():
    bake_sub_pivots.register()


def unregister():
    bake_sub_pivots.unregister()


if __name__ == '__main__':
    register()