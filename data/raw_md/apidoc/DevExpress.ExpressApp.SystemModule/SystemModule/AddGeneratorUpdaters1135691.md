---
uid: DevExpress.ExpressApp.SystemModule.SystemModule.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)
name: AddGeneratorUpdaters(ModelNodesGeneratorUpdaters)
type: Method
summary: Registers the **ObjectMethodActionsActionsNodeUpdater** Generator Updater.
syntax:
  content: public override void AddGeneratorUpdaters(ModelNodesGeneratorUpdaters updaters)
  parameters:
  - id: updaters
    type: DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters
    description: A **ModelNodesGeneratorUpdaters** object providing access to the list of Generator Updaters.
seealso:
- linkId: "112810"
---
This method is not intended to be called from your code.

A Generator Updater is a class used to customize the [Application Model](xref:112580)'s zero layer after it has been generated. The **ObjectMethodActionsActionsNodeUpdater** Generator Updater creates [Actions](xref:112622) from method declarations decorated with [](xref:DevExpress.Persistent.Base.ActionAttribute).