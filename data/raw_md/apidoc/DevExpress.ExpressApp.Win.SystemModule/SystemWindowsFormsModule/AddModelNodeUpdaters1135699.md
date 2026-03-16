---
uid: DevExpress.ExpressApp.Win.SystemModule.SystemWindowsFormsModule.AddModelNodeUpdaters(DevExpress.ExpressApp.Model.Core.IModelNodeUpdaterRegistrator)
name: AddModelNodeUpdaters(IModelNodeUpdaterRegistrator)
type: Method
summary: Registers [](xref:DevExpress.ExpressApp.Win.SystemModule.SystemWindowsFormsModule) as an updater of [](xref:DevExpress.ExpressApp.Model.IModelLocalization) and [](xref:DevExpress.ExpressApp.Model.IModelOptions) nodes.
syntax:
  content: public override void AddModelNodeUpdaters(IModelNodeUpdaterRegistrator updaterRegistrator)
  parameters:
  - id: updaterRegistrator
    type: DevExpress.ExpressApp.Model.Core.IModelNodeUpdaterRegistrator
    description: An [](xref:DevExpress.ExpressApp.Model.Core.IModelNodeUpdaterRegistrator) object exposing the **AddUpdater** method used to register node updaters in the application.
seealso:
- linkId: DevExpress.ExpressApp.Win.SystemModule.SystemWindowsFormsModule.UpdateNode*
---
This method is not intended to be called from your code. For information on node updaters refer to the [Convert Application Model Differences](xref:112796) topic.