---
uid: DevExpress.ExpressApp.Editors.DashboardViewItem
name: DashboardViewItem
type: Class
summary: Represents a [View Item](xref:112612) that displays a [View](xref:112611) in a nested [Frame](xref:112608).
syntax:
  content: 'public class DashboardViewItem : ViewItem, IComplexViewItem, IFrameContainer'
seealso:
- linkId: DevExpress.ExpressApp.Editors.DashboardViewItem._members
  altText: DashboardViewItem Members
- linkId: DevExpress.ExpressApp.Editors.ViewItemAttribute
---
Beside List Views and Detail Views, **XAF** supports a special View type - the [](xref:DevExpress.ExpressApp.DashboardView). A Dashboard View is used to display several Views side-by-side in a single [Frame](xref:112608) (on a single screen). Each View displayed on a dashboard is represented by a **DashboardViewItem**. To display its [View](xref:112611), a **DashboardViewItem** creates a nested Frame, which you can access via the [DashboardViewItem.Frame](xref:DevExpress.ExpressApp.Editors.DashboardViewItem.Frame) property. To access the displayed View, use the [DashboardViewItem.InnerView](xref:DevExpress.ExpressApp.Editors.DashboardViewItem.InnerView) property.

To learn how to add the **DashboardViewItem** to a Dashboard View, and configure it, refer to the [How to: Display Several Views Side-by-Side](xref:113296) help topic.