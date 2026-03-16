---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.ReloadObject(System.Object)
name: ReloadObject(Object)
type: Method
summary: Updates the specified object in the current Object Space's [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext) with data from the data source.
syntax:
  content: public override object ReloadObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: A persistent object this method reloads from the database.
  return:
    type: System.Object
    description: An object to be reloaded from the database.
seealso: []
---
If the specified persistent object is a new object, the **ReloadObject** method does nothing. To ensure that the persistent object is not new, use the [EFCoreObjectSpace.IsNewObject](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.IsNewObject(System.Object)) method.

If the specified object does not belong to the current Object Space, this method returns the object as is.

To reload a collection, use the @DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.ReloadCollection(System.Object) method instead of **ReloadObject**.