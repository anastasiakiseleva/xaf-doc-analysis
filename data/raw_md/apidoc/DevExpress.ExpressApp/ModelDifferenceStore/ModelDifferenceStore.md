---
uid: DevExpress.ExpressApp.ModelDifferenceStore
name: ModelDifferenceStore
type: Class
summary: The base class for classes that provide writable storage for the [Application Model](xref:112580) differences.
syntax:
  content: 'public abstract class ModelDifferenceStore : ModelStoreBase'
seealso:
- linkId: DevExpress.ExpressApp.ModelDifferenceStore._members
  altText: ModelDifferenceStore Members
---
Inherit this class to implement a custom writable storage for model differences. To use the implemented storage instead of the default, handle the [XafApplication.CreateCustomModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomModelDifferenceStore) and/or [XafApplication.CreateCustomUserModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomUserModelDifferenceStore) events.
