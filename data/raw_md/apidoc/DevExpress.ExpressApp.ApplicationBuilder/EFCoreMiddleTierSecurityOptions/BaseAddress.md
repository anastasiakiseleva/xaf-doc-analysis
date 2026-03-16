---
uid: DevExpress.ExpressApp.ApplicationBuilder.EFCoreMiddleTierSecurityOptions.BaseAddress
name: BaseAddress
type: Property
summary: Specifies the Middle Tier Security server address.
syntax:
  content: public Uri BaseAddress { get; set; }
  parameters: []
  return:
    type: System.Uri
    description: The Middle Tier Security server address.
seealso: []
---
The following code snippet specifies this property:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{11}
using DevExpress.ExpressApp.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        // ...
        builder.Security
            .UseMiddleTierMode(options => {
                options.BaseAddress = new Uri("https://localhost:44319/");
            })
            .UsePasswordAuthentication();
        // ...
    }
    // ...
}
```
***