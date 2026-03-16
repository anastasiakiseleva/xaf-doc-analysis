---
uid: DevExpress.ExpressApp.ViewItemsChangedEventArgs
name: ViewItemsChangedEventArgs
type: Class
summary: Represents arguments passed to the [CompositeView.ItemsChanged](xref:DevExpress.ExpressApp.CompositeView.ItemsChanged) event.
syntax:
  content: 'public class ViewItemsChangedEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.ViewItemsChangedEventArgs._members
  altText: ViewItemsChangedEventArgs Members
---
The [CompositeView.ItemsChanged](xref:DevExpress.ExpressApp.CompositeView.ItemsChanged) event occurs after changing a Composite View's [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection. Handle this event to perform specific actions when changing the collection.

The **ViewItemsChangedEventArgs** class exposes two properties. The [ViewItemsChangedEventArgs.Item](xref:DevExpress.ExpressApp.ViewItemsChangedEventArgs.Item) property specifies the View Item that was added or removed. The [ViewItemsChangedEventArgs.ChangedType](xref:DevExpress.ExpressApp.ViewItemsChangedEventArgs.ChangedType) property specifies whether the View Item was added or removed.