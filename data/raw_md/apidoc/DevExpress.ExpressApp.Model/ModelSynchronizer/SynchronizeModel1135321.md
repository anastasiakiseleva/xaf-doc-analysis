---
uid: DevExpress.ExpressApp.Model.ModelSynchronizer.SynchronizeModel
name: SynchronizeModel()
type: Method
summary: Persists the [ModelSynchronizer.Control](xref:DevExpress.ExpressApp.Model.ModelSynchronizer.Control)'s configuration to the [Application Model](xref:112580)'s [ModelSynchronizer.Model](xref:DevExpress.ExpressApp.Model.ModelSynchronizer.Model) node.
syntax:
  content: public abstract void SynchronizeModel()
seealso: []
---
When implementing a custom model synchronizer by deriving from the [](xref:DevExpress.ExpressApp.Model.ModelSynchronizer) class, override the **SynchronizeModel** method to check the [ModelSynchronizer.Control](xref:DevExpress.ExpressApp.Model.ModelSynchronizer.Control) property and configure the Application Model via the [ModelSynchronizer.Model](xref:DevExpress.ExpressApp.Model.ModelSynchronizer.Model) property accordingly.