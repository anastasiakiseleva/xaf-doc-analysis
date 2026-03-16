---
uid: DevExpress.ExpressApp.ModuleBase.AddModelNodeUpdaters(DevExpress.ExpressApp.Model.Core.IModelNodeUpdaterRegistrator)
name: AddModelNodeUpdaters(IModelNodeUpdaterRegistrator)
type: Method
summary: Registers node updaters in the application.
syntax:
  content: public virtual void AddModelNodeUpdaters(IModelNodeUpdaterRegistrator updaterRegistrator)
  parameters:
  - id: updaterRegistrator
    type: DevExpress.ExpressApp.Model.Core.IModelNodeUpdaterRegistrator
    description: An [](xref:DevExpress.ExpressApp.Model.Core.IModelNodeUpdaterRegistrator) object exposing the **AddUpdater** method used to register node updaters in the application.
seealso: []
---
Override this method in a module, to register node updaters. For information on node updaters and examples of using this method, refer to the [Convert Application Model Differences](xref:112796) topic.

By default, this method does nothing.