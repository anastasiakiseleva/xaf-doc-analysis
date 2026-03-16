---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.LockCount
name: LockCount
type: Property
summary: Gets the number of Appearance Controller updates that are currently in progress.
syntax:
  content: |-
    [DefaultValue(0)]
    public int LockCount { get; }
  parameters: []
  return:
    type: System.Int32
    description: An integer number of Appearance Controller updates that are currently in progress.
seealso: []
---
The [AppearanceController.AppearanceBeginUpdate](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceBeginUpdate) method increments this property value. The [AppearanceController.AppearanceEndUpdate](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceEndUpdate) method decrements it.