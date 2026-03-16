---
uid: DevExpress.ExpressApp.ModelStoreBase
name: ModelStoreBase
type: Class
summary: The base class for classes that provide a readonly storage for the [Application Model](xref:112580) differences.
syntax:
  content: public abstract class ModelStoreBase
seealso:
- linkId: DevExpress.ExpressApp.ModelStoreBase._members
  altText: ModelStoreBase Members
---
Inherit this class to implement a custom readonly storage for model differences. To use the implemented storage instead of the default, handle the [XafApplication.CreateCustomModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomModelDifferenceStore) and/or [XafApplication.CreateCustomUserModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomUserModelDifferenceStore) events.