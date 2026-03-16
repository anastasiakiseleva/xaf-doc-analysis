---
uid: DevExpress.ExpressApp.ISupportUpdate.EndUpdate
name: EndUpdate()
type: Method
summary: Unlocks an entity implementing the [](xref:DevExpress.ExpressApp.ISupportUpdate) interface after a call to the [ISupportUpdate.BeginUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.BeginUpdate) method, and causes an immediate update.
syntax:
  content: void EndUpdate()
seealso: []
---
The [ISupportUpdate.BeginUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.BeginUpdate) and [ISupportUpdate.EndUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.EndUpdate) methods are designed to implement batch modifications with UI entities. After the [ISupportUpdate.BeginUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.BeginUpdate) method has been called, and until a call to the [ISupportUpdate.EndUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.EndUpdate) method, generally, an entity's events will not be raised, and a UI will not be refreshed. This allows you to prevent excessive UI updates when changing multiple settings at once. For this purpose, enclose the code that changes the properties within calls to the [ISupportUpdate.BeginUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.BeginUpdate) and [ISupportUpdate.EndUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.EndUpdate) methods.