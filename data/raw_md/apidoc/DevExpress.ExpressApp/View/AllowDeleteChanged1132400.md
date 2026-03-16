---
uid: DevExpress.ExpressApp.View.AllowDeleteChanged
name: AllowDeleteChanged
type: Event
summary: Occurs when the current [View](xref:112611)'s [View.AllowDelete](xref:DevExpress.ExpressApp.View.AllowDelete) state has changed.
syntax:
  content: public event EventHandler AllowDeleteChanged
seealso: []
---
Handle this event to execute custom code in response to a change in the current View's **AllowDelete** property.

A View's **AllowDelete** state is changed in two cases:

* When the **AllowDelete** collection does not have any elements with the value part set to **false** remaining.
* When the **AllowDelete** collection, which has only items with values set to **true**, gets an element with the value part set to **false**.

To change a View's **AllowDelete** state, use methods of the [](xref:DevExpress.ExpressApp.Utils.BoolList) object returned by the **AllowDelete** property.