---
uid: "403389"
title: 'Automatic Code Error Diagnostics'
owner: Alexey Kazakov
---
# Automatic Code Error Diagnostics

## Code Diagnostics

The code analysis feature helps you detect XAF-specific errors in your code as you type. When a code analyzer finds rule violations, they are reported in the code editor (as a squiggle under the invalid code) and in the Error List window.

![|xaf code analysis](~/images/code-analysis.png)

> [!NOTE]
> 
> Code analysis prerequisites and limitations: 
>
> * Only works with C# code 

### Enable Code Analysis

To turn on code analysis, add the `DevExpress.ExpressApp.CodeAnalysis` NuGet package to all projects in your XAF solution. 

### Disable Code Analysis

To turn off code analysis, remove the `DevExpress.ExpressApp.CodeAnalysis` NuGet package from your project.

You can suppress warning messages as described in the following Microsoft article: [How to suppress code analysis warnings](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/suppress-warnings).

![|code analysis suppress warning](~/images/code-analysis-suppress-warning.png)
# [C#](#tab/tabid-csharp)
 
```csharp
// ...
namespace MySolution.Module.Controllers {
#pragma warning disable XAF0005 // XAF Controller classes should be public
    class MyViewController : ViewController {
#pragma warning restore XAF0005 // XAF Controller classes should be public
        // ...
    }
}
```
***

## Project Diagnostics

The project analysis feature helps you detect XAF-specific errors in your project. You can find information on rule violations in the Error List window.

![|Error list with an XAF-specific error](~/images/project_analysis.png)

These diagnostics are part of the _DevExpress.ExpressApp.Design.NetCorePackage_ extension. They work when the extension is enabled and ensure the stable operation of the Model Editor.

## Supported Diagnostics

- [](xref:403391)
- [](xref:403392)
- [](xref:403423)
- [](xref:403424)
- [](xref:403425)
- [XAF0006: Invalid target platform. Change the target platform to "Any CPU" in project or solution properties](xref:403508)
- [](xref:403510)
- [](xref:403511)
- [](xref:403613)
- [](xref:403724)
- [](xref:403726)
- [](xref:403914)
- [](xref:403917)
- [](xref:403919)
- [](xref:403920)
- [](xref:403921)
- [](xref:403922)
- [](xref:404042)
- [](xref:404100)
- [](xref:404101)
- [](xref:404102)
- [](xref:404103)
- [XAF0023: Do not implement IObjectSpaceLink in XPO classes](xref:404104)
- [XAF0024: Do not implement IXafEntityObject in XPO classes](xref:404105)
- [](xref:404162)
- [](xref:404215)
- [XAF0027: Do not apply DomainComponentAttribute to an XPO business class](xref:404164)
- [](xref:404165)
- [](xref:404216)
- [](xref:404217)
- [](xref:404519)
- [](xref:405222)
- [](xref:405499)
- [](xref:405603)
