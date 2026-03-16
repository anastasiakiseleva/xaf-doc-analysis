---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetAssociatedCollectionCriteria(System.Object,DevExpress.ExpressApp.DC.IMemberInfo)
name: GetAssociatedCollectionCriteria(Object, IMemberInfo)
type: Method
summary: Returns the criteria applied to a specific object's associated collection property.
syntax:
  content: public CriteriaOperator GetAssociatedCollectionCriteria(object obj, IMemberInfo memberInfo)
  parameters:
  - id: obj
    type: System.Object
    description: An object whose collection property's criteria must be retrieved.
  - id: memberInfo
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: An [](xref:DevExpress.ExpressApp.DC.IMemberInfo) object supplying metadata on the associated collection property.
  return:
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **CriteriaOperator** object that is the criteria applied to the specified object's associated collection property.
seealso: []
---
