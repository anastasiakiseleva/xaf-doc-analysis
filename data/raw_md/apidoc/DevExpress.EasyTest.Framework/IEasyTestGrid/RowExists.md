---
uid: DevExpress.EasyTest.Framework.IEasyTestGrid.RowExists(DevExpress.EasyTest.Framework.EasyTestParameter[])
name: RowExists(EasyTestParameter[])
type: Method
summary: Checks whether the specified rows exist.
syntax:
  content: bool RowExists(params EasyTestParameter[] parameters)
  parameters:
  - id: parameters
    type: DevExpress.EasyTest.Framework.EasyTestParameter[]
    description: An array of objects that represent field names with the corresponding values.
  return:
    type: System.Boolean
    description: '**true** if the specified rows exist; otherwise, **false**.'
seealso: []
---
Example:

# [C#](#tab/tabid-csharp1)
 
```csharp{37}
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
                new BlazorApplicationOptions(BlazorAppName, @$"{Environment.CurrentDirectory}\..\..\..\..\MainDemo.Blazor.Server"),
                new WinApplicationOptions(WinAppName, @$"{Environment.CurrentDirectory}\..\..\..\..\MainDemo.Win\bin\EasyTest\MainDemo.Win.exe"));
            FixtureContext.RegisterDatabases(new DatabaseOptions(MainDemoDBName, "MainDemoDB", server: "(localdb)\\mssqllocaldb"));
        }
        public void Dispose() {
            FixtureContext.CloseRunningApplications();
        }

        [Theory]
        [InlineData(BlazorAppName)]
        [InlineData(WinAppName)]
        public void EditGridData(string applicationName) {
            FixtureContext.DropDB(MainDemoDBName);
            var appContext = FixtureContext.CreateApplicationContext(applicationName);
            appContext.RunApplication();
            appContext.GetForm().FillForm(("User Name", "Sam"));
            appContext.GetAction("Log In").Execute();

            appContext.Navigate("Tasks");

            Assert.True(appContext.GetGrid().RowExists(("Subject", "Task1")));
            // ...
        }
    }
}
```
***