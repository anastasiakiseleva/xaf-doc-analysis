---
uid: DevExpress.EasyTest.Framework.ApplicationContextExtensions.Navigate(DevExpress.EasyTest.Framework.IApplicationContext,System.String)
name: Navigate(IApplicationContext, String)
type: Method
summary: Opens a specified [navigation item](xref:402131).
syntax:
  content: public static bool Navigate(this IApplicationContext context, string itemName)
  parameters:
  - id: context
    type: DevExpress.EasyTest.Framework.IApplicationContext
    description: The application's context.
  - id: itemName
    type: System.String
    description: A navigation item name.
  return:
    type: System.Boolean
    description: '**true** if a specified navigation item was opened successfully; otherwise, **false**.'
seealso: []
---
The code sample below demonstrates a test code that logs in the tested application and navigates to a _Roles_ view.

# [C#](#tab/tabid-csharp1)
 
```csharp{10}
[Theory]
[InlineData(BlazorAppName)]
[InlineData(WinAppName)]
public void ValidateRole(string applicationName) {
    FixtureContext.DropDB(MainDemoDBName);
    var appContext = FixtureContext.CreateApplicationContext(applicationName);
    appContext.RunApplication();
    appContext.GetForm().FillForm(("User Name", "Sam"));
    appContext.GetAction("Log In").Execute();
    appContext.Navigate("Roles");

    // ...
}
```
***