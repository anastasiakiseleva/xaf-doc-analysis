---
uid: DevExpress.Persistent.BaseImpl.DashboardData.SynchronizeTitle
name: SynchronizeTitle
type: Property
summary: Specifies if it is required to update the [IDashboardData.Title](xref:DevExpress.Persistent.Base.IDashboardData.Title) value with the dashboard title from the dashboard configuration (stored in the [IDashboardData.Content](xref:DevExpress.Persistent.Base.IDashboardData.Content) property).
syntax:
  content: |-
    [VisibleInDetailView(false)]
    [VisibleInListView(false)]
    [VisibleInLookupListView(false)]
    public bool SynchronizeTitle { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if it is required to update the dashboard title; otherwise, **false**.'
seealso: []
---
The title update occurs when the dashboard is saved in the designer.