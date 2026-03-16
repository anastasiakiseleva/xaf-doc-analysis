---
uid: DevExpress.ExpressApp.ApplicationBuilder.IXafApplicationBuilder`1.AddBuildStep(System.Action{DevExpress.ExpressApp.XafApplication})
name: AddBuildStep(Action<XafApplication>)
type: Method
summary: Configures the application on its initialization. Allows you to customize the application during its creation.
syntax:
  content: TBuilder AddBuildStep(Action<XafApplication> configureApplication)
  parameters:
  - id: configureApplication
    type: System.Action{DevExpress.ExpressApp.XafApplication}
    description: 'The delegate that configures your application. '
  return:
    type: '{TBuilder}'
    description: The @DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder or @DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder type.
seealso: []
---
The following example demonstrates how to use this method:

# [MySolution.Win\Startup.cs](#tab/tabid-csharp-1)
```csharp{9-12}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        // ...
        builder.AddBuildStep(application => {
            application.ConnectionString = connectionString;
            // ...
        });
    }
    // ...
}
```

# [MySolution.Blazor.Server\Startup.cs](#tab/tabid-csharp-2)
```csharp{11-16}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Blazor.ApplicationBuilder;
// ...
public class Startup {
   // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MySolutionBlazorApplication>();
            // ...
            builder.AddBuildStep(application => {
                if (Configuration.GetConnectionString("ConnectionString") != null) {
                    application.ConnectionString = Configuration.GetConnectionString("ConnectionString");
                }
                // ...
            });
        });
        // ...
    }
}
```
***