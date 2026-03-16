---
uid: DevExpress.ExpressApp.CollectionSourceBase.GetEnumerable(System.Boolean)
name: GetEnumerable(Boolean)
type: Method
summary: Returns a sequence ([](xref:System.Collections.IEnumerable) or [](xref:System.Linq.IQueryable)) that contains objects from the original collection.
syntax:
  content: public IEnumerable GetEnumerable(bool wrapNotifications = true)
  parameters:
  - id: wrapNotifications
    type: System.Boolean
    defaultValue: "True"
    description: '**true** if the returned sequence should implement the @System.Collections.Specialized.INotifyCollectionChanged interface; otherwise, **false**. The method considers this parameter only if the original collection implements the @System.ComponentModel.IBindingList interface.'
  return:
    type: System.Collections.IEnumerable
    description: The sequence that contains objects from the original collection.
seealso: []
---
