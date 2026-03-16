---
uid: DevExpress.ExpressApp.SystemModule.WindowTemplateController.UpdateWindowStatusMessage
name: UpdateWindowStatusMessage()
type: Method
summary: Refreshes the status bar messages.
syntax:
  content: public void UpdateWindowStatusMessage()
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeWindowStatusMessages
- linkId: DevExpress.ExpressApp.SystemModule.WindowTemplateController.UpdateWindowCaption*
---
Below is the example of using this method in a custom View Controller. This controller adds a status message that contains the selected objects count, by handling the [WindowTemplateController.CustomizeWindowStatusMessages](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeWindowStatusMessages) event. The **UpdateWindowStatusMessage** method is invoked in the [ListEditor.SelectionChanged](xref:DevExpress.ExpressApp.Editors.ListEditor.SelectionChanged) event handler, to refresh the status message when end-user changes the selection.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
// ...
public class UpdateWindowStatusMessagesController : ViewController<ListView> {
    private WindowTemplateController windowTemplateController;
    public UpdateWindowStatusMessagesController() {
        TargetViewNesting = Nesting.Root;
    }
    protected override void OnActivated() {
        base.OnActivated();
        windowTemplateController = Frame.GetController<WindowTemplateController>();
        if (windowTemplateController != null) {
            windowTemplateController.CustomizeWindowStatusMessages += 
                windowTemplateController_CustomizeWindowStatusMessages;
        }
    }
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        View.Editor.SelectionChanged += Editor_SelectionChanged;
    }
    protected override void OnDeactivated() {
        View.Editor.SelectionChanged -= Editor_SelectionChanged;
        if (windowTemplateController != null) {
            windowTemplateController.CustomizeWindowStatusMessages -= 
                windowTemplateController_CustomizeWindowStatusMessages;
            windowTemplateController.UpdateWindowStatusMessage();
        }
        base.OnDeactivated();
    }
    void windowTemplateController_CustomizeWindowStatusMessages(
        object sender, CustomizeWindowStatusMessagesEventArgs e) {
        e.StatusMessages.Add(
            String.Format("Selected objects count: {0}", View.SelectedObjects.Count));
    }
    void Editor_SelectionChanged(object sender, EventArgs e) {
        windowTemplateController.UpdateWindowStatusMessage();
    }
}
```
***
