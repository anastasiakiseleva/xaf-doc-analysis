---
uid: DevExpress.ExpressApp.Model.ModelSynchronizer.ApplyModel
name: ApplyModel()
type: Method
summary: Sets up the [ModelSynchronizer.Control](xref:DevExpress.ExpressApp.Model.ModelSynchronizer.Control), according to the configuration stored in the [Application Model](xref:112580)'s [ModelSynchronizer.Model](xref:DevExpress.ExpressApp.Model.ModelSynchronizer.Model) node.
syntax:
  content: public void ApplyModel()
seealso: []
---
When implementing a custom model synchronizer by deriving from the **ModelSynchronizer** class, override the protected **ApplyModelCore** method to check the [ModelSynchronizer.Model](xref:DevExpress.ExpressApp.Model.ModelSynchronizer.Model) property and configure the [ModelSynchronizer.Control](xref:DevExpress.ExpressApp.Model.ModelSynchronizer.Control) accordingly.