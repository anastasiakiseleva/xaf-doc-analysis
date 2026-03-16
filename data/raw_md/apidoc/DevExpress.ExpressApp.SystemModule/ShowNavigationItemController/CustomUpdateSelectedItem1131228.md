---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.CustomUpdateSelectedItem
name: CustomUpdateSelectedItem
type: Event
summary: Occurs when the [ShowNavigationItemController.ShowNavigationItemAction](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ShowNavigationItemAction)'s selected item is about to change, to reflect the change of the active [View](xref:112611).
syntax:
  content: public event EventHandler<CustomUpdateSelectedItemEventArgs> CustomUpdateSelectedItem
seealso:
- linkId: DevExpress.ExpressApp.Actions.SingleChoiceAction.SelectedItem
---
This event is raised by the [ShowNavigationItemController.UpdateSelectedItem](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.UpdateSelectedItem*) method. Handle this event to perform specific actions when the **ShowNavigationItemAction**'s selected item is about to change. You can perform the change of the selected item in a custom way. In this instance, set the event handler's **CustomUpdateSelectedItemEventArgs.Handled** parameter to **true**.

The following example specifies the selected item:
# [C#](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;

namespace MainDemo.Module {
    public class SelectedNavigationItemController : WindowController {
        public SelectedNavigationItemController() {
            TargetWindowType = WindowType.Main;
        }
        protected override void OnActivated() {
            base.OnActivated();
            Frame.GetController<ShowNavigationItemController>().CustomUpdateSelectedItem += SelectedNavigationItemController_CustomUpdateSelectedItem;
            Application.ViewShowing += Application_ViewShowing;
        }
        bool cancelSelectedNavigationItemChange;
        private void Application_ViewShowing(object sender, ViewShowingEventArgs e) {
            if (e.View.Id == "Employee_DetailView" && e.SourceFrame?.View?.Id == "Person_ListView") {
                cancelSelectedNavigationItemChange = true;
            }
        }
        private void SelectedNavigationItemController_CustomUpdateSelectedItem(object sender, CustomUpdateSelectedItemEventArgs e) {
            if (cancelSelectedNavigationItemChange) {
                cancelSelectedNavigationItemChange = false;
                e.Handled = true;
                e.ProposedSelectedItem = ((ShowNavigationItemController)sender).ShowNavigationItemAction.SelectedItem;
            }
        }
        protected override void OnDeactivated() {
            base.OnDeactivated();
            Frame.GetController<ShowNavigationItemController>().CustomUpdateSelectedItem -= SelectedNavigationItemController_CustomUpdateSelectedItem;
            Application.ViewShowing -= Application_ViewShowing;
        }
    }
}
```
***