---
uid: DevExpress.ExpressApp.IObjectSpace.CreateServerCollection(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
name: CreateServerCollection(Type, CriteriaOperator)
type: Method
summary: Creates a [Server](xref:118450) mode collection of objects specified by the _objectType_ parameter.
syntax:
  content: object CreateServerCollection(Type objectType, CriteriaOperator criteria)
  parameters:
  - id: objectType
    type: System.Type
    description: The type of persistent objects to include in the collection.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: The **DevExpress.Data.Filtering.CriteriaOperator** that specifies the criteria for object selection in a data store.
  return:
    type: System.Object
    description: A server collection that includes the persistent objects of the specified type. In addition, only objects that satisfy the specified criteria will be retrieved to this collection.
seealso:
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.CreateServerCollection(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
  altText: EFCoreObjectSpace.CreateServerCollection(Type,CriteriaOperator)
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.CreateServerCollection(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
  altText: XPObjectSpace.CreateServerCollection(Type,CriteriaOperator)
---
The newly created collection uses the current Object Space to load and save persistent objects.