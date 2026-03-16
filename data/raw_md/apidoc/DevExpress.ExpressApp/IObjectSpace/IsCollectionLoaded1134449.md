---
uid: DevExpress.ExpressApp.IObjectSpace.IsCollectionLoaded(System.Object)
name: IsCollectionLoaded(Object)
type: Method
summary: Indicates whether a particular collection is loaded with objects from the database.
syntax:
  content: bool IsCollectionLoaded(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: An object representing the collection for which it must be determined whether it is loaded with objects from the database.
  return:
    type: System.Boolean
    description: '**true**, if the specified collection is loaded with objects from the database; otherwise, **false**.'
seealso: []
---
As a rule, an Object Space works with particular types of collections. These collection types are the ones that are used for [Client](xref:118449) and [Server](xref:118450) modes. This method is intended to request whether the passed collection has objects loaded.