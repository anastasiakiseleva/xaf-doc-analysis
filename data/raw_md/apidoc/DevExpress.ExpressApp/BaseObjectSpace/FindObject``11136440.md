---
uid: DevExpress.ExpressApp.BaseObjectSpace.FindObject``1(DevExpress.Data.Filtering.CriteriaOperator,System.Boolean)
name: FindObject<ObjectType>(CriteriaOperator, Boolean)
type: Method
summary: Searches for the first object of the type designated by the specified generic type parameter, matching the specified criteria.
syntax:
  content: public ObjectType FindObject<ObjectType>(CriteriaOperator criteria, bool inTransaction)
  parameters:
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **DevExpress.Data.Filtering.CriteriaOperator** descendant which is the criteria to match persistent objects.
  - id: inTransaction
    type: System.Boolean
    description: '**true** if all objects (in the database and retrieved) are processed by the specified criteria; otherwise, **false**. Has effect in XPO only.'
  typeParameters:
  - id: ObjectType
    description: ''
  return:
    type: '{ObjectType}'
    description: An object which is the first persistent object which matches the specified criteria. `null` if there is no persistent object which matches the criteria.
seealso: []
---
To find the specified object, this method invokes a public virtual **FindObject** method that does nothing and returns null. So, the details on how the objects are searched depend on how the **FindObject** virtual method is overridden in a particular descendant of the **BaseObjectSpace** class.