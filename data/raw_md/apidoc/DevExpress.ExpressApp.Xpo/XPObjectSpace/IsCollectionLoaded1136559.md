---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.IsCollectionLoaded(System.Object)
name: IsCollectionLoaded(Object)
type: Method
summary: Indicates whether a particular collection is loaded with objects from the database.
syntax:
  content: public override bool IsCollectionLoaded(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: An object representing the collection for which it must be determined whether it is loaded with objects from the database.
  return:
    type: System.Boolean
    description: '**true**, if the specified collection is loaded with objects from the database; otherwise, **false**.'
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.IsLoaded
---
This method is used internally by Collection Sources, and generally, you do not need to use it.
For server collections this method always returns **true**.