---
uid: DevExpress.ExpressApp.BaseObjectSpace.CanApplyCriteria(System.Type)
name: CanApplyCriteria(Type)
type: Method
summary: Indicates whether collections of a particular type can be filtered on the server side.
syntax:
  content: public virtual bool CanApplyCriteria(Type collectionType)
  parameters:
  - id: collectionType
    type: System.Type
    description: A [](xref:System.Type) object specifying the type of collections whose server-side filtering capability must be determined.
  return:
    type: System.Boolean
    description: '**true**, if collections of the specified type can be filtered on the server side; otherwise, **false**.'
seealso: []
---
Generally, you do not need to use this method, since it is intended for internal use.