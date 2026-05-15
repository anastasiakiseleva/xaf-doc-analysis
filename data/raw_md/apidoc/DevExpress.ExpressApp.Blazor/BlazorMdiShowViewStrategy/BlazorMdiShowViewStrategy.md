---
uid: DevExpress.ExpressApp.Blazor.BlazorMdiShowViewStrategy
name: BlazorMdiShowViewStrategy
type: Class
summary: A [Show View Strategy](xref:DevExpress.ExpressApp.Win.WinShowViewStrategyBase) used to display a multiple document interface in XAF ASP.NET Core Blazor applications.
syntax:
  content: 'public class BlazorMdiShowViewStrategy : BlazorShowViewStrategy'
seealso:
- linkId: DevExpress.ExpressApp.Blazor.BlazorMdiShowViewStrategy._members
  altText: BlazorMdiShowViewStrategy Members
---
When the @DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.UIType property is set to `TabbedMDI`, the application UI displays a multiple document interface and uses the `BlazorMdiShowViewStrategy` to manage the display of [Views](xref:112611) in the UI.

XAF ASP.NET Core Blazor applications use the @DevExpress.Blazor.DxTabs component in Tabbed MDI mode. The number of tabs is limited to 10 (**default**). If the application displays the maximum number of tabs, users cannot open a new tab and receive a corresponding notification.

![|Max tab count notification](~/images/xaf-blazor-tabbedmdi-tablimit.png)

You can use the following properties to change the tab count limit or modify the application's behavior when the tab count exceeds the limit:

:  @DevExpress.ExpressApp.Blazor.BlazorMdiShowViewStrategy.MaxTabLimit
:  @DevExpress.ExpressApp.Blazor.BlazorMdiShowViewStrategy.TabOverflowStrategy

# [SolutionName.Blazor.Server\Program.cs](#tab/tabid-csharp)
 
```csharp
public static int Main(string[] args) {
    BlazorMdiShowViewStrategy.MaxTabLimit = 5;
    BlazorMdiShowViewStrategy.TabOverflowStrategy = TabOverflowStrategy.CloseLeastRecentTab;
    // ...
```
 
***