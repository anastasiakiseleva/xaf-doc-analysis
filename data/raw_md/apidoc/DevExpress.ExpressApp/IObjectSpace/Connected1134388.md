---
uid: DevExpress.ExpressApp.IObjectSpace.Connected
name: Connected
type: Event
summary: Occurs after a connection to a database has been established.
syntax:
  content: event EventHandler Connected
seealso: []
---
If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, to raise the **Connected** event, you should invoke the **BaseObjectSpace.OnConnected** method when a connection to the database is opened.