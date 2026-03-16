---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetDisplayableProperties(System.Object)
name: GetDisplayableProperties(Object)
type: Method
summary: Gets the properties considered visible by the specified collection.
syntax:
  content: public override string GetDisplayableProperties(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: A collection whose visible properties will be retrieved.
  return:
    type: System.String
    description: A semicolon-separated list of property names considered visible by a particular collection.
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.DisplayableProperties
---
This method is used internally by Collection Sources, and generally, you do not need to use it.