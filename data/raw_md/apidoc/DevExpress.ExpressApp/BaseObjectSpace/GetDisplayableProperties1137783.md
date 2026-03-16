---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetDisplayableProperties(System.Object)
name: GetDisplayableProperties(Object)
type: Method
summary: Gets the properties considered visible by the specified collection.
syntax:
  content: public virtual string GetDisplayableProperties(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: A collection whose visible properties will be retrieved.
  return:
    type: System.String
    description: A semicolon-separated list of property names considered visible by a particular collection.
seealso: []
---
This method is intended for internal use. It is supposed to get the properties that must be visible in the specified collection if this collection is of the type with which the current Object Space can operate (e.g. XPCollection for an XPObjectSpace or EFCollection for an EFObjectSpace). When implementing this method, consider the case when a server collection is passed as the _collection_ parameter.