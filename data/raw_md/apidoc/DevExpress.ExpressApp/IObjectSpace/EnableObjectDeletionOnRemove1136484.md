---
uid: DevExpress.ExpressApp.IObjectSpace.EnableObjectDeletionOnRemove(System.Object,System.Boolean)
name: EnableObjectDeletionOnRemove(Object, Boolean)
type: Method
summary: Enables/disables the deletion of persistent objects from the data source when they are removed from the specified collection.
syntax:
  content: void EnableObjectDeletionOnRemove(object collection, bool enable)
  parameters:
  - id: collection
    type: System.Object
    description: A collection of persistent objects whose removal is requested from the database, along with their removal from the collection.
  - id: enable
    type: System.Boolean
    description: '**true**, to enable the object deletion from the database along with its removal from the collection; **false**, to disable it.'
seealso:
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.EnableObjectDeletionOnRemove(System.Object,System.Boolean)
---
This property is intended for internal use. It is supposed to enable/disable object deletion from the database along with its removal from the specified collection if this collection is of the type with which the current Object Space can operate (e.g. XPCollection for an XPObjectSpace or EFCollection for an EFObjectSpace). When implementing this property, consider the case when a server collection is passed as the _collection_ parameter.