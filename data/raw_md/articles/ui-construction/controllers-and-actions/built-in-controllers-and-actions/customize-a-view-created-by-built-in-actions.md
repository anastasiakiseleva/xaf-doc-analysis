---
uid: "403731"
title: 'Customize ShowViewParameters for Built-in Simple Actions'
owner: Alexey Kazakov
---
# Customize ShowViewParameters for Built-in Simple Actions

To customize [](xref:DevExpress.ExpressApp.ShowViewParameters), handle the [](xref:DevExpress.ExpressApp.Actions.ActionBase.Executed) event. If an action owner controller has an event that allows you to customize [](xref:DevExpress.ExpressApp.ShowViewParameters), use this event instead of the `Executed` event. 

The example below demonstrates how to show a Detail View in a pop-up window when a user activates a [NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction) or a [ProcessCurrentObjectAction](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.ProcessCurrentObjectAction).

# [C#](#tab/tabid-csharp)

```csharp{7,10}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;

namespace MainDemo.Module.Controllers {
    public class ChangeWindowTypeToModalController : ViewController<ListView> {
        private void NewObjectAction_Executed(object sender, DevExpress.ExpressApp.Actions.ActionBaseEventArgs e) {
            e.ShowViewParameters.TargetWindow = TargetWindow.NewModalWindow;
        }
        private void ListViewProcessCurrentObjectController_CustomizeShowViewParameters(object sender, CustomizeShowViewParametersEventArgs e) {
            e.ShowViewParameters.TargetWindow = TargetWindow.NewModalWindow;
        }
        protected override void OnActivated() {
            base.OnActivated();
            NewObjectViewController newObjectViewController = Frame.GetController<NewObjectViewController>();
            if (newObjectViewController != null) {
                newObjectViewController.NewObjectAction.Executed += NewObjectAction_Executed;
            }
            ListViewProcessCurrentObjectController listViewProcessCurrentObjectController = Frame.GetController<ListViewProcessCurrentObjectController>();
            if(listViewProcessCurrentObjectController != null) {
                listViewProcessCurrentObjectController.CustomizeShowViewParameters += ListViewProcessCurrentObjectController_CustomizeShowViewParameters;
            }
        }
        protected override void OnDeactivated() {
            NewObjectViewController newObjectViewController = Frame.GetController<NewObjectViewController>();
            if(newObjectViewController != null) {
                newObjectViewController.NewObjectAction.Executed -= NewObjectAction_Executed;
            }
            ListViewProcessCurrentObjectController listViewProcessCurrentObjectController = Frame.GetController<ListViewProcessCurrentObjectController>();
            if(listViewProcessCurrentObjectController != null) {
                listViewProcessCurrentObjectController.CustomizeShowViewParameters -= ListViewProcessCurrentObjectController_CustomizeShowViewParameters;
            }
            base.OnDeactivated();
        }
    }
} 
```
***

[`ShowViewParameters`]: xref:DevExpress.ExpressApp.ShowViewParameters
