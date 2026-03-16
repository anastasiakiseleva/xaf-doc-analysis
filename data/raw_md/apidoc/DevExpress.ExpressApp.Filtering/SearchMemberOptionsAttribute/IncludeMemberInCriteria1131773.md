---
uid: DevExpress.ExpressApp.Filtering.SearchMemberOptionsAttribute.IncludeMemberInCriteria
name: IncludeMemberInCriteria
type: Property
summary: Indicates whether to include or exclude the target property from the search performed by the **FullTextSearch** Action (see [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction)).
syntax:
  content: public SearchMemberMode IncludeMemberInCriteria { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Filtering.SearchMemberMode
    description: The [](xref:DevExpress.ExpressApp.Filtering.SearchMemberMode) enumeration value specifying whether to include or exclude the target property from the search performed by the **FullTextSearch** Action.
seealso: []
---
This property is specified by the _useMemberInCriteria_ parameter passed as the **SearchMemberOptions** attribute, applied to a business class property. The following values are possible:

* **Include**
    
    The target property is allowed to be used in the search performed by the **FullTextSearch** Action.
* **Exclude**
    
    The target property is prohibited from use in the search performed by the **FullTextSearch** Action.