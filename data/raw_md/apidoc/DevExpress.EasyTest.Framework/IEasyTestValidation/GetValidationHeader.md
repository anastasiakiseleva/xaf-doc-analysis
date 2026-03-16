---
uid: DevExpress.EasyTest.Framework.IEasyTestValidation.GetValidationHeader
name: GetValidationHeader()
type: Method
summary: Gets a header displayed within a validation message dialog. Supported only in WinForms applications.
syntax:
  content: string GetValidationHeader()
  return:
    type: System.String
    description: 'Validation header string.'
seealso: []
---

Example:

# [C#](#tab/tabid-csharp1)
 
```csharp{50}
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

            if (appContext.IsWin()) {
                Assert.Equal("\"Name\" Required.", appContext.GetValidation().GetValidationHeader());
            }
        }
    }
}
```
***