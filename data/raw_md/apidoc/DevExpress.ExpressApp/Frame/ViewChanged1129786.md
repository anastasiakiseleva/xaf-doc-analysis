---
uid: DevExpress.ExpressApp.Frame.ViewChanged
name: ViewChanged
type: Event
summary: Occurs after setting a [View](xref:112611) for a [Frame](xref:112608).
syntax:
  content: public event EventHandler<ViewChangedEventArgs> ViewChanged
seealso:
- linkId: DevExpress.ExpressApp.Frame.SetView*
---
Handle this event to customize the current Frame's [Frame.View](xref:DevExpress.ExpressApp.Frame.View).

You can also handle the [Frame.ViewChanging](xref:DevExpress.ExpressApp.Frame.ViewChanging) event to perform specific actions before setting a new View for the current Frame.