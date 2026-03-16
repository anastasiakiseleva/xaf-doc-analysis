---
uid: DevExpress.EasyTest.Framework.ApplicationContextExtensions.GetAction(DevExpress.EasyTest.Framework.IApplicationContext,System.String)
name: GetAction(IApplicationContext, String)
type: Method
summary: Provides access to API that allows you to manipulate a specified Action.
syntax:
  content: public static IEasyTestAction GetAction(this IApplicationContext context, string actionName)
  parameters:
  - id: context
    type: DevExpress.EasyTest.Framework.IApplicationContext
    description: The application's context.
  - id: actionName
    type: System.String
    description: An Action's name.
  return:
    type: DevExpress.EasyTest.Framework.IEasyTestAction
    description: The API that allows you to manipulate a specified Action. Returns `null` if the Action was not found.
seealso: []
---

If a specified Action was not found, the `GetAction` returns `null`. 

# [C#](#tab/tabid-csharp1)
 
```csharp
appContext.GetAction("Edit")?.Execute();
```
***

The code sample below demonstrates a test code that logs in the tested application and navigates to a _Roles_ view.

# [C#](#tab/tabid-csharp1)
 
```csharp{9}
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