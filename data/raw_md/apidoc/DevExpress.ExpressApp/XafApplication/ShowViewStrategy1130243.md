---
uid: DevExpress.ExpressApp.XafApplication.ShowViewStrategy
name: ShowViewStrategy
type: Property
summary: Specifies the application's Show View Strategy.
syntax:
  content: |-
    [Browsable(false)]
    public ShowViewStrategyBase ShowViewStrategy { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ShowViewStrategyBase
    description: A [](xref:DevExpress.ExpressApp.ShowViewStrategyBase) descendant that defines the application's Show View Strategy.
seealso: []
---
A Show View Strategy is the object that manages how to display [Views](xref:112611): whether to show a View in a lookup or common [Window](xref:112608), in a new or the current Window, in a pop-up or modal Window, and so on. XAF supplies several Show View Strategies:
* `DevExpress.ExpressApp.Blazor.BlazorMdiShowViewStrategy`
* `DevExpress.ExpressApp.Blazor.BlazorShowViewStrategy`
* [](xref:DevExpress.ExpressApp.Win.ShowInSingleWindowStrategy)
* [](xref:DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy)
* [](xref:DevExpress.ExpressApp.Win.WinShowViewStrategyBase)
* [](xref:DevExpress.ExpressApp.ShowViewStrategyBase)

XAF uses the following strategies by default:
ASP.NET Core Blazor
:   `BlazorShowViewStrategy`
Windows Forms
:   `ShowInMultipleWindowsStrategy`

The type of UI depends on the specified value of the [IModelOptionsBlazor.UIType](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.UIType) and [IModelOptionsWin.UIType](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.UIType) property respectively. For more information about Show View Strategies, refer to the [](xref:DevExpress.ExpressApp.ShowViewStrategyBase) class description.

To change the Show View Strategy, use the `ShowViewStrategy` property. The code below demonstrates how to set the `MdiShowViewStrategy` for the Windows Forms application. This strategy shows all Views in tabs.

Create an instance of the `MdiShowViewStrategy` class and assign it to the [WinApplication.ShowViewStrategy](xref:DevExpress.ExpressApp.Win.WinApplication.ShowViewStrategy) property in the _Program.cs_ file before the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method call.

# [C#](#tab/tabid-csharp)

```csharp
public static void Main(string[] arguments) {
    // ...
    winApplication.ShowViewStrategy = new MdiShowViewStrategy(winApplication);
    winApplication.Setup();
    winApplication.Start();
    //...
}
```
***

Alternatively, you can specify the [Application Model](xref:112580)'s `UIType` property of the **Options** node.

[!include[ShovViewStrategy_Events](~/templates/showviewstrategy_events111940_1130243.md)]