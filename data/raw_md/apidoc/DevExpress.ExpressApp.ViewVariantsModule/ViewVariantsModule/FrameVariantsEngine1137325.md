---
uid: DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsModule.FrameVariantsEngine
name: FrameVariantsEngine
type: Property
summary: Specifies the [](xref:DevExpress.ExpressApp.ViewVariantsModule.IFrameVariantsEngine) object that provides methods to manage view variants.
syntax:
  content: |-
    [Browsable(false)]
    public IFrameVariantsEngine FrameVariantsEngine { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ViewVariantsModule.IFrameVariantsEngine
    description: An [](xref:DevExpress.ExpressApp.ViewVariantsModule.IFrameVariantsEngine) object that provides methods to manage view variants.
seealso: []
---
By default, the [](xref:DevExpress.ExpressApp.ViewVariantsModule.FrameVariantsEngine) object is assigned to the **FrameVariantsEngine** property when the [XafApplication.SetupComplete](xref:DevExpress.ExpressApp.XafApplication.SetupComplete) event occurs if this property is not yet initialized. The [](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController) class uses an object assigned to this property to switch view variants and to obtain a list of available view variants. Add a class that implements the **IFrameVariantsEngine** interface and assign an instance of this class to the **FrameVariantsEngine** property to replace the default behavior.