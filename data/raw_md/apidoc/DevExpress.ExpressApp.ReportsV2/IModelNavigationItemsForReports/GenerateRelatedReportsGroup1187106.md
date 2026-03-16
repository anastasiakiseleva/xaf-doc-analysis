---
uid: DevExpress.ExpressApp.ReportsV2.IModelNavigationItemsForReports.GenerateRelatedReportsGroup
name: GenerateRelatedReportsGroup
type: Property
summary: Specifies whether context navigation is enabled for the [Reports V2 Module](xref:113591).
syntax:
  content: bool GenerateRelatedReportsGroup { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, to enable context navigation for the Reports V2 module; otherwise, **false**.'
seealso: []
---
When this property is set to true, the [Reports V2 Module](xref:113591) adds navigation items for the items corresponding to business classes participating in existing inplace reports. Each additional item corresponds to an inplace report. If you need a navigation item for a particular report, set the report's **IsInplaceReport** property to **true**.