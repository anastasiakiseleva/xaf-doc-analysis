---
uid: DevExpress.EasyTest.Framework.ApplicationContextExtensions.GetForm(DevExpress.EasyTest.Framework.IApplicationContext)
name: GetForm(IApplicationContext)
type: Method
summary: Provides access to API that allows you to manipulate a currently displayed form.
syntax:
  content: public static IEasyTestForm GetForm(this IApplicationContext context)
  parameters:
  - id: context
    type: DevExpress.EasyTest.Framework.IApplicationContext
    description: The application's context.
  return:
    type: DevExpress.EasyTest.Framework.IEasyTestForm
    description: The API that allows you to manipulate a currently displayed form.
seealso: []
---
The code sample below demonstrates a test code that logs in the tested application and navigates to a _Roles_ view.

# [C#](#tab/tabid-csharp1)
 
```csharp{8}
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