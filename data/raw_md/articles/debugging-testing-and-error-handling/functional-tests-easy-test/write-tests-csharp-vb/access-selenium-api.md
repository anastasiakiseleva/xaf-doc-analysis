---
uid: "403966"
title: 'Access Selenium API From Testing Code'
---
# Access Selenium API From Testing Code

A fixture context for Blazor applications has access to the Selenium API. With this functionality, you can perform any actions with a page that Selenium supports.

> [!NOTE]
> 
> To complete the steps in this article, your solution must already have an xUnit testing project. Follow the steps in this article to add a testing project to your XAF solution: [End-to-End Tests with xUnit](xref:403852).


Navigate to the testing project. Add the following test to the _Tests.cs_ file:

# [C#](#tab/tabid-csharp1)

```csharp
using DevExpress.EasyTest.Framework;
using OpenQA.Selenium.Support.Extensions;
using Xunit;

// ...
[Fact]
public void Test() {
    var appContext = FixtureContext.CreateApplicationContext(BlazorAppName);
    appContext.RunApplication();
    appContext.GetForm().FillForm(("User Name", "Sam"));
    appContext.GetAction("Log In").Execute();
    Assert.Equal(
        "XAF's Blazor UI Demo", 
        appContext.AsBlazor()
            .WebDriver
            .ExecuteJavaScript<string>("return document.title")
    );
}
```
***

## Create a Custom Command that Uses a Selenium API

After you create custom code that works with the application's web page, you may need to reuse this code in test scripts. To do this, create a custom EasyTest command.

This code shows how to register a custom command as an extension for the `IBlazorApplicationContext`.


# [C#](#tab/tabid-csharp1)
 
```csharp
public static class BlazorEasyTestExtensions {
    public static string GetDocumentTitle(this IBlazorApplicationContext context) {
        return context.WebDriver.ExecuteJavaScript<string>("return document.title");
    }
}
```
***


You can use the extension method as follows:

# [C#](#tab/tabid-csharp1)
 
```csharp
[Theory]
[InlineData(BlazorAppName)]
[InlineData(WinAppName)]
public void Test(string applicationName) {
    var appContext = FixtureContext.CreateApplicationContext(applicationName);
    appContext.RunApplication();
    appContext.GetForm().FillForm(("User Name", "Sam"));
    appContext.GetAction("Log In").Execute();
    //
    if(appContext.IsBlazor()) {
        Assert.Equal("XAF's Blazor UI Demo", appContext.AsBlazor().GetDocumentTitle());
    }
}
```
***

