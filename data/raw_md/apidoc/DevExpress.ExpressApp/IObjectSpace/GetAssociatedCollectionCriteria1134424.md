---
uid: DevExpress.ExpressApp.IObjectSpace.GetAssociatedCollectionCriteria(System.Object,DevExpress.ExpressApp.DC.IMemberInfo)
name: GetAssociatedCollectionCriteria(Object, IMemberInfo)
type: Method
summary: Specifies the criteria applied to a specific object's associated collection property.
syntax:
  content: CriteriaOperator GetAssociatedCollectionCriteria(object obj, IMemberInfo memberInfo)
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
When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, you don't have to implement the **GetAssociatedCollectionCriteria** method. It's implemented by the **BaseObjectSpace** class. However, you can override the **BaseOBjectSpace.GetAssociatedCollectionCriteriaCore** method, which is invoked by the **BaseObjectSpace.GetAssociatedCollectionCriteria** method, if you need to replace the base implementation with a custom one.