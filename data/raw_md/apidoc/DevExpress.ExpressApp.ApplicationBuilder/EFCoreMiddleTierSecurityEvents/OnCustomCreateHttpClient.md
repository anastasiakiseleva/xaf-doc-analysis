---
uid: DevExpress.ExpressApp.ApplicationBuilder.EFCoreMiddleTierSecurityEvents.OnCustomCreateHttpClient
name: OnCustomCreateHttpClient
type: Property
summary: Specifies the delegate that creates a custom @System.Net.Http.HttpClient that your WinForms application uses to interact with the Middle Tier Security server.
syntax:
  content: public Func<HttpClient> OnCustomCreateHttpClient { get; set; }
  parameters: []
  return:
    type: System.Func{System.Net.Http.HttpClient}
    description: The delegate that creates a custom @System.Net.Http.HttpClient that your WinForms application uses to interact with the Middle Tier Security server.
seealso: []
---
The following code snippet specifies this property:

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
                options.Events.OnCustomCreateHttpClient = () => {
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