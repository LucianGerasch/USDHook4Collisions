bl_info = {
    "name": "USDHook4Collisions",
    "blender": (4, 0, 0),
    "category": "Import-Export",
    "version": (1, 0, 0),
    "author": "Lucian Gerasch",
    "description": "Automatically adds collision metadata for all meshes in an USD export",
}

import bpy
import bpy.types
import pxr.Sdf as Sdf
import pxr.UsdGeom as UsdGeom

class USDHookCollision(bpy.types.USDHook):
    bl_idname = "usd_hook_collision"
    bl_label = "USD Export with collision"

    @staticmethod
    def on_export(export_context):
        stage = export_context.get_stage()

        if stage is None:
            return False

        for prim in stage.Traverse():
            if prim.IsA(UsdGeom.Mesh):

                api_schemas = prim.GetMetadata('apiSchemas')

                if api_schemas:
                    current_schemas = api_schemas.GetAddedOrExplicitItems()
                else:
                    current_schemas = []

                schemas_set = set(current_schemas)

                new_schemas = ["PhysicsCollisionAPI", "PhysicsMeshCollisionAPI"]
                schemas_set.update(new_schemas)

                updated_api_schemas = list(schemas_set)
                token_list_op = Sdf.TokenListOp()
                token_list_op.prependedItems = updated_api_schemas

                prim.SetMetadata('apiSchemas', token_list_op)

        return True

def register():
    bpy.utils.register_class(USDHookCollision)

def unregister():
    bpy.utils.unregister_class(USDHookCollision)

if __name__ == "__main__":
    register()