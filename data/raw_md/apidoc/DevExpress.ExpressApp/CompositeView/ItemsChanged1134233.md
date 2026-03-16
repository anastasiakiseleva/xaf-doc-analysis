---
uid: DevExpress.ExpressApp.CompositeView.ItemsChanged
name: ItemsChanged
type: Event
summary: Occurs after changing a Composite View's [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection.
syntax:
  content: public event EventHandler<ViewItemsChangedEventArgs> ItemsChanged
seealso:
- linkId: DevExpress.ExpressApp.CompositeView.AddItem*
- linkId: DevExpress.ExpressApp.CompositeView.InsertItem*
- linkId: DevExpress.ExpressApp.CompositeView.RemoveItem(System.String)
---
The [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection is changed when you add or insert a new [View Item](xref:112612) or remove one of the existing items.

Handle the `ItemsChanged` event to perform specific actions when you change the collection. Use the handler's [ViewItemsChangedEventArgs.Item](xref:DevExpress.ExpressApp.ViewItemsChangedEventArgs.Item) and [ViewItemsChangedEventArgs.ChangedType](xref:DevExpress.ExpressApp.ViewItemsChangedEventArgs.ChangedType) parameters to specify the View Item and the operation performed.