---
uid: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder`1.Add(System.Func{System.IServiceProvider,DevExpress.ExpressApp.IObjectSpaceProvider})
name: Add(Func<IServiceProvider, IObjectSpaceProvider>)
type: Method
summary: Adds the specified Object Space Provider to your application. This method allows you to use a custom Object Space Provider factory.
syntax:
  content: IObjectSpaceProviderServiceBasedBuilder<TContext> Add(Func<IServiceProvider, IObjectSpaceProvider> createObjectSpaceProviderFactoryDelegate)
  parameters:
  - id: createObjectSpaceProviderFactoryDelegate
    type: System.Func{System.IServiceProvider,DevExpress.ExpressApp.IObjectSpaceProvider}
    description: A delegate that creates the Object Space Provider.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder`1
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{10-13}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Blazor.ApplicationBuilder;
// ...
public class Startup {
   // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MySolutionBlazorApplication>();
            builder.ObjectSpaceProviders
                .Add((serviceProvider) => {
                    // ...
                })
                .AddNonPersistent();
        });
        // ...
    }
}
```
***
