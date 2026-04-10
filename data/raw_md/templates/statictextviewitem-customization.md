The following code snippet enables HTML markup in a Static Text component:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

namespace MySolution.Module.Controllers;

public class CustomizeDashboardViewController : ViewController<DashboardView> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<StaticTextViewItem>(this, item => {
            item.ComponentModel.UseMarkupString = true;
        });
    }
}
```