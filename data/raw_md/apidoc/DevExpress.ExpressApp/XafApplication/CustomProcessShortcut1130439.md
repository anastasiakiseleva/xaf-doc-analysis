---
uid: DevExpress.ExpressApp.XafApplication.CustomProcessShortcut
name: CustomProcessShortcut
type: Event
summary: Occurs when a [View](xref:112611) is created by its shortcut.
syntax:
  content: public event EventHandler<CustomProcessShortcutEventArgs> CustomProcessShortcut
seealso:
- linkId: DevExpress.ExpressApp.View.CreateShortcut
---
This event is raised as a result of calling the [XafApplication.ProcessShortcut](xref:DevExpress.ExpressApp.XafApplication.ProcessShortcut(DevExpress.ExpressApp.ViewShortcut)) method. You can handle this event to create a custom [](xref:DevExpress.ExpressApp.View) when a specific shortcut is passed as the handler's [CustomProcessShortcutEventArgs.Shortcut](xref:DevExpress.ExpressApp.CustomProcessShortcutEventArgs.Shortcut) parameter. Set the created View to the [CustomizePopupWindowParamsEventArgs.View](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.View) parameter. To cancel the default View creation, set the **Handled** parameter to **true**.

# [C#](#tab/tabid-csharp)

```csharp
public sealed partial class MySolutionModule : ModuleBase {
   // ...
    public override void Setup(XafApplication application) {
        base.Setup(application);
        application.CustomProcessShortcut += delegate (object sender, CustomProcessShortcutEventArgs e) {
            if ((e.Shortcut.ViewId == "MyDomainObject_ListView")) {
                IObjectSpace objectSpace = Application.CreateObjectSpace(e.Shortcut.ObjectClass);
                e.View = Application.CreateDashboardView(objectSpace, "MyDashboardView", true);
                e.Handled = true;
            }
        };
    }
    // ...
}
```
***