---
uid: "113656"
seealso: []
title: 'How to: Disable an Action When the Current View Has Unsaved Changes'
---
# How to: Disable an Action When the Current View Has Unsaved Changes

This topic demonstrates how to disable an [Action](xref:112622) when business objects loaded to the current [Object Space](xref:113707) are changed. For this purpose, the [IObjectSpace.ModifiedChanged](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedChanged) event is handled, and the [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property is set based on the [IObjectSpace.IsModified](xref:DevExpress.ExpressApp.IObjectSpace.IsModified) property.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using System;
// ...
public class ViewController1 : ViewController {
    SimpleAction action1;
    public ViewController1() {
        action1 = new SimpleAction(this, "Action1", DevExpress.Persistent.Base.PredefinedCategory.View);
    }
    protected override void OnActivated() {
        base.OnActivated();
        ObjectSpace.ModifiedChanged += ObjectSpace_ModifiedChanged;
        UpdateActionState();
    }
    void ObjectSpace_ModifiedChanged(object sender, EventArgs e) {
        UpdateActionState();
    }
    protected virtual void UpdateActionState() {
        action1.Enabled["ObjectSpaceIsModified"] = !ObjectSpace.IsModified;
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        ObjectSpace.ModifiedChanged -= ObjectSpace_ModifiedChanged;
    }
}
```
***

As a result, the **Action1** is grayed out in the UI when there are unsaved changes in the current View. It is impossible to execute the Action until changes are saved to a data store (e.g., using the **Save** Action). When the changes are saved, the **Action1** reverts to its normal state.