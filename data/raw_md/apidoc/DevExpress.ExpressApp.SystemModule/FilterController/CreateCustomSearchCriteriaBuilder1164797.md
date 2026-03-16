---
uid: DevExpress.ExpressApp.SystemModule.FilterController.CreateCustomSearchCriteriaBuilder
name: CreateCustomSearchCriteriaBuilder
type: Event
summary: Occurs when the Search Criteria Builder object used to build a criteria expression based on the value passed to the [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction) is created.
syntax:
  content: public event EventHandler<CreateCustomSearchCriteriaBuilderEventArgs> CreateCustomSearchCriteriaBuilder
seealso: []
---
You can handle this event and pass a custom **DevExpress.ExpressApp.Filtering.SearchCriteriaBuilder** instance to the **e.SearchCriteriaBuilder** parameter. The default **CreateSearchCriteriaBuilder** method will not be called in this case.