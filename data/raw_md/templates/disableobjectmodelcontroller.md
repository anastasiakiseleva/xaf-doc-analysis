You can disable the [ObjectModelController](xref:113141#objectmodelcontroller) before the View Controls are created:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.SystemModule;

namespace YourApplicationName.Blazor.Server.Controllers;
public class DisableObjectModelController : ViewController {

    private ObjectModelController objectModelController;
    const string deactivateReason = "NoCustomizationRequired";
    protected override void OnActivated() {
        base.OnActivated();
        objectModelController = Frame.GetController<ObjectModelController>();
        if (objectModelController != null) {
            objectModelController.Active.SetItemValue(deactivateReason, false);
        }
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        if (objectModelController != null) {
            objectModelController.Active.RemoveItem(deactivateReason);
            objectModelController = null;
        }
    }
}
```