```csharp{13-15}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Blazor.ApplicationBuilder;
using DevExpress.Persistent.BaseImpl.EF;
// ...
public class Startup {
   // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<YourSolutionNameBlazorApplication>();
            builder.Modules
                // ...
                .AddOffice(options => {
                    <:0:>
                })
            // ...
        });
        // ...
    }
}
```