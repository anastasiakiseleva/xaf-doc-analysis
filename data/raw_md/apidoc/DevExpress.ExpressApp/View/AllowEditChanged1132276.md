---
uid: DevExpress.ExpressApp.View.AllowEditChanged
name: AllowEditChanged
type: Event
summary: Occurs when the current [View](xref:112611)'s [View.AllowEdit](xref:DevExpress.ExpressApp.View.AllowEdit) state has changed.
syntax:
  content: public event EventHandler AllowEditChanged
seealso: []
---
Handle this event to execute custom code in response to a change in the current View's **AllowEdit** property.

A View's **AllowEdit** state is changed in two cases:

* When the **AllowEdit** collection does not have any elements with the value part set to **false** remaining.
* When the **AllowEdit** collection, which has only items with values set to **true**, gets an element with the value part set to **false**.

To change a View's **AllowEdit** state, use methods of the [](xref:DevExpress.ExpressApp.Utils.BoolList) object returned by the **AllowEdit** property.