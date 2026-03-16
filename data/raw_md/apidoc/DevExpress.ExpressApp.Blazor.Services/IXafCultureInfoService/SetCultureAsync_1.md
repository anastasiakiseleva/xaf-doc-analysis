---
uid: DevExpress.ExpressApp.Blazor.Services.IXafCultureInfoService.SetCultureAsync(System.String)
name: SetCultureAsync(String)
type: Method
summary: Saves the specified culture in `CookieRequestCultureProvider.DefaultCookie` and reloads the page.
syntax:
  content: Task SetCultureAsync(string culture)
  parameters:
  - id: culture
    type: System.String
    description: A new culture.
  return:
    type: System.Threading.Tasks.Task
    description: A task that sets a new culture.
seealso:
- linkId: "402956"
---
After calling the `SetCultureAsync` method, the [](xref:DevExpress.ExpressApp.XafApplication) is recreated in a new culture. The new culture is read from cookies in `RequestLocalizationMiddleware`. 

After calling the `SetCultureAsync`  method, the application is reloaded even if the new culture is the same as the previous culture (that means that the culture was not changed).

Learn more: [How to: Localize an XAF Application (Blazor and WinForms)](xref:402956)


## Example

The code sample below demonstrates how to use the `SetCultureAsync` method to change the application localization.

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
