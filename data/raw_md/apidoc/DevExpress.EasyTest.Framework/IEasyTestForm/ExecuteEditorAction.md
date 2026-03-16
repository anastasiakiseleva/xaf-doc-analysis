---
uid: DevExpress.EasyTest.Framework.IEasyTestForm.ExecuteEditorAction(System.String,System.String)
name: ExecuteEditorAction(String, String)
type: Method
summary: Executes an Action supplied by a Lookup Property Editor or an Object Property Editor.
syntax:
  content: void ExecuteEditorAction(string propertyName, string extraParameter = null)
  parameters:
  - id: propertyName
    type: System.String
    description: The edited property name.
  - id: extraParameter
    type: System.String
    defaultValue: "null"
    description: Lookup property editor's Action.
seealso: []
---
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
            appContext.GetForm().ExecuteEditorAction("Assigned To", "Edit");
            // ...
        }
    }
}
```
***