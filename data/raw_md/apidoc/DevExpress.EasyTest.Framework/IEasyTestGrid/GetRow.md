---
uid: DevExpress.EasyTest.Framework.IEasyTestGrid.GetRow(System.Int32,System.String[])
name: GetRow(Int32, String[])
type: Method
summary: Returns a collection of strings that represent row values.
syntax:
  content: string[] GetRow(int rowIndex, params string[] columnNames)
  parameters:
  - id: rowIndex
    type: System.Int32
    description: A row index.
  - id: columnNames
    type: System.String[]
    description: Names of columns whose values are returned.
  return:
    type: System.String[]
    description: A collection of strings that represent row values.
seealso: []
---
Example:

# [C#](#tab/tabid-csharp1)
 
```csharp{40}
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
            FixtureContext.RegisterDatabases(
                new DatabaseOptions(MainDemoDBName, "MainDemoDB", server: "(localdb)\\mssqllocaldb"));
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
            var firstRow = appContext.GetGrid().GetRow(0, "Subject", "Status", "Priority");
            Assert.Equal(new string[] { "Fix breakfast", "Completed", "Low" }, firstRow);
        }
    }
}
```
***