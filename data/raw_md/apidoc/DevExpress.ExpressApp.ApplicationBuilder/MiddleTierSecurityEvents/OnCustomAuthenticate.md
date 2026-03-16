---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierSecurityEvents.OnCustomAuthenticate
name: OnCustomAuthenticate
type: Property
summary: Specifies the delegate that configures custom authentication.
syntax:
  content: public Action<object, ISecurityStrategyBase, WebApiSecuredDataServerClientCustomAuthenticateEventArgs> OnCustomAuthenticate { get; set; }
  parameters: []
  return:
    type: System.Action{System.Object,DevExpress.ExpressApp.Security.ISecurityStrategyBase,DevExpress.ExpressApp.Security.ClientServer.WebApiSecuredDataServerClientCustomAuthenticateEventArgs}
    description: The delegate that configures custom authentication.
seealso: []
---
The following example demonstrates how to specify this property:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{11-14}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        // ...
        builder.Security
            .UseMiddleTierMode(options => {
                options.Events.OnCustomAuthenticate = (sender, security, args) => {
                    args.Handled = true;
                    // ...
                };
            })
            .UsePasswordAuthentication();
        // ...
    }
    // ...
}
```
***