# USDHook4Collisions
This addon enhances Blender’s USD export by automatically adding collision metadata to every mesh. As of now Blender’s default USD export doesn't have an option to include this data, complicating asset imports into game engines like Unreal Engine where collision setup is crucial for playtesting. Without this add-on, users would need to manually add the PhysicsCollisionAPI and PhysicsMeshCollisionAPI to the apiSchemas metadata of each mesh in the .usda file, which is very repetitive and time-consuming. This add-on streamlines the workflow, making USD exports game-ready with collision data fully integrated for seamless staging in engines.

## Install

In Blender, go to Edit -> Preferences, in the Add-ons tab click on the dropdown menu in the top right corner and choose "Install from Disk...". Locate the downloaded addon and press install.

## Disclaimer

This will only work with Unreal Engine 5.4 or newer. Older UE versions don't seem to load this metadata to the UsdAssetCache.
