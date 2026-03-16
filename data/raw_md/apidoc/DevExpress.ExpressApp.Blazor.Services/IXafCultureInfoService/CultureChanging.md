---
uid: DevExpress.ExpressApp.Blazor.Services.IXafCultureInfoService.CultureChanging
name: CultureChanging
type: Event
summary: Fires before a change of culture in the application.
syntax:
  content: event EventHandler<CultureChangingEventArgs> CultureChanging
seealso: []
---
XAF raises the `CultureChanging` event before the application's culture changes, for example, when a user selects a different language. Use the event to intercept and perform custom actions before the culture switches and the page reloads if you need to validate, cancel, or log the culture change. To cancel the culture change, set the `Cancel` property of the `CultureChangingEventArgs` to `true` to prevent switching the culture and reloading the page.

You can use this event to control when and how the culture is changed and enforce business rules or perform localization-specific logic before the change takes effect. However, it is important to use caution when you cancel the culture change, as it may affect the overall user experience or consistency of the application's behavior.

For an example of use, see the following code snippet:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Services;

namespace MySolutionName.Blazor.Server.Controllers;

public class MyController : WindowController {
    protected override void OnActivated() {
        base.OnActivated();
        var cultService = Application.ServiceProvider.GetService<IXafCultureInfoService>();
        cultService.CultureChanging += CultService_CultureChanging;
    }

    private void CultService_CultureChanging(object sender, CultureChangingEventArgs e) {
        e.Cancel = true;
    }
}
```