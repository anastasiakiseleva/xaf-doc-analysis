---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObjects``1(DevExpress.Data.Filtering.CriteriaOperator,System.Boolean)
name: GetObjects<T>(CriteriaOperator, Boolean)
type: Method
summary: Returns an **IList** collection of objects of the specified type, retrieved to the current Object Space and filtered according to the specified criteria.
syntax:
  content: public IList<T> GetObjects<T>(CriteriaOperator criteria, bool inTransaction)
  parameters:
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **DevExpress.Data.Filtering.CriteriaOperator** which specifies the criteria for object selection.
  - id: inTransaction
    type: System.Boolean
    description: '**true** if all objects (in the database and retrieved) are processed by the specified criteria; otherwise, **false**. Has effect in XPO only.'
  typeParameters:
  - id: T
    description: ''
  return:
    type: System.Collections.Generic.IList{{T}}
    description: A [](xref:System.Collections.IList) collection that contains the persistent objects of the specified type. Only objects that satisfy the specified criteria will be retrieved to this collection.
seealso: []
---
To get the specified objects, this method invokes a protected virtual **CreateCollection** method that does nothing and returns null. So, the details on how the objects are retrieved depend on how the **CreateCollection** method is overridden in a particular descendant of the **BaseObjectSpace** class.