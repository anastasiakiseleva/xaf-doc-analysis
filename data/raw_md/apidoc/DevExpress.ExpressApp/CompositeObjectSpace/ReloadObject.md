---
uid: DevExpress.ExpressApp.CompositeObjectSpace.ReloadObject(System.Object)
name: ReloadObject(Object)
type: Method
summary: Updates the specified object in the current Object Space with data from the data source.
syntax:
  content: public override object ReloadObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object to be reloaded from the data source.
  return:
    type: System.Object
    description: The reloaded object.
seealso: []
---
If the specified object is a new object, the **ReloadObject** method does nothing. To ensure that the object is not a new object, use the @DevExpress.ExpressApp.IObjectSpace.IsNewObject(System.Object) method.

If the specified object does not belong to the current Object Space, the **ReloadObject** method retrieves this object to the current Object Space, and then reloads its state.

A **CannotReloadPurgedObjectException** is thrown if the specified persistent object is deleted from the data store.