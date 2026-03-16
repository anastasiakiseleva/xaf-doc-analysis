---
uid: DevExpress.ExpressApp.SystemModule.FilterController.FullTextSearchTargetPropertiesMode
name: FullTextSearchTargetPropertiesMode
type: Property
summary: Specifies the way in which the **FullTextSearch** [Action](xref:112622) collects properties to be included in search criteria.
syntax:
  content: public FullTextSearchTargetPropertiesMode FullTextSearchTargetPropertiesMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SystemModule.FullTextSearchTargetPropertiesMode
    description: |-
      A [](xref:DevExpress.ExpressApp.SystemModule.FullTextSearchTargetPropertiesMode) enumeration value that specifies the way in which the **FullTextSearch** Action collects properties for the criterion to be generated.
      The default value depends on the kind of List View for which the [](xref:DevExpress.ExpressApp.SystemModule.FilterController) was activated. 
      For the List Views used by the Lookup Property Editors, the default value is `VisibleColumns`. For all the other List Views, the default value is `AllSearchableMembers`.
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFullTextSearchProperties
- linkId: DevExpress.ExpressApp.SystemModule.FilterController.GetFullTextSearchProperties
---

When the `FullTextSearchTargetPropertiesMode` property is set to `VisibleColumns`, the **FullTextSearch** Action performs only scans properties if their corresponding columns are visibile.

> [!NOTE]
> [!include[FullTextSearchFriendlyKeyNote](~/templates/fulltextsearchfriendlykeynote11178.md)]

When the `FullTextSearchTargetPropertiesMode` property is set to `AllSearchableMembers`, the **FullTextSearch** Action scans the following properties:

* Any property of the current object
* Any property of the aggregated object
* The default property of the referenced object
* The properties that are presented by visible columns in the current List View

> [!NOTE]
> If the current List View uses [Server, ServerView, InstantFeedback, or InstantFeedbackView](xref:118450) mode (see [IModelListView.DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelListView.DataAccessMode)), XAF excludes non-persistent properties from the search.

Some properties that are added to the search because they satisfy the currently set `FullTextSearchTargetPropertiesMode` can be excluded if they use the [](xref:DevExpress.ExpressApp.Filtering.SearchMemberOptionsAttribute) with the `SearchMemberMode.Exclude` parameter value, or the [](xref:DevExpress.ExpressApp.Filtering.SearchClassOptionsAttribute) with the `SearchMemberMode.Exclude` parameter value, applied to the entire class.

If you need to manually specify a set of properties to be included in search criteria, handle the [FilterController.CustomGetFullTextSearchProperties](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFullTextSearchProperties) event.

> [!TIP]
> For information on how to filter search in Lookup Property Editors that do not use List Views, refer to the following topic: [Search in LookupProperty Editor](xref:113572#search-in-lookupproperty-editor).