---
uid: DevExpress.ExpressApp.NonPersistentObjectSpace.GetObjectsCount(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
name: GetObjectsCount(Type, CriteriaOperator)
type: Method
summary: Returns the number of objects specified.
syntax:
  content: public override int GetObjectsCount(Type objectType, CriteriaOperator criteria)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object that identifies the type of objects against which the calculation will be performed.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: The [](xref:DevExpress.Data.Filtering.CriteriaOperator) that specifies the criteria for object selection.
  return:
    type: System.Int32
    description: An integer value that is the count of non-persistent objects that satisfy the specified criteria.
seealso: []
---
You can handle the [NonPersistentObjectSpace.ObjectsCountGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsCountGetting) event to supply custom logic for calculating the **GetObjectsCount** result. 
If the **ObjectsCountGetting** event is not handled, or if the [ObjectsCountGettingEventArgs.Count](xref:DevExpress.ExpressApp.ObjectsCountGettingEventArgs.Count) is _null_, the **GetObjectsCount** method calls the [IObjectSpace.CreateCollection](xref:DevExpress.ExpressApp.IObjectSpace.CreateCollection*) method to calculate the count.