---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.ReloadObject(System.Object)
name: ReloadObject(Object)
type: Method
summary: Reloads the state of the specified persistent object and its aggregated objects from the data store.
syntax:
  content: public override object ReloadObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object which represents the persistent object whose state needs to be reloaded.
  return:
    type: System.Object
    description: The object specified by the _obj_ parameter after it has been reloaded.
seealso: []
---
If the specified persistent object is a new object, the **ReloadObject** method does nothing. To ensure that the persistent object is not a new object, use the [XPObjectSpace.IsNewObject](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.IsNewObject(System.Object)) method.

It is not required that the specified object belong to the current Object Space. If it does not belong, it is retrieved by the current Object Space, and then its state is reloaded.

A **CannotReloadPurgedObjectException** is thrown if the specified persistent object is permanently deleted from the data store.