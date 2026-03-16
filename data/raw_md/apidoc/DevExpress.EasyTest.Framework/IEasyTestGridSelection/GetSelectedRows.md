---
uid: DevExpress.EasyTest.Framework.IEasyTestGridSelection.GetSelectedRows(System.String[])
name: GetSelectedRows(String[])
type: Method
summary: Returns a dictionary that contains selected grid records and their indexes.
syntax:
  content: IReadOnlyDictionary<int, string[]> GetSelectedRows(params string[] columnNames)
  parameters:
  - id: columnNames
    type: System.String[]
    description: Names of columns whose values are returned.
  return:
    type: System.Collections.Generic.IReadOnlyDictionary{System.Int32,System.String[]}
    description: Row values across with their indexes.
seealso: []
---
Example:

# [C#](#tab/tabid-csharp1)
 
```csharp{41}
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

            appContext.GetGrid().SelectRows("Subject", "Task1");
            int[] selectedIndices = appContext.GetGrid().GetSelectedRowIndices();

            System.Collections.Generic.IReadOnlyDictionary<int, string[]> selectedRows = 
                appContext.GetGrid().GetSelectedRows("Subject", "Status", "Priority");
            Assert.Equal(new string[] { "Task1", "Completed", "High" }, selectedRows[selectedIndices[0]]);
        }
    }
}
```
***