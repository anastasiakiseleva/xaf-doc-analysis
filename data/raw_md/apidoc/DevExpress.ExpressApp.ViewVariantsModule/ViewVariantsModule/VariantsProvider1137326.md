---
uid: DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsModule.VariantsProvider
name: VariantsProvider
type: Property
summary: Specifies the [](xref:DevExpress.ExpressApp.ViewVariantsModule.IVariantsProvider) object that provides a list of view variants available for the specific View, and stores the variant selected by user.
syntax:
  content: |-
    [Browsable(false)]
    public IVariantsProvider VariantsProvider { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ViewVariantsModule.IVariantsProvider
    description: An [](xref:DevExpress.ExpressApp.ViewVariantsModule.IVariantsProvider) object that provides a list of view variants available for the specific View, and stores the variant selected by the user.
seealso:
- linkId: DevExpress.ExpressApp.ViewVariantsModule.IVariantsProvider
---
The **VariantsProvider** property is used by the [](xref:DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsModule) class to initialize the `DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsModule.FrameVariantsEngine` property and by the **CustomizeNavigationItemsController** class to build additional navigation nodes for view variants. By default, a [](xref:DevExpress.ExpressApp.ViewVariantsModule.ModelVariantsProvider) object is assigned to the **VariantsProvider** property when the [XafApplication.SetupComplete](xref:DevExpress.ExpressApp.XafApplication.SetupComplete) event occurs if this property is not yet initialized. Add a class that implements the [](xref:DevExpress.ExpressApp.ViewVariantsModule.IVariantsProvider) interface and assign an instance of this class to the **VariantsProvider** property if you want to replace the standard behavior. 

# [C#](#tab/tabid-csharp)

```csharp
public sealed partial class MySolutionModule : ModuleBase {
    public override void Setup(XafApplication application) {
        base.Setup(application);
        application.SetupComplete += application_SetupComplete;
    }
    void application_SetupComplete(object sender, EventArgs e) {
        Application.Modules.FindModule<ViewVariantsModule>().VariantsProvider = new DatabaseViewVariantsProvider(Application);
    }
    // ...
}
```
***

The **DatabaseViewVariantsProvider** class is used in the snippet above. This class implementation is demonstrated in the [](xref:DevExpress.ExpressApp.ViewVariantsModule.IVariantsProvider) topic.