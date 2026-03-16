---
uid: DevExpress.ExpressApp.ISupportUpdate
name: ISupportUpdate
type: Interface
summary: Implemented by classes representing UI entities that support batch updates.
syntax:
  content: public interface ISupportUpdate
seealso:
- linkId: DevExpress.ExpressApp.ISupportUpdate._members
  altText: ISupportUpdate Members
---
The [ISupportUpdate.BeginUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.BeginUpdate) and [ISupportUpdate.EndUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.EndUpdate) methods are designed to implement batch modifications with UI entities. After the [ISupportUpdate.BeginUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.BeginUpdate) method has been called, and until a call to the [ISupportUpdate.EndUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.EndUpdate) method, generally, an entity's events will not be raised, and a UI will not be refreshed. This allows you to prevent excessive UI updates when changing multiple settings at once. For this purpose, enclose the code that changes the properties within calls to the [ISupportUpdate.BeginUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.BeginUpdate) and [ISupportUpdate.EndUpdate](xref:DevExpress.ExpressApp.ISupportUpdate.EndUpdate) methods.