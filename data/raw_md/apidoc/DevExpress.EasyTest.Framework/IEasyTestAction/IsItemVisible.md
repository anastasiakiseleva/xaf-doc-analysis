---
uid: DevExpress.EasyTest.Framework.IEasyTestAction.IsItemVisible(System.String)
name: IsItemVisible(String)
type: Method
summary: Checks whether a specified item within a single choice action is visible.
syntax:
  content: bool IsItemVisible(string item = null)
  parameters:
  - id: item
    type: System.String
    defaultValue: "null"
    description: The checked item.
  return:
    type: System.Boolean
    description: '**true**, if the specified item is visible; otherwise, **false**.'
seealso: []
---
Example:

# [C#](#tab/tabid-csharp1)
 
```csharp{43,45}
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

            appContext.Navigate("Tasks");
            Assert.True(appContext.GetAction("Set Task").IsItemEnabled("Priority"));
            Assert.True(appContext.GetAction("Set Task").IsItemVisible("Priority"));
            Assert.True(appContext.GetAction("Set Task").IsItemEnabled("Status.In progress"));
            Assert.True(appContext.GetAction("Set Task").IsItemVisible("Status.In progress"));
            // ...
        }
    }
}
```
***