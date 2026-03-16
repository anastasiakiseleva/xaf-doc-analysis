---
uid: DevExpress.ExpressApp.BaseObjectSpace.FindObjectSpaceByObject(System.Object)
name: FindObjectSpaceByObject(Object)
type: Method
summary: Returns the [Object Space](xref:113707) used to load and save a specified persistent object. This method is for internal use.
syntax:
  content: public static IObjectSpace FindObjectSpaceByObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: The object whose Object Space this method returns.
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An Object Space used to load and save the specified persistent object. _null_ if the specified object does not belong to any Object Space.
seealso: []
---
This method is for internal use. It can access certain [Object Spaces](xref:113707) XAF uses internally (for example, the Object Space used by the [Security System](xref:113366)). Do not use such Object Spaces in your applications because this may cause unexpected behavior. Instead of this, implement the approaches below.

To access an object's Object Space in the class code, use one of the following options:
- Implement the @DevExpress.ExpressApp.IObjectSpaceLink interface in non-persistent classes.
- Use the automatically implemented @DevExpress.ExpressApp.IObjectSpaceLink interface in EF Core classes.
- Use the object's [Session](xref:DevExpress.Xpo.PersistentBase.Session) in XPO persistent classes.

In other cases, create a new [Object Space](xref:113707) and use the @DevExpress.ExpressApp.IObjectSpace.GetObject(System.Object) method to retrieve an object in the current Object Space.
