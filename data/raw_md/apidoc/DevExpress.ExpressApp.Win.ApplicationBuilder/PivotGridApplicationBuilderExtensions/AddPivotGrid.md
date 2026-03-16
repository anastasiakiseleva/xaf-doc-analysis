---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.PivotGridApplicationBuilderExtensions.AddPivotGrid(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder})
name: AddPivotGrid(IModuleBuilder<IWinApplicationBuilder>)
type: Method
summary: '[!include[<\[Pivot Grid Module\](xref:113303)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IWinApplicationBuilder> AddPivotGrid(this IModuleBuilder<IWinApplicationBuilder> builder)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{10}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        builder.Modules
            // ...
            .AddPivotGrid()
        // ...
    }
    // ...
}
```
***