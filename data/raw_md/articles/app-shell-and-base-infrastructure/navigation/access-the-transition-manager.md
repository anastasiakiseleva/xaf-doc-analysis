---
uid: "116416"
seealso: []
title: Access the Transition Manager
---
# Access the Transition Manager

This topic demonstrates how to access the **Transition Manager** used to animate the transition on [](xref:DevExpress.XtraBars.Navigation.OfficeNavigationBar) root groups switching when the **OutlookStyleMainRibbonForm** [Template](xref:112609) is used in a WinForms application.

Perform the following steps to access the [](xref:DevExpress.Utils.Animation.TransitionManager) object and customize its settings.

1. Create a new [](xref:DevExpress.ExpressApp.WindowController) in your WinForms module.
2. Override the Controller's **OnActivated** method, get the **OfficeNavBarTransitionController** using the [Frame.GetController\<ControllerType>](xref:DevExpress.ExpressApp.Frame.GetController``1) method and subscribe to the **OfficeNavBarTransitionController.CustomizeTransition** event.
3. To access the **TransitionManager** object in the **CustomizeTransition** event handler, use the **e.TransitionManager** parameter.
4. Unsubscribe from the **CustomizeTransition** event in the overridden **OnDeactivated** method when the Controller is deactivated.
5. In the **CustomizeTransition** event handler, assign the **Transitions.TransitionType** property to the newly created object of the **CombTransition** type.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Win.SystemModule;
using DevExpress.Utils.Animation;
//...
public class TransitionCustomizationController : WindowController
{
    private OfficeNavBarTransitionController officeNavBarTransitionController;

    private void OnCustomizeTransition(object sender, CustomizeTransitionEventArgs e) {
        e.TransitionManager.Transitions[e.TransitionControl].TransitionType = new CombTransition();
    }
    protected override void OnActivated() {
        base.OnActivated();
        OfficeNavBarTransitionController officeNavBarTransitionController = Frame.GetController<OfficeNavBarTransitionController>();
        if(officeNavBarTransitionController != null) {
            officeNavBarTransitionController.CustomizeTransition += OnCustomizeTransition;
        }
    }
    protected override void OnDeactivated() {
        if(officeNavBarTransitionController != null) {
            officeNavBarTransitionController.CustomizeTransition -= OnCustomizeTransition;
        }
        base.OnDeactivated();
    }
    public TransitionCustomizationController() {
        TargetWindowType = WindowType.Main;
    }
}
```
***

Run the application to ensure that the transition type was changed.
