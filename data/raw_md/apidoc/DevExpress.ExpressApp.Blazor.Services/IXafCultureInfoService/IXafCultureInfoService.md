---
uid: DevExpress.ExpressApp.Blazor.Services.IXafCultureInfoService
name: IXafCultureInfoService
type: Interface
summary: Declares members of a localization service.
syntax:
  content: public interface IXafCultureInfoService
seealso:
- linkId: DevExpress.ExpressApp.Blazor.Services.IXafCultureInfoService._members
  altText: IXafCultureInfoService Members
- linkId: "402956"
---
XAF features a built-in implementation of the `IXafCultureInfoService` interface. 

## Example

The code sample below demonstrates how to use `IXafCultureInfoService` to change the application localization.

[!include[<MySolution.Blazor.Server\Controllers\GermanCultureController.cs>](~/templates/platform_specific_file_path.md)]

# [C#](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp; 
using DevExpress.ExpressApp.Actions; 
using DevExpress.ExpressApp.Blazor; 
using DevExpress.ExpressApp.Blazor.Services; 
using DevExpress.Persistent.Base; 
// ...
public class GermanCultureController : ViewController { 
    BlazorApplication BlazorApplication => (BlazorApplication)Application; 
    IXafCultureInfoService CultureInfoService => (IXafCultureInfoService)BlazorApplication.ServiceProvider.GetService(typeof(IXafCultureInfoService)); 
    public GermanCultureController() { 
        SimpleAction myAction = new SimpleAction(this, "SetGermanCulture", PredefinedCategory.Edit); 
        myAction.Execute += async (s, e) => await CultureInfoService.SetCultureAsync("de"); 
    } 
} 
```

***
