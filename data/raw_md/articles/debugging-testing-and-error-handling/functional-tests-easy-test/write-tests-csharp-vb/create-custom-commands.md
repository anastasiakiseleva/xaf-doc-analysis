---
uid: "403967"
title: 'Create Custom Commands'
owner: Alexey Kazakov
---
# Create Custom Commands

EasyTest exposes a set of API to implement most common use cases for functional testing. To implement custom testing scenarios and reuse them in testing scripts, you can create custom commands.

> [!NOTE]
> 
> To complete the steps in this article, your solution must already have an xUnit testing project. Follow the steps in this article to add a testing project to your XAF solution: [End-to-End Tests with xUnit](xref:403852).

A custom command is an extension for one of the following classes:

- [](xref:DevExpress.EasyTest.Framework.IApplicationContext)
- `IWinApplicationContext`
- `IBlazorApplicationContext`
- `IWebApplicationContext`


This code shows how to register a custom extension for the [](xref:DevExpress.EasyTest.Framework.IApplicationContext). This extension gets a document title for Blazor and WinForms applications.

# [C#](#tab/tabid-csharp1)
 
```csharp
public static class EasyTestExtensions {
    public static string GetDocumentTitle(this IApplicationContext context) {
        if (context is IBlazorApplicationContext blazorContext) {
            return blazorContext.WebDriver.ExecuteJavaScript<string>("return document.title");
        }
        else if (context is IWinApplicationContext winContext) {
            return winContext.GetDialog().Title;
        }
        throw new ArgumentException("The context is not a Blazor or WinForms context");
    }
}
```
***

You can use the extension as follows:

# [C#](#tab/tabid-csharp1)
 
```csharp
using DevExpress.EasyTest.Framework;
using OpenQA.Selenium.Support.Extensions;
using Xunit;

[assembly: CollectionBehavior(DisableTestParallelization = true)]

namespace MySolution.Module.E2E.Tests;

public class MySolutionTests : IDisposable {
    const string BlazorAppName = "MySolutionBlazor";
    const string WinAppName = "MySolutionWin";
    const string AppDBName = "MySolution";
    EasyTestFixtureContext FixtureContext { get; } = new EasyTestFixtureContext();

    public MySolutionTests() {
        FixtureContext.RegisterApplications(
            new BlazorApplicationOptions(
                BlazorAppName, 
                string.Format(@"{0}\..\..\..\..\MySolution.Blazor.Server",
                Environment.CurrentDirectory)
            ),
            new WinApplicationOptions(
                WinAppName, 
                string.Format(@"{0}\..\..\..\..\MySolution.Win\bin\EasyTest\net8.0-windows\MySolution.Win.exe", 
                Environment.CurrentDirectory)
            )
        );
        FixtureContext.RegisterDatabases(
            new DatabaseOptions(
                AppDBName, 
                "MySolutionEasyTest", 
                server: @"(localdb)\mssqllocaldb")
        );
    }
    public void Dispose() {
        FixtureContext.CloseRunningApplications();
    }
    [Theory]
    [InlineData(BlazorAppName)]
    [InlineData(WinAppName)]
    public void Test(string applicationName) {
        FixtureContext.DropDB(AppDBName);
        var appContext = FixtureContext.CreateApplicationContext(applicationName);
        appContext.RunApplication();
        appContext.GetForm().FillForm(("User Name", "Admin"));
        appContext.GetAction("Log In").Execute();
        appContext.Navigate("My Details");
        if (appContext.IsBlazor()) {
            Assert.Equal("MySolution", appContext.GetDocumentTitle());
        }
        if (appContext.IsWin()) {
            Assert.Equal("Admin - Application User", appContext.GetDocumentTitle());
        }
    }
}
```
***
