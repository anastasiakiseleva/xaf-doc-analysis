---
uid: "118592"
seealso:
- linkId: "403527"
title: 'Apply Application Model Changes to the Current View Immediately'
owner: Ekaterina Kiseleva
---
# Apply Application Model Changes to the Current View Immediately

The example in this topic shows how to update the [Application Model](xref:112579) and apply the changes to a View immediately. Your application doesn't reload the View if you follow the instructions below.

The code below implements two [Actions](xref:112622) that illustrate this approach to model customization.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Scheduler.Win;
using DevExpress.ExpressApp.Win.Editors;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.General;
// ...
public class RefreshViewControlsAfterModelChangesViewController :
        ObjectViewController<ListView, IEvent> {
    public RefreshViewControlsAfterModelChangesViewController() {
        new SimpleAction(this, "SwitchMasterDetailMode", 
         PredefinedCategory.View.ToString(), (s, e) => {
           
            // Obtain and save the view
            ListView savedView = (ListView)Frame.View;
            
            // Detach the View from the Frame 
            // Don't dispose the old view
            if(Frame.SetView(view: null, true, null, disposeOldView: false)) {
                
                // Change the Application Model
                MasterDetailMode defaultMasterDetailMode = MasterDetailMode.ListViewOnly;
                savedView.Model.MasterDetailMode = 
                    savedView.Model.MasterDetailMode == defaultMasterDetailMode ?
                    MasterDetailMode.ListViewAndDetailView : defaultMasterDetailMode;
                
                // Load Model changes into the View 
                savedView.LoadModel(false);
                
                // Re-attach the View back to its Frame
                Frame.SetView(savedView);
            }
        });
        new SimpleAction(this, "SwitchEditor", 
         PredefinedCategory.View.ToString(), (s, e) => {
            // Same algorithm as above
            var savedView = View;
            if(Frame.SetView(view: null, true, null, disposeOldView: false)) {
                Type defaultListEditorType = Application.Model.Views.DefaultListEditor;
                savedView.Model.EditorType = 
                    savedView.Model.EditorType == defaultListEditorType ? 
                    typeof(SchedulerListEditor) : defaultListEditorType;
                savedView.LoadModel(false);
                Frame.SetView(savedView);
            }
        });
    }
}
```
***

> [!CAUTION]
> We did not design this solution to be used in the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler or in an DevExpress.ExpressApp.Controller.OnActivated method override. In these cases, the solution usage may lead to unexpected results.