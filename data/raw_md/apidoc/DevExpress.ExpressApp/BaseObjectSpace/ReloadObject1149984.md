---
uid: DevExpress.ExpressApp.BaseObjectSpace.ReloadObject(System.Object)
name: ReloadObject(Object)
type: Method
summary: Updates the specified object in the current Object Space with data from the data source.
syntax:
  content: public virtual object ReloadObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object which represents the persistent object whose state needs to be reloaded.
  return:
    type: System.Object
    description: The object specified by the _obj_ parameter after it has been reloaded.
seealso: []
---
If the specified persistent object is a new object, the **ReloadObject** method does nothing. To ensure that the persistent object is not a new object, use the [BaseObjectSpace.IsNewObject](xref:DevExpress.ExpressApp.BaseObjectSpace.IsNewObject(System.Object)) method.