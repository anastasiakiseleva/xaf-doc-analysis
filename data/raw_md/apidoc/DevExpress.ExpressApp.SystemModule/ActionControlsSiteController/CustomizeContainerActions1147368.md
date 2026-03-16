---
uid: DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomizeContainerActions
name: CustomizeContainerActions
type: Event
summary: Occurs when [Actions](xref:112622) are added to the [Action Containers](xref:112610) according to the information specified in the **ActionDesign** | **ActionToContainerMapping** [Application Model](xref:112579) node.
syntax:
  content: public event EventHandler<CustomizeContainerActionsEventArgs> CustomizeContainerActions
seealso:
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/e1977/xaf-winforms-create-a-custom-action-type-and-a-custom-associated-control-barcheckitem
  altText: How to create a custom action type with a custom control (BarCheckItem), associated with it
---
Handle the **CustomizeContainerActions** event to customize the action-to-container mapping in code, without making changes in the Application Model. To do the same for [Templates](xref:112609) that does not support the **IActionControlsSite** interface, additionally handle the **FillActionContainersController.CustomizeContainerActions** event. The following code demonstrates how to remove the **SaveAndNew** Action from the **Save** container and add it to the **Edit** container:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.ExpressApp.Win.Templates.Bars.ActionControls;
// ...
public class CustomizeContainerActionsController : Controller {
    protected override void OnActivated() {
        base.OnActivated();
        Frame.GetController<ActionControlsSiteController>().CustomizeContainerActions += OnCustomizeContainerActions;
        Frame.GetController<FillActionContainersController>().CustomizeContainerActions += OnCustomizeContainerActions;
    }
    protected override void OnDeactivated() {
        Frame.GetController<ActionControlsSiteController>().CustomizeContainerActions -= OnCustomizeContainerActions;
        Frame.GetController<FillActionContainersController>().CustomizeContainerActions -= OnCustomizeContainerActions;
        base.OnDeactivated();
    }
    private void OnCustomizeContainerActions(object sender, CustomizeContainerActionsEventArgs e) {
        ActionBase actionToBeMoved = e.AllActions.Find("SaveAndNew");
        if ((actionToBeMoved != null) && (e.Category == "Save") && (e.Container is BarLinkActionControlContainer)) {
            e.ContainerActions.Remove(actionToBeMoved);
        }
        if ((actionToBeMoved != null) && (e.Category == "Edit")) {
            e.ContainerActions.Add(actionToBeMoved);
        }
    }
}
```
***

The result is demonstrated in the image below:

![ActionControlsSiteController_CustomizeContainerActions](~/images/actioncontrolssitecontroller_customizecontaineractions118802.png)
