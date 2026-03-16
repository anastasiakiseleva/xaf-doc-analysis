---
uid: DevExpress.ExpressApp.View.QueryCanChangeCurrentObject
name: QueryCanChangeCurrentObject
type: Event
summary: Occurs when the View is asked whether its current object can be changed.
syntax:
  content: public event EventHandler<CancelEventArgs> QueryCanChangeCurrentObject
seealso: []
---
This event is raised by the [View.CanChangeCurrentObject](xref:DevExpress.ExpressApp.View.CanChangeCurrentObject) method. Handle this event to prohibit changing the current object by setting the event handler's **CancelEventArgs.Cancel** parameter to **true**.