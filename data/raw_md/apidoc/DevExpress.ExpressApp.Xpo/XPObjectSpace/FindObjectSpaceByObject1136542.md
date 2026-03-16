---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.FindObjectSpaceByObject(System.Object)
name: FindObjectSpaceByObject(Object)
type: Method
summary: Determines the [Object Space](xref:113707) used to load and save a specified persistent object.
syntax:
  content: public static IObjectSpace FindObjectSpaceByObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: The object whose Object Space must be determined.
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object which represents the Object Space used to load and save the specified persistent object. _null_ if the specified object belongs to an XPO **Session** not managed by the **ObjectSpace** class.
seealso: []
---
This method is for internal use. It can access certain [Object Spaces](xref:113707) XAF uses internally (for example, the Object Space used by the [Security System](xref:113366)). Do not use such Object Spaces in your applications because this may cause unexpected behavior. Instead of this, implement the approaches below.

* Within the object's class code, use [Session](xref:DevExpress.Xpo.PersistentBase.Session) and its methods instead of an Object Space.

* In other scenarios, create a new [Object Space](xref:113707) and use the @DevExpress.ExpressApp.IObjectSpace.GetObject(System.Object) method to retrieve an object in the current Object Space. Refer to the method's description to see an example.
