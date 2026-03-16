---
uid: DevExpress.ExpressApp.View.AllowNewChanged
name: AllowNewChanged
type: Event
summary: Occurs when the current [View](xref:112611)'s [View.AllowNew](xref:DevExpress.ExpressApp.View.AllowNew) state has changed.
syntax:
  content: public event EventHandler AllowNewChanged
seealso: []
---
Handle this event to execute custom code in response to a change in the current View's **AllowNew** property.

A View's **AllowNew** state is changed in two cases:

* When the **AllowNew** collection does not have any elements with the value part set to **false** remaining.
* When the **AllowNew** collection, which has only items with values set to **true**, gets an element with the value part set to **false**.

To change a View's **AllowNew** state, use methods of the [](xref:DevExpress.ExpressApp.Utils.BoolList) object returned by the **AllowNew** property.