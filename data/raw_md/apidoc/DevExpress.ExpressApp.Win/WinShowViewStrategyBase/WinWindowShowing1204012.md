---
uid: DevExpress.ExpressApp.Win.WinShowViewStrategyBase.WinWindowShowing
name: WinWindowShowing
type: Event
summary: Occurs before a [](xref:DevExpress.ExpressApp.Win.WinWindow) is displayed.
syntax:
  content: public event EventHandler<WinWindowShowingEventArgs> WinWindowShowing
seealso: []
---
Handle the **WinWindowShowing** event to access the [Form](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.form) passed using the [WinWindowShowingEventArgs.Form](xref:DevExpress.ExpressApp.Win.WinWindowShowingEventArgs.Form) parameter. You can also access the [WinWindowShowingEventArgs.IsModal](xref:DevExpress.ExpressApp.Win.WinWindowShowingEventArgs.IsModal) parameter to determine if the form is modal. As the Show View Strategy can be changed during the application life cycle, it s recommended to subscribe to the **WinWindowShowing** event from the [XafApplication.ShowViewStrategyChanged](xref:DevExpress.ExpressApp.XafApplication.ShowViewStrategyChanged) event handler. In the snippet bellow, the main window is adjusted to be shown at the (10, 10) point, the modal window is adjusted to be shown at the center of the active form and all other forms are adjusted to be shown at the active form location.

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
// ...
static void Main() {
    // ...
    MySolutionWindowsFormsApplication winApplication = new MySolutionWindowsFormsApplication ();
    // ...
    winApplication.ShowViewStrategyChanged += WinApplication_ShowViewStrategyChanged;
    // ...
    winApplication.Setup();
    winApplication.Start();
}
private static void WinApplication_ShowViewStrategyChanged(object sender, EventArgs e) {
    WinApplication winApplication = (WinApplication)sender;
    if (winApplication.ShowViewStrategy != null) {
        winApplication.ShowViewStrategy.WinWindowShowing += ShowViewStrategy_WinWindowShowing;
    }
}
private static void ShowViewStrategy_WinWindowShowing(object sender, WinWindowShowingEventArgs e) {
    if (((WinShowViewStrategyBase)sender).MainWindow == null) {
        e.Form.StartPosition = FormStartPosition.Manual;
        e.Form.Location = new Point(10, 10);
    }
    else {
        if (e.IsModal) {
            e.Form.Owner = Form.ActiveForm;
            e.Form.StartPosition = FormStartPosition.CenterParent;
        }
        else {
            e.Form.StartPosition = FormStartPosition.Manual;
            e.Form.Location = (Form.ActiveForm != null) ? Form.ActiveForm.Location : new Point(10, 10);
        }
    }
}
```
***
