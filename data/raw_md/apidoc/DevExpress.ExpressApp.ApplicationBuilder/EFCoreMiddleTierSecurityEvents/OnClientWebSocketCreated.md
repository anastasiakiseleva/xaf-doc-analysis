---
uid: DevExpress.ExpressApp.ApplicationBuilder.EFCoreMiddleTierSecurityEvents.OnClientWebSocketCreated
name: OnClientWebSocketCreated
type: Property
summary: Specifies the delegate that configures a @System.Net.WebSockets.ClientWebSocket that your WinForms application uses to interact with the Middle Tier Security server.
syntax:
  content: public Action<ClientWebSocket> OnClientWebSocketCreated { get; set; }
  parameters: []
  return:
    type: System.Action{System.Net.WebSockets.ClientWebSocket}
    description: The delegate that configures a @System.Net.WebSockets.ClientWebSocket that your WinForms application uses to interact with the Middle Tier Security server.
seealso: []
---
The following code snippet accesses this property:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{11-13}
using DevExpress.ExpressApp.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        // ...
        builder.Security
            .UseMiddleTierMode(options => {
                options.Events.OnClientWebSocketCreated = (client) => {
                  //...
                }
            })
            .UsePasswordAuthentication();
        // ...
    }
    // ...
}
```
***