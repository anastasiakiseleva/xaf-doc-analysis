---
uid: DevExpress.ExpressApp.ListView
name: ListView
type: Class
summary: A [List View](xref:112611).
syntax:
  content: 'public class ListView : ObjectView'
seealso:
- linkId: DevExpress.ExpressApp.ListView._members
  altText: ListView Members
- linkId: "112611"
---
The **ListView** class allows you to view or edit an objects collection.


> [!ImageGallery]
> ![A List View in a WinForms application](~/images/views_listview_win132343.png)
> ![A List View in a Blazor application](~/images/views_listview_blazor.png)

List Views take part in the automatic UI construction, so you do not spend time on [](xref:DevExpress.ExpressApp.ListView) objects creation. 

To influence this process, edit the [Application Model](xref:112580)'s [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] (**LookupListView**) node. In this node, you can specify the following:
* Type of objects to be displayed
* Columns to be displayed
* Order and visibility of the columns

To customize a **List View** in code, use either of the following properties:
* [Frame.View](xref:DevExpress.ExpressApp.Frame.View) 
* [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) property.

To perform custom actions when a user selects an object in a List View's editor, handle the [ListViewProcessCurrentObjectController.CustomProcessSelectedItem](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.CustomProcessSelectedItem) event.

The [](xref:DevExpress.ExpressApp.ObjectView) class that is the base class for the [](xref:DevExpress.ExpressApp.ListView) class, has one more descendant - the [](xref:DevExpress.ExpressApp.DetailView) class. This class is used to display an individual object.

[!example[XAF - How to show filter dialog before a List View](https://github.com/DevExpress-Examples/XAF_how-to-show-filter-dialog-before-listview)]
