---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.ReloadCollection(System.Object)
name: ReloadCollection(Object)
type: Method
summary: Clears the specified collection and reloads its contents from a database.
syntax:
  content: public override void ReloadCollection(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: A collection this method reloads.
seealso: []
---
This method reloads the collection if it is of the **EFCoreCollection** type.

To reload a single object, use the @DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.ReloadObject(System.Object) method instead of **ReloadCollection**.