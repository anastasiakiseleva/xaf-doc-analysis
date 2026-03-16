---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.IsDeletionDeferredType(System.Type)
name: IsDeletionDeferredType(Type)
type: Method
summary: Returns a value that indicates if the deferred deletion is enabled for persistent objects of a given type.
syntax:
  content: public override bool IsDeletionDeferredType(Type type)
  parameters:
  - id: type
    type: System.Type
    description: A [](xref:System.Type) object that is a type of persistent object.
  return:
    type: System.Boolean
    description: '**true**, if the deferred deletion is enabled; otherwise - **false**.'
seealso:
- linkId: "2026"
---
Deferred deletion assumes that a record is not immediately deleted in the underlying data store when the [IObjectSpace.Delete](xref:DevExpress.ExpressApp.IObjectSpace.Delete*) is executed. Instead, the record is marked as deleted.