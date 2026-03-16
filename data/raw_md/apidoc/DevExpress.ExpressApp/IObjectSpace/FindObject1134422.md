---
uid: DevExpress.ExpressApp.IObjectSpace.FindObject(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
name: FindObject(Type, CriteriaOperator)
type: Method
summary: Searches for the first object that matches the specified criteria and is of the specified type. The search takes uncommitted changes into account.
syntax:
  content: object FindObject(Type objectType, CriteriaOperator criteria)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object which is the type of objects to search for.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) descendant which is the criteria to match persistent objects.
  return:
    type: System.Object
    description: An object which is  the first persistent object which matches the specified criteria. `null` if there is no persistent object which matches the criteria.
seealso:
- linkId: "113711"
---

[!include[](~/templates/objectspace_getobject.md)]

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, you don't have to implement the **FindObject** method. The **BaseObjectSpace** class' **FindObject(Type objectType, CriteriaOperator criteria)** method invokes a public virtual **FindObject(Type objectType, CriteriaOperator criteria, Boolean inTransaction)** method passing **true** as the _inTransaction_ parameter. So, to implement an object search, override the public virtual **BaseObjectSpace.FindObject** method.