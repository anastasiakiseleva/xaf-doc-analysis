---
uid: DevExpress.ExpressApp.Blazor.Services.IXafCultureInfoService.SetCultureAsync(System.String,System.String)
name: SetCultureAsync(String, String)
type: Method
summary: Saves the specified culture in `CookieRequestCultureProvider.DefaultCookie` and reloads the page.
syntax:
  content: Task SetCultureAsync(string culture, string uiCulture)
  parameters:
  - id: culture
    type: System.String
    description: A new culture.
  - id: uiCulture
    type: System.String
    description: A new UI culture.
  return:
    type: System.Threading.Tasks.Task
    description: A task that sets a new culture.
seealso:
- linkId: "402956"
---
After calling the **SetCultureAsync** method, the [](xref:DevExpress.ExpressApp.XafApplication) is recreated in a new culture. The new culture is read from cookies in `RequestLocalizationMiddleware`. 

Learn more: [How to: Localize an XAF Application (Blazor and WinForms)](xref:402956)