---
uid: DevExpress.ExpressApp.IObjectSpace.IsObjectDeletionOnRemoveEnabled(System.Object)
name: IsObjectDeletionOnRemoveEnabled(Object)
type: Method
summary: Indicates whether the deletion of persistent objects from the data source when they are removed from the specified collection is enabled.
syntax:
  content: bool IsObjectDeletionOnRemoveEnabled(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: A collection of persistent objects whose removal from the database is requested along with their removal from the collection.
  return:
    type: System.Boolean
    description: '**true**, if deletion from the database along with removal from the collection is enabled; **false**, if disabled.'
seealso:
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.IsObjectDeletionOnRemoveEnabled(System.Object)
---
This property is intended for internal use. It is supposed to determine whether the object deletion from the database along with their removal from the specified collection is enabled, if this collection is of the type with which the current Object Space can operate (e.g. XPCollection for an XPObjectSpace or EFCollection for an EFObjectSpace). When implementing this property, consider the case when a server collection is passed as the _collection_ parameter.