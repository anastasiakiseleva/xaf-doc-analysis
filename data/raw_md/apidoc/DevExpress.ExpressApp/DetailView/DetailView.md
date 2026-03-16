---
uid: DevExpress.ExpressApp.DetailView
name: DetailView
type: Class
summary: A [Detail View](xref:112611).
syntax:
  content: 'public class DetailView : ObjectView'
seealso:
- linkId: DevExpress.ExpressApp.DetailView._members
  altText: DetailView Members
- linkId: "112607"
- linkId: "112611"
- linkId: "112817"
---
The [](xref:DevExpress.ExpressApp.DetailView) class is an [](xref:DevExpress.ExpressApp.ObjectView) descendant. Use the `DetailView` class to view or edit an object's properties.

ASP.NET Core Blazor
:   ![|A Detail View in an XAF ASP.NET Core Blazor application, DevExpress|](~/images/xaf-blazor-detailview-devexpress.png)
Windows Forms
:   ![A Detail View in an XAF Windows Forms application, DevExpress](~/images/views_detailview_win132339.png)

XAF automatically generates a user interface for Detail Views. You can customize an auto-generated Detail View in the [Application Model](xref:112580). Use the [!include[Node_DetailView](~/templates/node_detailview111382.md)] node. For example, you can specify the object that this Detail View displays and change the displayed [View Items](xref:112612) and their layout.

To customize a Detail View in code, use the [Frame.View](xref:DevExpress.ExpressApp.Frame.View) or [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) property.

To specify the object displayed in the Detail View, use the [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) property.

To populate a View with [View Items](xref:112612), use the following members:
* [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items)
* [CompositeView.AddItem](xref:DevExpress.ExpressApp.CompositeView.AddItem*)
* [CompositeView.RemoveItem](xref:DevExpress.ExpressApp.CompositeView.RemoveItem(System.String))
* [CompositeView.InsertItem](xref:DevExpress.ExpressApp.CompositeView.InsertItem*)

To customize View Items' layout, use the [CompositeView.LayoutManager](xref:DevExpress.ExpressApp.CompositeView.LayoutManager) property.

> [!TIP]
> To view and edit the properties of a collection of objects, use the [](xref:DevExpress.ExpressApp.ListView) class.