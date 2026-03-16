---
uid: DevExpress.ExpressApp.ApplicationBuilder.EFCoreMiddleTierSecurityOptions.Events
name: Events
type: Property
summary: Provides access to [EF Core Middle Tier Security](xref:404389) events.
syntax:
  content: public EFCoreMiddleTierSecurityEvents Events { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.EFCoreMiddleTierSecurityEvents
    description: '[EF Core Middle Tier Security](xref:404389) events.'
seealso: []
---
The following code snippet uses this property:

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