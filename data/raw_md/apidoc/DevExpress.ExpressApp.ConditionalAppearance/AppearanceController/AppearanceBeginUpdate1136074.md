---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceBeginUpdate
name: AppearanceBeginUpdate()
type: Method
summary: Prevents the AppearanceController from being updated until the [AppearanceController.AppearanceEndUpdate](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceEndUpdate) method is called.
syntax:
  content: public void AppearanceBeginUpdate()
seealso: []
---
This method is intended for internal use. It increments the [AppearanceController.LockCount](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.LockCount) value.