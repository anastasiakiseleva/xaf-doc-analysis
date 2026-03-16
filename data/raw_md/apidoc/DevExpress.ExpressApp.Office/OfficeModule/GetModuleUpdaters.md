---
uid: DevExpress.ExpressApp.Office.OfficeModule.GetModuleUpdaters(DevExpress.ExpressApp.IObjectSpace,System.Version)
name: GetModuleUpdaters(IObjectSpace, Version)
type: Method
summary: Returns the list of [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) updaters that handle database updates for the [](xref:DevExpress.ExpressApp.Office.OfficeModule) module.
syntax:
  content: public override IEnumerable<ModuleUpdater> GetModuleUpdaters(IObjectSpace objectSpace, Version versionFromDB)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object which represents the Object Space used to update the database.
  - id: versionFromDB
    type: System.Version
    description: A **System.Version** object that represents the current database version.
  return:
    type: System.Collections.Generic.IEnumerable{DevExpress.ExpressApp.Updating.ModuleUpdater}
    description: An IEnumerable\<[](xref:DevExpress.ExpressApp.Updating.ModuleUpdater)> list of updaters that handle database updates for the [](xref:DevExpress.ExpressApp.Office.OfficeModule) module.
seealso: []
---
