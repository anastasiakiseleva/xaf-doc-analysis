---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierSecurityEvents.OnCustomCreateHttpClient
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
The following example demonstrates how to specify this property:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{11-13}
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