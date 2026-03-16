---
uid: DevExpress.ExpressApp.IObjectSpace.CanApplyCriteria(System.Type)
name: CanApplyCriteria(Type)
type: Method
summary: Indicates whether collections of a particular type can be filtered on the server side.
syntax:
  content: bool CanApplyCriteria(Type collectionType)
  parameters:
  - id: collectionType
    type: System.Type
    description: A [](xref:System.Type) object specifying the type of collections whose server-side filtering capability must be determined.
  return:
    type: System.Boolean
    description: '**true**, if collections of the specified type can be filtered on the server side; otherwise, **false**.'
seealso:
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.CanApplyCriteria(System.Type)
  altText: EFCoreObjectSpace.CanApplyCriteria(Type)
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.CanApplyCriteria(System.Type)
  altText: XPObjectSpace.CanApplyCriteria(Type)
---
In this method, check whether the collection type passed as the _collectionType_ parameter supports applying criteria. As a rule, an Object Space works with particular types of collections. These collection types are the ones that are used for [Client](xref:118449) and [Server](xref:118450) modes.