---
uid: DevExpress.EasyTest.Framework.IEasyTestGridEditing.FillRow(DevExpress.EasyTest.Framework.EasyTestParameter[])
name: FillRow(EasyTestParameter[])
type: Method
summary: Fills an edited row with new values.
syntax:
  content: void FillRow(params EasyTestParameter[] parameters)
  parameters:
  - id: parameters
    type: DevExpress.EasyTest.Framework.EasyTestParameter[]
    description: An array of objects that represent field names with the corresponding values.
seealso: []
---
Example:

# [C#](#tab/tabid-csharp1)

```csharp{35}
using System;
using System.Linq;
using DevExpress.EasyTest.Framework;
using Xunit;

[assembly: CollectionBehavior(DisableTestParallelization = true)]

namespace MainDemo.E2E.Tests {
    public class MainDemoTests : IDisposable {
        const string WinAppName = "MainDemoWin";
        const string MainDemoDBName = "MainDemo";
        EasyTestFixtureContext FixtureContext { get; } = new EasyTestFixtureContext();

        public MainDemoTests() {
            FixtureContext.RegisterApplications(
                new WinApplicationOptions(WinAppName, @$"{Environment.CurrentDirectory}\..\..\..\..\MainDemo.Win\bin\EasyTest\MainDemo.Win.exe"));
            FixtureContext.RegisterDatabases(new DatabaseOptions(MainDemoDBName, "MainDemoDB", server: "(localdb)\\mssqllocaldb"));
        }
        public void Dispose() {
            FixtureContext.CloseRunningApplications();
        }

        [Theory]
        [InlineData(WinAppName)]
        public void EditGridData(string applicationName) {
            FixtureContext.DropDB(MainDemoDBName);
            var appContext = FixtureContext.CreateApplicationContext(applicationName);
            appContext.RunApplication();
            appContext.GetForm().FillForm(("User Name", "Sam"));
            appContext.GetAction("Log In").Execute();

            appContext.Navigate("Tasks");

            appContext.GetGrid().InlineEdit(("Subject", "Fix breakfast"));
            appContext.GetGrid().FillRow(("Subject", "Test"), ("Status", "In progress"));
            appContext.GetGrid().InlineUpdate();
        }
    }
}
```
***
