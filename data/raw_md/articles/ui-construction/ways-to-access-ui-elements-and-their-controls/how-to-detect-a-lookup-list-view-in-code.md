---
uid: "112908"
seealso:
- linkId: "113103"
- linkId: DevExpress.ExpressApp.Controller.Active
- linkId: DevExpress.ExpressApp.Frame.GetController``1
- linkId: "112609"
title: 'How to: Detect a Lookup List View in Code'
---
# How to: Detect a Lookup List View in Code

This topic demonstrates how to check if the current [View](xref:112611) is a Lookup List View. This can be useful if you want to customize Lookups only, for instance, to hide the **New** [Action](xref:112622) displayed below the Lookup List View.

> [!NOTE]
> ASP.NET Core Blazor applications do not show the **New** Action in Lookup List Editors, but you can use this approach to implement other customizations.

Implement a [View Controller](xref:112621) that targets List Views only and override the **OnActivated** method. Check that the [Frame.Context](xref:DevExpress.ExpressApp.Frame.Context) value is **LookupControl** or **LookupWindow**. If the condition is true, this means that the current List View is a Lookup List View.

You can now, for example, deactivate the **New** Action in all Lookups. Use the [Frame.GetController\<ControllerType>](xref:DevExpress.ExpressApp.Frame.GetController``1) method to get the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController) and then use the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction) property to access the **New** Action.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
// ...
public class DeactivateNewActionInLookupsController : ViewController<ListView> {
    protected override void OnActivated() {
        base.OnActivated();
        if (Frame.Context == TemplateContext.LookupControl || Frame.Context == TemplateContext.LookupWindow) {
            NewObjectViewController controller = Frame.GetController<NewObjectViewController>();
            if (controller != null) {
                controller.NewObjectAction.Active.SetItemValue("LookupListView", false);
            }
        }
    }
}
```
***

Run an application to ensure that the **New** Action is deactivated in all Lookup List Views.

You can also detect a Lookup List View by its [View.Id](xref:DevExpress.ExpressApp.View.Id): all Lookup List Views have identifiers with the "_LookupListView" suffix by default. However, this also detects Views that were initially designed as Lookups, but are not used as Lookups.

> [!TIP]
> If you want to hide the **New** Action for a particular Lookup List View, find the corresponding View node in the [Model Editor](xref:112582) and set the [IModelView.AllowNew](xref:DevExpress.ExpressApp.Model.IModelView.AllowNew) property to **false**.