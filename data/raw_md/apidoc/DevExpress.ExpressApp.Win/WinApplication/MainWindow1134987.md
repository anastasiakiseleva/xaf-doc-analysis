---
uid: DevExpress.ExpressApp.Win.WinApplication.MainWindow
name: MainWindow
type: Property
summary: Gets the application's main [Window](xref:112608).
syntax:
  content: public override Window MainWindow { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Window
    description: A [](xref:DevExpress.ExpressApp.Window) object which is the application's main Window.
seealso: []
---
Uses the [WinApplication.ShowViewStrategy](xref:DevExpress.ExpressApp.Win.WinApplication.ShowViewStrategy) property to get the main Window (see [WinShowViewStrategyBase.MainWindow](xref:DevExpress.ExpressApp.Win.WinShowViewStrategyBase.MainWindow)). Returns `null`, if the `ShowViewStrategy` is `null`.