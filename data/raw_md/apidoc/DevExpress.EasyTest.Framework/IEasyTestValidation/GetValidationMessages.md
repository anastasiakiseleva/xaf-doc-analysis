---
uid: DevExpress.EasyTest.Framework.IEasyTestValidation.GetValidationMessages
name: GetValidationMessages()
type: Method
summary: Returns an array of the displayed validation messages.
syntax:
  content: string[] GetValidationMessages()
  return:
    type: System.String[]
    description: The array of the displayed validation messages.
seealso: []
---
Example:

# [C#](#tab/tabid-csharp1)
 
```csharp{47}
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
            Assert.Equal("New Role", appContext.GetAction("New").Hint);
            appContext.GetAction("New").Execute();
            appContext.GetAction("Save").Execute();

            Assert.Equal("\"Name\" must not be empty.", appContext.GetValidation().GetValidationMessages().First());
        }
    }
}
```
***