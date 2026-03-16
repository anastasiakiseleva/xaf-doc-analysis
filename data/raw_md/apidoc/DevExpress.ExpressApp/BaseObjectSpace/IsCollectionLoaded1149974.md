---
uid: DevExpress.ExpressApp.BaseObjectSpace.IsCollectionLoaded(System.Object)
name: IsCollectionLoaded(Object)
type: Method
summary: Indicates whether a particular collection is loaded with objects from the database.
syntax:
  content: public virtual bool IsCollectionLoaded(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: An object representing the collection for which it must be determined whether it is loaded with objects from the database.
  return:
    type: System.Boolean
    description: '**true**, if the specified collection is loaded with objects from the database; otherwise, **false**.'
seealso: []
---
In [](xref:DevExpress.ExpressApp.BaseObjectSpace), this method always returns false, but this behavior is overridden in descendants (see [EFCoreObjectSpace.IsCollectionLoaded](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.IsCollectionLoaded(System.Object)) and [XPObjectSpace.IsCollectionLoaded](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.IsCollectionLoaded(System.Object))).