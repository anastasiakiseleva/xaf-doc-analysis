---
uid: DevExpress.ExpressApp.Filtering.SearchClassOptionsAttribute.IncludeMembersInCriteria
name: IncludeMembersInCriteria
type: Property
summary: Indicates whether to include or exclude the target class' properties from the search performed by the **FullTextSearch** Action (see [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction)).
syntax:
  content: public SearchMemberMode IncludeMembersInCriteria { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Filtering.SearchMemberMode
    description: The [](xref:DevExpress.ExpressApp.Filtering.SearchMemberMode) enumeration value specifying whether to include or exclude the target class' properties from the search performed by the **FullTextSearch** Action.
seealso: []
---
This property is specified by the _includeMembersInCriteria_ parameter passed in the [](xref:DevExpress.ExpressApp.Filtering.SearchClassOptionsAttribute), applied to a business class. The following values are possible:

* **Include**
    
    The search is allowed within all the properties of the target class. So, all the properties that are specified by the [FilterController.FullTextSearchTargetPropertiesMode](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextSearchTargetPropertiesMode) will be used in the search performed by the **FullTextSearch** Action.
    
    Note that individual properties will be excluded from the search scope, if they use the [](xref:DevExpress.ExpressApp.Filtering.SearchMemberOptionsAttribute) with the [SearchMemberMode.Exclude](xref:DevExpress.ExpressApp.Filtering.SearchMemberMode.Exclude) parameter value.
* **Exclude**
    
    The search is not allowed within all the properties of the target class.
    
    Note that individual properties will be included in the search scope if they use the [](xref:DevExpress.ExpressApp.Filtering.SearchMemberOptionsAttribute) with the [SearchMemberMode.Include](xref:DevExpress.ExpressApp.Filtering.SearchMemberMode.Include) parameter value, and satisfy the Filter Controller's **FullTextSearchTargetPropertiesMode**.