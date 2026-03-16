---
uid: DevExpress.ExpressApp.CollectionSourceBase.CriteriaApplied
name: CriteriaApplied
type: Event
summary: Occurs after the Collection Source's collection has been filtered using the [](xref:DevExpress.Data.Filtering.CriteriaOperator) objects contained in the [CollectionSourceBase.Criteria](xref:DevExpress.ExpressApp.CollectionSourceBase.Criteria) dictionary.
syntax:
  content: public event EventHandler CriteriaApplied
seealso: []
---
This event is raised in the private **ApplyCriteria** method after the Collection Source's collection has been filtered. Generally, you do not need to handle this event.