---
uid: DevExpress.ExpressApp.Win.WinApplication.ShowViewStrategy
name: ShowViewStrategy
type: Property
summary: Specifies the Show View Strategy used in a Windows Forms application.
syntax:
  content: |-
    [Browsable(false)]
    public WinShowViewStrategyBase ShowViewStrategy { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Win.WinShowViewStrategyBase
    description: A [](xref:DevExpress.ExpressApp.Win.WinShowViewStrategyBase) object, specifying the Show View Strategy used in a Windows Forms application.
seealso:
- linkId: DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy
- linkId: DevExpress.ExpressApp.Win.ShowInSingleWindowStrategy
- linkId: DevExpress.ExpressApp.Win.MdiShowViewStrategy
- linkId: "404211"
---
General information on **Show View Strategies** is provided in the [](xref:DevExpress.ExpressApp.ShowViewStrategyBase) topic. An example of accessing this property to enable the [](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy) is shown below.

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

[!include[ShovViewStrategy_Events](~/templates/showviewstrategy_events111940_1130243.md)]