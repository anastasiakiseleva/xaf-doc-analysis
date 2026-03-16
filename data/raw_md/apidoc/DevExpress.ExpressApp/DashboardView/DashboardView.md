---
uid: DevExpress.ExpressApp.DashboardView
name: DashboardView
type: Class
summary: A Dashboard View.
syntax:
  content: 'public class DashboardView : CompositeView'
seealso:
- linkId: DevExpress.ExpressApp.DashboardView._members
  altText: DashboardView Members
- linkId: "112611"
- linkId: "112817"
---
Dashboard Views can display multiple Views side-by-side in a single [Frame](xref:112608) (on a single screen).

> [!ImageGallery]
> ![A Dashboard View in a WinForms application](~/images/views_dashboardview_win132346.png)
> ![A Dashboard View in a Blazor UI application](~/images/views-dashboard-blazor.png)


A Dashboard View maintains a collection of [](xref:DevExpress.ExpressApp.Editors.DashboardViewItem) objects. Each Item uses the [IModelDashboardViewItem.View](xref:DevExpress.ExpressApp.Model.IModelDashboardViewItem.View) property to refer to a View. This property is available in **DashboardViewItem** nodes of the [Application Model](xref:112580). 

When the application initializes a Dashboard View, it calls the [View.CreateControls](xref:DevExpress.ExpressApp.View.CreateControls) method. This method creates nested Frames for each [View Item](xref:112612) and displays associated Views. 

Dashboard Views support multiple View Items types. In addition to XAF Views, the dashboard can display text blocks, images, and Action Containers. Add [](xref:DevExpress.ExpressApp.Editors.StaticText), [](xref:DevExpress.ExpressApp.Editors.StaticImage), and [](xref:DevExpress.ExpressApp.Editors.ActionContainerViewItem) View Items to the Dashboard View if you need to display such elements. 

> [!Note]
> Blazor ListViews with a [split layout](xref:113249#split-layout-the-masterdetailmode-property) display [Dashboards](xref:117449) in read-only mode.

If you need to customize a Dashboard View in code, you can access it from a [Frame.View](xref:DevExpress.ExpressApp.Frame.View) or [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) property. Use the following `DashboardView`'s members to specify the [View Items](xref:112612) that you want to display:
* [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items)
* [CompositeView.AddItem](xref:DevExpress.ExpressApp.CompositeView.AddItem*)
* [CompositeView.RemoveItem](xref:DevExpress.ExpressApp.CompositeView.RemoveItem(System.String))
* [CompositeView.InsertItem](xref:DevExpress.ExpressApp.CompositeView.InsertItem*)

The [](xref:DevExpress.ExpressApp.CompositeView) class that is the base class for the [](xref:DevExpress.ExpressApp.DashboardView) class, has another descendant - the [](xref:DevExpress.ExpressApp.DetailView) class. Use it to display an individual object.

To learn how to create and configure a Dashboard View, refer to the [Display Multiple Views Side-by-Side (Dashboard View)](xref:113296) help topic.
