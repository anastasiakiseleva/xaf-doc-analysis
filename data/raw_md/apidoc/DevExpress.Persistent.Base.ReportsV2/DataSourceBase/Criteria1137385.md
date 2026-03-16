---
uid: DevExpress.Persistent.Base.ReportsV2.DataSourceBase.Criteria
name: Criteria
type: Property
summary: The criteria used to filter data in a report.
syntax:
  content: public CriteriaOperator Criteria { get; set; }
  parameters: []
  return:
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) object used to filter data.
seealso:
- linkId: "113594"
---
The **Criteria** value is passed to the [IObjectSpace.ApplyCriteria](xref:DevExpress.ExpressApp.IObjectSpace.ApplyCriteria(System.Object,DevExpress.Data.Filtering.CriteriaOperator)) method.