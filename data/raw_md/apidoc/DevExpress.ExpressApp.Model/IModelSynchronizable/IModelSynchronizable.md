---
uid: DevExpress.ExpressApp.Model.IModelSynchronizable
name: IModelSynchronizable
type: Interface
summary: Declares members implemented by classes used to persist the configuration of an entity into the [Application Model](xref:112580).
syntax:
  content: public interface IModelSynchronizable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelSynchronizable._members
  altText: IModelSynchronizable Members
---
This interface is implemented by various built-in XAF classes and exposes two methods. The [IModelSynchronizable.ApplyModel](xref:DevExpress.ExpressApp.Model.IModelSynchronizable.ApplyModel) method persists the configuration of an entity into the Application Model. The [IModelSynchronizable.SynchronizeModel](xref:DevExpress.ExpressApp.Model.IModelSynchronizable.SynchronizeModel) method sets up the entity according to the configuration stored in the Application Model.

One of the built-in classes implementing the **IModelSynchronizable** interface is the [](xref:DevExpress.ExpressApp.Editors.ListEditor) class. To ensure correct functioning, each [built-in List Editor](xref:113189) overrides the protected **ListEditor.CreateModelSynchronizer** method, to create a specific model synchronizer. This model synchronizer's methods are called by XAF via the [ListEditor.ApplyModel](xref:DevExpress.ExpressApp.Editors.ListEditor.ApplyModel) and [ListEditor.SaveModel](xref:DevExpress.ExpressApp.Editors.ListEditor.SaveModel) methods. You can specify an additional custom model synchronizer to be used by a built-in List Editor by handling its `DevExpress.ExpressApp.Editors.ListEditor.CreateCustomModelSynchronizer` event.

When creating a custom model synchronizer, it is recommended that you derive from the [](xref:DevExpress.ExpressApp.Model.ModelSynchronizer`2) class. Its implementation already contains the necessary infrastructure code so that you can focus on the model synchronization logic.