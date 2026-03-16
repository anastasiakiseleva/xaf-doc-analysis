---
uid: DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.FindReportsModule(DevExpress.ExpressApp.ModuleList)
name: FindReportsModule(ModuleList)
type: Method
summary: Searches for a [](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2) instance in a particular module list.
syntax:
  content: public static ReportsModuleV2 FindReportsModule(ModuleList modules)
  parameters:
  - id: modules
    type: DevExpress.ExpressApp.ModuleList
    description: A `ModuleList` object, which is a collection of modules.
  return:
    type: DevExpress.ExpressApp.ReportsV2.ReportsModuleV2
    description: A [](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2) instance found in the _modules_ module list.
seealso: []
---
If no `ReportsModule` instances are contained in the _modules_ collection, the method returns `null`. If there is more than one instance in the collection, the method throws an `InvalidOperationException`.