---
uid: "118592"
seealso:
- linkId: "403527"
title: 'Apply Application Model Changes to the Current View Immediately'
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

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.ExpressApp.Scheduler.Win
Imports DevExpress.ExpressApp.Win.Editors
Imports DevExpress.Persistent.Base
Imports DevExpress.Persistent.Base.General
' ...
Public Class RefreshViewControlsAfterModelChangesViewController
    Inherits ObjectViewController(Of ListView, IEvent)

    Public Sub New()
        New SimpleAction(Me, "SwitchMasterDetailMode",
         PredefinedCategory.View.ToString(), Sub(s, e)
            
            ' Obtain and save the view
            Dim savedView As ListView = CType(Frame.View, ListView)
            
            ' Detach the View from the Frame 
            ' Don't dispose the old view
            If Frame.SetView(view:=Nothing, True, Nothing, disposeOldView:=False) Then
                
                ' Change the Application Model
                Dim defaultMasterDetailMode As MasterDetailMode = MasterDetailMode.ListViewOnly
                savedView.Model.MasterDetailMode = If(savedView.Model.MasterDetailMode Is defaultMasterDetailMode, MasterDetailMode.ListViewAndDetailView, defaultMasterDetailMode)
                
                ' Load Model changes into the View
                savedView.LoadModel(False)
                
                ' Re-attach the View back to its Frame
                Frame.SetView(savedView)
            End If
        End Sub)
        New SimpleAction(Me, "SwitchEditor", PredefinedCategory.View.ToString(), Sub(s, e)
            ' Same algorithm as above
            Dim savedView = View
            If Frame.SetView(view:=Nothing, True, Nothing, disposeOldView:=False) Then
                Dim defaultListEditorType As Type = Application.Model.Views.DefaultListEditor
                savedView.Model.EditorType = If(savedView.Model.EditorType = defaultListEditorType, GetType(SchedulerListEditor), defaultListEditorType)
                savedView.LoadModel(False)
                Frame.SetView(savedView)
            End If
        End Sub)
    End Sub
End Class
```
[`Frame.View`]: xref:DevExpress.ExpressApp.Frame.View
[`Frame.SetView`]: xref:DevExpress.ExpressApp.Frame.SetView(DevExpress.ExpressApp.View,System.Boolean,DevExpress.ExpressApp.Frame,System.Boolean)
[`LoadModel`]: xref:DevExpress.ExpressApp.View.LoadModel*
***

> [!CAUTION]
> We did not design this solution to be used in the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler or in an DevExpress.ExpressApp.Controller.OnActivated method override. In these cases, the solution usage may lead to unexpected results.