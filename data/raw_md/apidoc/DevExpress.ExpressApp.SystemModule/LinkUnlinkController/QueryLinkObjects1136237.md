---
uid: DevExpress.ExpressApp.SystemModule.LinkUnlinkController.QueryLinkObjects
name: QueryLinkObjects
type: Event
summary: Occurs when executing the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction).
syntax:
  content: public event EventHandler<QueryLinkObjectsEventArgs> QueryLinkObjects
seealso:
- linkId: DevExpress.ExpressApp.ListView.SelectedObjects
- linkId: DevExpress.ExpressApp.Frame.View
---
By default, the **Link** Action links the objects that are selected in the invoked popup Window. Handle this event to create a custom list of objects to be linked. Set the created list to the event handler's **QueryLinkObjectsEventArgs.LinkObjects** parameter. To access the Link View, use the event handler's **QueryLinkObjectsEventArgs.LinkWindow** parameter. To prevent linking the default list of objects, set the handler's **QueryLinkObjectsEventArgs.Handled** parameter to **true**.