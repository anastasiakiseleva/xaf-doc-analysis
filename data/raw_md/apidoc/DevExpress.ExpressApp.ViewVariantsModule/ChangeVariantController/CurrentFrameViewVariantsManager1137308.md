---
uid: DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController.CurrentFrameViewVariantsManager
name: CurrentFrameViewVariantsManager
type: Property
summary: Specifies the [](xref:DevExpress.ExpressApp.ViewVariantsModule.ICurrentFrameViewVariantsManager) object that provides available View Variants and changes the View of the current [](xref:DevExpress.ExpressApp.Frame).
syntax:
  content: |-
    [Browsable(false)]
    public ICurrentFrameViewVariantsManager CurrentFrameViewVariantsManager { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ViewVariantsModule.ICurrentFrameViewVariantsManager
    description: An [](xref:DevExpress.ExpressApp.ViewVariantsModule.ICurrentFrameViewVariantsManager) object that provides available View Variants and changes the View of the current [](xref:DevExpress.ExpressApp.Frame).
seealso: []
---
By default, this property is initialized with the [](xref:DevExpress.ExpressApp.ViewVariantsModule.CurrentFrameViewVariantsManager) object.

To change the default value, implement a custom [Controller](xref:112621) and access this property in the overridden **OnFrameAssigned** method. The previous value of the this property can be disposed of either when a new value is assigned or when the [](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController) Controller is deactivated, depending on the [ChangeVariantController.IsCurrentFrameViewVariantsManagerOwner](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController.IsCurrentFrameViewVariantsManagerOwner) value.