---
uid: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder`1.Add(System.Func{DevExpress.ExpressApp.XafApplication,DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs,DevExpress.ExpressApp.IObjectSpaceProvider})
name: Add(Func<XafApplication, CreateCustomObjectSpaceProviderEventArgs, IObjectSpaceProvider>)
type: Method
summary: Adds the specified Object Space Provider to your application. This method allows you to use a custom Object Space Provider factory.
syntax:
  content: IObjectSpaceProviderBuilder<TContext> Add(Func<XafApplication, CreateCustomObjectSpaceProviderEventArgs, IObjectSpaceProvider> createObjectSpaceProviderDelegate)
  parameters:
  - id: createObjectSpaceProviderDelegate
    type: System.Func{DevExpress.ExpressApp.XafApplication,DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs,DevExpress.ExpressApp.IObjectSpaceProvider}
    description: A delegate that creates the Object Space Provider.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder`1
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{8-11}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        builder.ObjectSpaceProviders
            .Add((application, e) => {
                // ...
            })
            .AddNonPersistent();
    }
    // ...
}
```
***