---
uid: DevExpress.ExpressApp.BaseObjectSpace.SetDisplayableProperties(System.Object,System.String)
name: SetDisplayableProperties(Object, String)
type: Method
summary: Changes the properties considered visible by a particular collection.
syntax:
  content: public virtual void SetDisplayableProperties(object collection, string displayableProperties)
  parameters:
  - id: collection
    type: System.Object
    description: An object representing the collection whose visible properties will be changed.
  - id: displayableProperties
    type: System.String
    description: A semicolon separated list of property names to be considered visible by a particular collection.
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.SetDisplayableProperties(System.Object,System.String)
  altText: EFCoreObjectSpace.SetDisplayableProperties(Object,String)
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.SetDisplayableProperties(System.Object,System.String)
  altText: XPObjectSpace.SetDisplayableProperties(Object,String)
---
This method is intended for internal use. It is supposed to set the properties that must be visible in the specified collection if this collection is of the type with which the current Object Space can operate. When implementing this method, consider the case when a server collection is passed as the _collection_ parameter.