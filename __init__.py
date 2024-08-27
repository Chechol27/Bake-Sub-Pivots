bl_info = {
    "name": "Mesh Sub-pivots baker",
    "author": "Sergio Peñaloza",
    "blender": (4, 0, 0),
    "version": (1, 0, 0),
    "location": "Object > VFX Utils > Bake Sub Pivots",
    "description": "Join loose geometry, Calculates virtual pivots, and store that data in a unified mesh's vertex buffer to avoid partilce-like behaviour in a non-particle renderer and save draw calls",
    "category": "Modeling",
    "doc_url": "https://github.com"
}

if "bpy" in locals():
    import importlib
    if "property_settings" in locals():
        importlib.reload(property_settings)
    if "menu_ui" in locals():
        importlib.reload(menu_ui)
    if "bake_sub_pivots" in locals():
        importlib.reload(bake_sub_pivots)


import bpy
from . import property_settings
from . import menu_ui
from . import bake_sub_pivots


def register():
    property_settings.register()
    menu_ui.register()
    bake_sub_pivots.register()


def unregister():
    bake_sub_pivots.unregister()
    menu_ui.unregister()
    property_settings.unregister()


if __name__ == '__main__':
    register()