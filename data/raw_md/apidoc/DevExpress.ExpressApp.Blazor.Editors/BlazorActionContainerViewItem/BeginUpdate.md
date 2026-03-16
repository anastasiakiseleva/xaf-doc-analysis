---
uid: DevExpress.ExpressApp.Blazor.Editors.BlazorActionContainerViewItem.BeginUpdate
name: BeginUpdate()
type: Method
summary: Prevents the View Item's [Action Container](xref:112610) control from being updated until the [ActionContainerViewItem.EndUpdate](xref:DevExpress.ExpressApp.Editors.ActionContainerViewItem.EndUpdate) method is called.
syntax:
  content: public override void BeginUpdate()
seealso: []
---
The **BeginUpdate** and **EndUpdate** methods are designed to implement batch modifications with Action Container View Items. This allows you to prevent excessive updates when changing multiple settings at once. For this purpose, enclose the code that changes multiple properties within calls to these methods.