---
uid: DevExpress.ExpressApp.CollectionSourceBase.GetEnumerable``1(System.Boolean)
name: GetEnumerable<T>(Boolean)
type: Method
summary: Returns a strongly-typed sequence ([](xref:System.Collections.Generic.IEnumerable`1) or [](xref:System.Linq.IQueryable`1)) that contains objects from the original collection.
syntax:
  content: public IEnumerable<T> GetEnumerable<T>(bool wrapNotifications = true)
  parameters:
  - id: wrapNotifications
    type: System.Boolean
    defaultValue: "True"
    description: '**true** if the returned sequence should implement the @System.Collections.Specialized.INotifyCollectionChanged interface; otherwise, **false**. The method considers this parameter only if the original collection implements the @System.ComponentModel.IBindingList interface.'
  typeParameters:
  - id: T
    description: The type of objects in the sequence. This parameter should match the [CollectionSourceBase.ObjectTypeInfo](xref:DevExpress.ExpressApp.CollectionSourceBase.ObjectTypeInfo).Type property value.
  return:
    type: System.Collections.Generic.IEnumerable{{T}}
    description: The strongly-typed sequence that contains objects from the original collection.
seealso: []
---
