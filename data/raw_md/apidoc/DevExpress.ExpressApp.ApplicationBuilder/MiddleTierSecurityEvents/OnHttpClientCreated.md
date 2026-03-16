---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierSecurityEvents.OnHttpClientCreated
name: OnHttpClientCreated
type: Property
summary: Specifies the delegate that configures the @System.Net.Http.HttpClient that your WinForms application uses to interact with the Middle Tier Security server.
syntax:
  content: public Action<HttpClient> OnHttpClientCreated { get; set; }
  parameters: []
  return:
    type: System.Action{System.Net.Http.HttpClient}
    description: The delegate that configures the @System.Net.Http.HttpClient that your WinForms application uses to interact with the Middle Tier Security server.
seealso: []
---
The following example demonstrates how to use this property:

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
                options.Events.OnHttpClientCreated = (client) => {
                    client.DefaultRequestHeaders.Add("Accept", "application/json");
                };
            })
            .UsePasswordAuthentication();
        // ...
    }
    // ...
}
```
***