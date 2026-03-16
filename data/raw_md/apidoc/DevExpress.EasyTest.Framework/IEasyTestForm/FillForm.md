---
uid: DevExpress.EasyTest.Framework.IEasyTestForm.FillForm(DevExpress.EasyTest.Framework.EasyTestParameter[])
name: FillForm(EasyTestParameter[])
type: Method
summary: Fills fields with values.
syntax:
  content: void FillForm(params EasyTestParameter[] parameters)
  parameters:
  - id: parameters
    type: DevExpress.EasyTest.Framework.EasyTestParameter[]
    description: An array of objects that represent field names with the corresponding values.
seealso: []
---
The parameters specify field captions (or control names, or control tags in WinForms) and their values. Lookup fields are supported as well.

Example:

# [C#](#tab/tabid-csharp1)
 
```csharp
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
            appContext.GetForm().FillForm( 
                ("Subject", "Prepare financial statements for presentation to boards of directors"), 
                ("Priority", "Normal"), 
                ("Start Date", "1/11/2006"), 
                ("Due Date", "1/12/2006"), 
                ("Assigned To", "Mary Tellitson") 
            ); 
            // ...
        }
    }
}
```
***