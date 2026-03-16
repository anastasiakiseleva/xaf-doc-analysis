---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierSecurityOptions.Events
name: Events
type: Property
summary: Provides access to [XPO Middle Tier Security](xref:113439) events.
syntax:
  content: public MiddleTierSecurityEvents Events { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierSecurityEvents
    description: '[XPO Middle Tier Security](xref:113439) events.'
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