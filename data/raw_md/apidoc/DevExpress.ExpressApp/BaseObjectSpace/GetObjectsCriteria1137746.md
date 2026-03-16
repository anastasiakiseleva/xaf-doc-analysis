---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObjectsCriteria(DevExpress.ExpressApp.DC.ITypeInfo,System.Collections.IList)
name: GetObjectsCriteria(ITypeInfo, IList)
type: Method
summary: Constructs a criteria that can be used to select the specified list of business objects.
syntax:
  content: public CriteriaOperator GetObjectsCriteria(ITypeInfo objectTypeInfo, IList objects)
  parameters:
  - id: objectTypeInfo
    type: DevExpress.ExpressApp.DC.ITypeInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypeInfo) object that provides metadata on the business object's type.
  - id: objects
    type: System.Collections.IList
    description: An [](xref:System.Collections.IList) collection of business objects.
  return:
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) object which is a criterion that can be used to select the specified list of objects.
seealso: []
---
