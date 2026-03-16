---
uid: DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsCountGetting
name: ObjectsCountGetting
type: Event
summary: Occurs when the [NonPersistentObjectSpace.GetObjectsCount](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.GetObjectsCount(System.Type,DevExpress.Data.Filtering.CriteriaOperator)) method is called.
syntax:
  content: public event EventHandler<ObjectsCountGettingEventArgs> ObjectsCountGetting
seealso: []
---
Handle the **ObjectsCountGetting** event and pass a custom count value to the [ObjectsCountGettingEventArgs.Count](xref:DevExpress.ExpressApp.ObjectsCountGettingEventArgs.Count) parameter. If **ObjectsCountGetting** is not handled or if **Count** is set to _null_, the **GetObjectsCount** method calls the [IObjectSpace.CreateCollection](xref:DevExpress.ExpressApp.IObjectSpace.CreateCollection*) method to calculate the count.