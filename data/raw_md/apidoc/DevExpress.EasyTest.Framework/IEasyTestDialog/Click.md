---
uid: DevExpress.EasyTest.Framework.IEasyTestDialog.Click(System.String)
name: Click(String)
type: Method
summary: Clicks a specified dialog button.
syntax:
  content: void Click(string buttonCaption)
  parameters:
  - id: buttonCaption
    type: System.String
    description: A clicked button caption.
seealso: []
---
Example:

# [C#](#tab/tabid-csharp1)
 
```csharp{44}
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
        public void TestDialog(string applicationName) {
            FixtureContext.DropDB(MainDemoDBName);
            var appContext = FixtureContext.CreateApplicationContext(applicationName);
            appContext.RunApplication();
            appContext.GetForm().FillForm(("User Name", "Sam"));
            appContext.GetAction("Log In").Execute();

            appContext.Navigate("Tasks");
            appContext.GetAction("Delete").Execute();  
            Assert.Equal("Delete", appContext.GetDialog().Title);
            appContext.GetDialog().Click("Yes"); 
            // ...
        }
    }
}
```
***