---
uid: DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController.AllowChangeVariantWhenObjectSpaceIsModified
name: AllowChangeVariantWhenObjectSpaceIsModified
type: Property
summary: Indicates whether the [ChangeVariantController.ChangeVariantAction](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController.ChangeVariantAction) is enabled when the Object Space is modified.
syntax:
  content: public bool? AllowChangeVariantWhenObjectSpaceIsModified { get; set; }
  parameters: []
  return:
    type: System.Nullable{System.Boolean}
    description: '`true`, if the **ChangeVariantAction** is enabled when the Object Space is modified; otherwise - `false`.'
seealso: []
---
The `AllowChangeVariantWhenObjectSpaceIsModified` property is initialized in the `OnFrameAssigned` method in case the value is not yet assigned. This Action's state is influenced by its [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property's `NotModified` key value. This property is set to `true` by default.

To change the default value, implement a custom [Controller](xref:112621) and access this property in the overridden `OnFrameAssigned` method.