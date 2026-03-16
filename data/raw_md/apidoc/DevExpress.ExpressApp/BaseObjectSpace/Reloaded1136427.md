---
uid: DevExpress.ExpressApp.BaseObjectSpace.Reloaded
name: Reloaded
type: Event
summary: Occurs when the [BaseObjectSpace.Rollback](xref:DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean)) or [BaseObjectSpace.Refresh](xref:DevExpress.ExpressApp.BaseObjectSpace.Refresh) method is called.
syntax:
  content: public event EventHandler Reloaded
seealso: []
---
In [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace), this event is raised when the [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) object is recreated. In [](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace), this event is raised when the [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext) is recreated.