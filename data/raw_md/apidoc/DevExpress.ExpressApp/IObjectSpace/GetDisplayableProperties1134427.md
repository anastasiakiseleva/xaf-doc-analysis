---
uid: DevExpress.ExpressApp.IObjectSpace.GetDisplayableProperties(System.Object)
name: GetDisplayableProperties(Object)
type: Method
summary: Gets the properties considered visible by the specified collection.
syntax:
  content: string GetDisplayableProperties(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: A collection whose visible properties will be retrieved.
  return:
    type: System.String
    description: A semicolon separated list of property names considered visible by a particular collection.
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.GetDisplayableProperties(System.Object)
  altText: EFCoreObjectSpace.GetDisplayableProperties(Object)
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetDisplayableProperties(System.Object)
  altText: XPObjectSpace.GetDisplayableProperties(Object)
---
This method is intended for internal use. It is supposed to return a semicolon separated list of property names considered visible by a particular collection if this collection is of the type with which the current Object Space can operate. When implementing this method, consider the case when a server collection is passed as the _collection_ parameter.