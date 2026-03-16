---
uid: DevExpress.ExpressApp.Blazor.Editors.BlazorActionContainerViewItem.EndUpdate
name: EndUpdate()
type: Method
summary: Unlocks the View Item's [Action Container](xref:112610) control after a call to the [ActionContainerViewItem.BeginUpdate](xref:DevExpress.ExpressApp.Editors.ActionContainerViewItem.BeginUpdate) method and causes an immediate update.
syntax:
  content: public override void EndUpdate()
seealso: []
---
The **BeginUpdate** and **EndUpdate** methods are designed to implement batch modifications with Action Container View Items. This allows you to prevent excessive updates when changing multiple settings at once. For this purpose, enclose the code that changes multiple properties within calls to these methods.