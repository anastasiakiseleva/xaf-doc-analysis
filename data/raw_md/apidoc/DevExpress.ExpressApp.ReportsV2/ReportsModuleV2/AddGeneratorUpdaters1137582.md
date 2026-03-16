---
uid: DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)
name: AddGeneratorUpdaters(ModelNodesGeneratorUpdaters)
type: Method
summary: Registers the Generator Updater of the Reports V2 Module.
syntax:
  content: public override void AddGeneratorUpdaters(ModelNodesGeneratorUpdaters updaters)
  parameters:
  - id: updaters
    type: DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters
    description: A **ModelNodesGeneratorUpdaters** object providing access to the list of Generator Updaters.
seealso: []
---
This method is not intended to be called from your code.

A Generator Updater is a class used to customize the [Application Model](xref:112580)'s zero layer after it has been generated. The **Reports V2 Module**  creates a **Reports** navigation item if the type specified by the [ReportsModuleV2.ReportDataType](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportDataType) property is not decorated with the [](xref:DevExpress.Persistent.Base.NavigationItemAttribute).