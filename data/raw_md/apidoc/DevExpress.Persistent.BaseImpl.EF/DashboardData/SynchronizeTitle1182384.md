---
uid: DevExpress.Persistent.BaseImpl.EF.DashboardData.SynchronizeTitle
name: SynchronizeTitle
type: Property
summary: Specifies if it is required to update the [DashboardData.Title](xref:DevExpress.Persistent.BaseImpl.EF.DashboardData.Title) value with the dashboard title from the dashboard configuration (stored in the [DashboardData.Content](xref:DevExpress.Persistent.BaseImpl.EF.DashboardData.Content) property).
syntax:
  content: |-
    [VisibleInDetailView(false)]
    [VisibleInListView(false)]
    [VisibleInLookupListView(false)]
    public virtual bool SynchronizeTitle { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if it is required to update the dashboard title; otherwise, **false**.'
seealso: []
---
The title update occurs when the dashboard is saved in the designer.