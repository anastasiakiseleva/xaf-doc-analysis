---
uid: DevExpress.ExpressApp.CloneObject.CloneObjectModule.GetModuleUpdaters(DevExpress.ExpressApp.IObjectSpace,System.Version)
name: GetModuleUpdaters(IObjectSpace, Version)
type: Method
summary: Returns the list of [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) updaters that handle database updates for the [](xref:DevExpress.ExpressApp.CloneObject.CloneObjectModule) module.
syntax:
  content: public override IEnumerable<ModuleUpdater> GetModuleUpdaters(IObjectSpace objectSpace, Version versionFromDB)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: The Object Space used to update the database.
  - id: versionFromDB
    type: System.Version
    description: The current database version.
  return:
    type: System.Collections.Generic.IEnumerable{DevExpress.ExpressApp.Updating.ModuleUpdater}
    description: An IEnumerable\<[](xref:DevExpress.ExpressApp.Updating.ModuleUpdater)> list of updaters that handle database updates for the [](xref:DevExpress.ExpressApp.CloneObject.CloneObjectModule) module.
seealso: []
---
