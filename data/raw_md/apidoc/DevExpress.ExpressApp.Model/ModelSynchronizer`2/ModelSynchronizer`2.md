---
uid: DevExpress.ExpressApp.Model.ModelSynchronizer`2
name: ModelSynchronizer<T, V>
type: Class
summary: The recommended base class to use for model synchronizers.
syntax:
  content: 'public abstract class ModelSynchronizer<T, V> : ModelSynchronizer'
  typeParameters:
  - id: T
    description: ''
  - id: V
    description: ''
seealso:
- linkId: DevExpress.ExpressApp.Model.ModelSynchronizer`2._members
  altText: ModelSynchronizer<T, V> Members
---
To create a custom model synchronizer by deriving from the **ModelSynchronizer\<T, V>** class, override two methods. Override the protected **ApplyModelCore** method to check the [ModelSynchronizer`2.Model](xref:DevExpress.ExpressApp.Model.ModelSynchronizer`2.Model) property and configure the [ModelSynchronizer.Control](xref:DevExpress.ExpressApp.Model.ModelSynchronizer.Control) accordingly. Override the [ModelSynchronizer.SynchronizeModel](xref:DevExpress.ExpressApp.Model.ModelSynchronizer.SynchronizeModel) method to check the **Control** property and configure the Application Model via the **Model** property accordingly.