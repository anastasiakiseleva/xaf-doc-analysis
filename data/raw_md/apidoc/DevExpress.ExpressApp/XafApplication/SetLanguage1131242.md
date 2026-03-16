---
uid: DevExpress.ExpressApp.XafApplication.SetLanguage(System.String)
name: SetLanguage(String)
type: Method
summary: Sets the specified language for the current application when called before the application windows are shown.
syntax:
  content: public void SetLanguage(string languageName)
  parameters:
  - id: languageName
    type: System.String
    description: A string value representing the name of the language that must be used in the application.
seealso: []
---
XAF application uses the language specified by the [IModelApplication.PreferredLanguage](xref:DevExpress.ExpressApp.Model.IModelApplication.PreferredLanguage) property of the Application Model's [](xref:DevExpress.ExpressApp.Model.IModelApplication) node (see [Localization Basics](xref:112595)). To set another language during application startup, use the **SetLanguage** method. The method assigns the _languageName_ parameter value to the **PreferredLanguage** property. So, the specified language will be used even after the application is restarted.

See the [SetFormattingCulture](xref:DevExpress.ExpressApp.XafApplication.SetFormattingCulture(System.String)) article for an example.

> [!NOTE]
> 
> The **SetLanguage** method does not work for XAF ASP.NET Core Blazor UI applications. Refer to the following topic for information on how to localize XAF ASP.NET Core Blazor UI applications: [](xref:402956).


> [!NOTE]
> XAF applications are not designed to switch the language during application execution.