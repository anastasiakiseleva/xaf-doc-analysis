---
uid: DevExpress.ExpressApp.ApplicationBuilder.ILegacyInitializationXafApplication
name: ILegacyInitializationXafApplication
type: Interface
summary: Contains the @DevExpress.ExpressApp.ApplicationBuilder.ILegacyInitializationXafApplication.InitializeComponent method that you can use when you migrate your application configuration to the application builder.
syntax:
  content: public interface ILegacyInitializationXafApplication
seealso:
- linkId: DevExpress.ExpressApp.ApplicationBuilder.ILegacyInitializationXafApplication._members
  altText: ILegacyInitializationXafApplication Members
---
Implement this interface in your @DevExpress.ExpressApp.XafApplication descendant to call the **InitializeComponent** method on application initialization when you migrate your application configuration to the application builder. This allows you to perform this migration step by step. 

When you implement this interface in your application, additionally apply the following modifications: 

1. Remove the **InitializeComponents** method call from the application constructor.
2. Remove registration of system modules from the `InitializeComponents` method.
3. Change the `InitializeComponents` method's access modifier to `public`. 

**ASP.NET Core Blazor**  
**File**: _MySolution.Blazor.Server\BlazorApplication.cs_.  

# [C#](#tab/tabid-csharp-1)
```csharp
using DevExpress.ExpressApp.ApplicationBuilder;
// ...
public partial class MySolutionBlazorApplication : BlazorApplication, ILegacyInitializationXafApplication {
    // ...
    public MySolutionBlazorApplication() {
        //InitializeComponent();
    }
    // ...
    public void InitializeComponent() {
        //this.systemModule1 = new DevExpress.ExpressApp.SystemModule.SystemModule();
        //this.systemBlazorModule1 = new DevExpress.ExpressApp.Blazor.SystemModule.SystemBlazorModule();
        // ...
    }
}
```
***

**WinForms**  
**File**: _MySolution.Win\WinApplication.cs_.  

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.ApplicationBuilder;
// ...
public class MySolutionWindowsFormsApplication : WinApplication, ILegacyInitializationXafApplication {
    // ...
    public MySolutionWindowsFormsApplication() {
        //InitializeComponent();
    }
    public void InitializeComponent() {
        //this.systemModule1 = new DevExpress.ExpressApp.SystemModule.SystemModule();
        //this.winSystemModule1 = new DevExpress.ExpressApp.Win.SystemModule.SystemWindowsFormsModule();
        // ...
    }
}
```
*** 