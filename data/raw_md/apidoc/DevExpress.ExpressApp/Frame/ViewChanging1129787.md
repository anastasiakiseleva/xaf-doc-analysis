---
uid: DevExpress.ExpressApp.Frame.ViewChanging
name: ViewChanging
type: Event
summary: Occurs before setting a [View](xref:112611) for a [Frame](xref:112608).
syntax:
  content: public event EventHandler<ViewChangingEventArgs> ViewChanging
seealso:
- linkId: DevExpress.ExpressApp.Frame.SetView*
---
Handle this event to perform specific actions before setting a [](xref:DevExpress.ExpressApp.View) for the current [](xref:DevExpress.ExpressApp.Frame).

You can also handle the [Frame.ViewChanged](xref:DevExpress.ExpressApp.Frame.ViewChanged) event to perform specific actions after setting a new View for the current Frame.