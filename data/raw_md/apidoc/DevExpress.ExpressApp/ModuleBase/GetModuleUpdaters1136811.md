---
uid: DevExpress.ExpressApp.ModuleBase.GetModuleUpdaters(DevExpress.ExpressApp.IObjectSpace,System.Version)
name: GetModuleUpdaters(IObjectSpace, Version)
type: Method
summary: Returns the list of [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) updaters that handle database updates for the [](xref:DevExpress.ExpressApp.ModuleBase) module.
syntax:
  content: public virtual IEnumerable<ModuleUpdater> GetModuleUpdaters(IObjectSpace objectSpace, Version versionFromDB)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object which represents the Object Space used to update the database.
  - id: versionFromDB
    type: System.Version
    description: A **System.Version** object which represents the current database version.
  return:
    type: System.Collections.Generic.IEnumerable{DevExpress.ExpressApp.Updating.ModuleUpdater}
    description: An IEnumerable\<[](xref:DevExpress.ExpressApp.Updating.ModuleUpdater)> list of updaters that handle database updates for the [](xref:DevExpress.ExpressApp.ModuleBase) module.
seealso: []
---
This method collects module updaters declared in the current module's assembly via the reflection. In your custom module, you can override this method to explictly specify required module updaters and thus, avoid the use of reflection and improve performance.
When you create a module updater class, register it in the overridden **GetModuleUpdaters** method.

# [C#](#tab/tabid-csharp)

```csharp
public class MyModule : ModuleBase {
    // ...
    public override IEnumerable<ModuleUpdater> GetModuleUpdaters(
        IObjectSpace objectSpace, Version versionFromDB) {
        return new ModuleUpdater[] { new Updater(objectSpace, versionFromDB) };
    }
}
```
***
This code is already added to a module template. Change it if you need to register extra module updater classes. If your custom module is not supposed to provide any updates to the database, then override the method as follows.

# [C#](#tab/tabid-csharp)

```csharp
public override IEnumerable<ModuleUpdater> GetModuleUpdaters(
    IObjectSpace objectSpace, Version versionFromDB) {
     return ModuleUpdater.EmptyModuleUpdaters;
}
```
***