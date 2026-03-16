---
uid: DevExpress.ExpressApp.SystemModule.CustomBuildCriteriaEventArgs.Criteria
name: Criteria
type: Property
summary: Specifies the **CriteriaOperator** to be used by the **FullTextSearch** [Action](xref:112622) to filter a [List View](xref:112611).
syntax:
  content: public CriteriaOperator Criteria { get; set; }
  parameters: []
  return:
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **CriteriaOperator** that will be used by the **FullTextSearch** [Action](xref:112622) to filter the current [List View](xref:112611).
seealso:
- linkId: DevExpress.Data.Filtering.CriteriaOperator
---
Set this property to a custom-built **CriteriaOperator**. For additional explanation, refer to the [FilterController.CustomBuildCriteria](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomBuildCriteria) event description.