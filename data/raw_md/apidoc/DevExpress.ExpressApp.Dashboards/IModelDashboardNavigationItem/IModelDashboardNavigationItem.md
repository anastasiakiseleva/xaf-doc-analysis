---
uid: DevExpress.ExpressApp.Dashboards.IModelDashboardNavigationItem
name: IModelDashboardNavigationItem
type: Interface
summary: A Navigation Item node that points to a [dashboard](xref:117449).
syntax:
  content: 'public interface IModelDashboardNavigationItem : IModelNavigationItem, IModelNode, IModelBaseChoiceActionItem, IModelToolTip, IModelChoiceActionItemChildItemsDisplayStyle'
seealso:
- linkId: DevExpress.ExpressApp.Dashboards.IModelDashboardNavigationItem._members
  altText: IModelDashboardNavigationItem Members
---
This interface extends the [](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem) node with the [IModelDashboardNavigationItem.DashboardTitle](xref:DevExpress.ExpressApp.Dashboards.IModelDashboardNavigationItem.DashboardTitle) property. You can create the **IModelDashboardNavigationItem** node in the [Model Editor](xref:112582).

![DashboardNavigationItem](~/images/dashboardnavigationitem125662.png)

Refer to the [Create a Predefined Dashboard and Add it to the Navigation](xref:117453) topic to see the complete example.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.