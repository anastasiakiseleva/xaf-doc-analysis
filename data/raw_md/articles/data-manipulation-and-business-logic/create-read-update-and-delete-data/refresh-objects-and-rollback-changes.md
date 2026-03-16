---
uid: "403622"
title: Refresh Objects and Rollback Changes
owner: Dmitry Egorov
seealso:
  - linkId: "403905"
---
# Refresh Objects and Rollback Changes

> [!spoiler][Useful API]
> 
> {|
> |-
> ! Members !! Description
> |-
> | colspan="2"| **Methods**:
> |-
> | [IObjectSpace.Refresh](xref:DevExpress.ExpressApp.IObjectSpace.Refresh) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.Refresh)]
> |-
> | [IObjectSpace.ReloadObject](xref:DevExpress.ExpressApp.IObjectSpace.ReloadObject(System.Object)) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.ReloadObject(System.Object))]
> |-
> | [IObjectSpace.Rollback](xref:DevExpress.ExpressApp.IObjectSpace.Rollback(System.Boolean)) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.Rollback(System.Boolean))]
> |-
> | colspan="2"| **Events**:
> |-
> | [IObjectSpace.Refreshing](xref:DevExpress.ExpressApp.IObjectSpace.Refreshing) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.Refreshing)]
> |-
> | [IObjectSpace.Reloaded](xref:DevExpress.ExpressApp.IObjectSpace.Reloaded) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.Reloaded)]
> |-
> | [IObjectSpace.ObjectReloaded](xref:DevExpress.ExpressApp.IObjectSpace.ObjectReloaded) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.ObjectReloaded)]
> |-
> | [IObjectSpace.CustomRefresh](xref:DevExpress.ExpressApp.IObjectSpace.CustomRefresh) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.CustomRefresh)]
> |-
> | [IObjectSpace.RollingBack](xref:DevExpress.ExpressApp.IObjectSpace.RollingBack) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.RollingBack)]
> |-
> | [IObjectSpace.CustomRollBack](xref:DevExpress.ExpressApp.IObjectSpace.CustomRollBack) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.CustomRollBack)]
> |}

In your code, you can modify business objects to create new ones, delete objects or edit objects' properties. If you perform this in an ObjectSpace different from the current View's ObjectSpace, refresh the current View's ObjectSpace to show changes in the View. Call the [IObjectSpace.Refresh](xref:DevExpress.ExpressApp.IObjectSpace.Refresh) method to show new data in the View.

[!include[](~/templates/refresh-code_snippet.md)]

[!include[](~/templates/objectreloaded-codesnippet.md)]

To reload an object changed in another Object Space in the current Object Space, use the [IObjectSpace.ReloadObject](xref:DevExpress.ExpressApp.IObjectSpace.ReloadObject(System.Object)) method. The following controller demonstrates how to open a Popup Window to edit an **Task** object and then, reload this object in the **Task** List View.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Editors;

public class EditTaskController : ObjectViewController<ListView, Task> {
    public EditTaskController() {
        PopupWindowShowAction action = new PopupWindowShowAction(this, "EditTask", DevExpress.Persistent.Base.PredefinedCategory.Edit);
        action.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        action.CustomizePopupWindowParams += Action_CustomizePopupWindowParams;
        action.Execute += Action_Execute;
    }
    private void Action_Execute(object sender, PopupWindowShowActionExecuteEventArgs e) {
        e.PopupWindowView.ObjectSpace.CommitChanges();
        ObjectSpace.ReloadObject(e.PopupWindowViewCurrentObject);
    }

    private void Action_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
        IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Task));
        Task task = (Task)objectSpace.GetObject(View.CurrentObject);
        DetailView detailView = Application.CreateDetailView(objectSpace, task);
        detailView.ViewEditMode = ViewEditMode.Edit;
        e.View = detailView;
    }
}
```
***

When you use a [Data Access Mode](xref:113683) that does not load real objects ([ServerView](xref:118450), [DataView](xref:118452), and [InstantFeedbackView](xref:118450)), use the [IObjectSpace.Refresh](xref:DevExpress.ExpressApp.IObjectSpace.Refresh) method to reload a changed object in the current List View.

