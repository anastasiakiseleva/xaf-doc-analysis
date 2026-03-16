---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.InstantFeedbackMappingMode
name: InstantFeedbackMappingMode
type: Property
summary: Specifies what properties should be mapped on a grid in the [InstantFeedback or InstantFeedbackView](xref:118450) mode.
syntax:
  content: public XPInstantFeedbackSourceMappingMode InstantFeedbackMappingMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Xpo.XPInstantFeedbackSourceMappingMode
    description: The [](xref:DevExpress.ExpressApp.Xpo.XPInstantFeedbackSourceMappingMode) enumeration value that specifies a properties mapping mode in the **InstantFeedback** or **InstantFeedbackView** mode.
seealso: []
---
By default, in the **InstantFeedback** and **InstantFeedbackView** modes, all properties values are calculated at once regardless of grid columns settings. If you need to calculate only visible columns values, set the **InstantFeedbackMappingMode** property to [XPInstantFeedbackSourceMappingMode.RequiredProperties](xref:DevExpress.ExpressApp.Xpo.XPInstantFeedbackSourceMappingMode.RequiredProperties) as demonstrated below:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Xpo;
//...
public class MyController : WindowController {
    public MyController() {
        this.TargetWindowType = WindowType.Main;
    }
    protected override void OnActivated() {
        base.OnActivated();
        Application.ListViewCreating += Application_ListViewCreating;
    }
    private void Application_ListViewCreating(object sender, ListViewCreatingEventArgs e) {
        if((e.CollectionSource.DataAccessMode == CollectionSourceDataAccessMode.InstantFeedback) && 
          (e.ObjectSpace is DevExpress.ExpressApp.Xpo.XPObjectSpace) && (e.ViewID == "Customer_ListView")) {
            ((XPObjectSpace)e.ObjectSpace).InstantFeedbackMappingMode =
XPInstantFeedbackSourceMappingMode.RequiredProperties;
        }
    }
    protected override void OnDeactivated() {
        Application.ListViewCreating -= Application_ListViewCreating;
        base.OnDeactivated();
    }
}
```
***

To map other columns which are not visible in the grid, add them to a collection of displayed options as described in the [CollectionSourceBase.DisplayableProperties](xref:DevExpress.ExpressApp.CollectionSourceBase.DisplayableProperties) topic.

If you want to specify what properties should be mapped on a grid for all Object Spaces, use the [XPObjectSpaceProvider.InstantFeedbackMappingMode](xref:DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.InstantFeedbackMappingMode) property of an Object Space Provider.