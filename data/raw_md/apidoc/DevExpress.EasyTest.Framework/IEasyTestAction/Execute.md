---
uid: DevExpress.EasyTest.Framework.IEasyTestAction.Execute(System.String)
name: Execute(String)
type: Method
summary: Executes an Action.
syntax:
  content: bool Execute(string parameter = null)
  parameters:
  - id: parameter
    type: System.String
    defaultValue: "null"
    description: Action execution parameter.
  return:
    type: System.Boolean
    description: '**true**, if the Action was executed; otherwise, **false**.'
seealso: []
---
Example:

# [C#](#tab/tabid-csharp1)
 
```csharp{39}
using System;
using System.Linq;
using DevExpress.EasyTest.Framework;
using Xunit;

[assembly: CollectionBehavior(DisableTestParallelization = true)]

namespace MainDemo.E2E.Tests {
    public class MainDemoTests : IDisposable {
        const string BlazorAppName = "MainDemoBlazor";
        const string WinAppName = "MainDemoWin";
        const string MainDemoDBName = "MainDemo";
        EasyTestFixtureContext FixtureContext { get; } = new EasyTestFixtureContext();

        public MainDemoTests() {
            FixtureContext.RegisterApplications(
                new BlazorApplicationOptions(BlazorAppName, 
                    @$"{Environment.CurrentDirectory}\..\..\..\..\MainDemo.Blazor.Server"),
                new WinApplicationOptions(WinAppName, 
                    @$"{Environment.CurrentDirectory}\..\..\..\..\MainDemo.Win\bin\EasyTest\MainDemo.Win.exe")
            );
            FixtureContext.RegisterDatabases(new DatabaseOptions(
                MainDemoDBName, "MainDemoDB", 
                server: "(localdb)\\mssqllocaldb")
            );
        }
        public void Dispose() {
            FixtureContext.CloseRunningApplications();
        }

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

            Assert.True(appContext.GetAction("New").Enabled);
            // ...
        }
    }
}
```
***