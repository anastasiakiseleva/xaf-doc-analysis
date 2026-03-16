---
uid: DevExpress.ExpressApp.Model.ModelSynchronizer
name: ModelSynchronizer
type: Class
summary: A basic implementation of a model synchronizer.
syntax:
  content: 'public abstract class ModelSynchronizer : IModelSynchronizable, IDisposable'
seealso:
- linkId: DevExpress.ExpressApp.Model.ModelSynchronizer._members
  altText: ModelSynchronizer Members
---
The **ModelSynchronizer** class provides a basic implementation of the [](xref:DevExpress.ExpressApp.Model.IModelSynchronizable) interface. Note that when creating a custom model synchronizer, it is recommended that you derive from the [](xref:DevExpress.ExpressApp.Model.ModelSynchronizer`2) class. Its implementation already contains the necessary infrastructure code so that you can focus on the model synchronization logic.