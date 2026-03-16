---
uid: DevExpress.ExpressApp.ViewController.TargetViewType
name: TargetViewType
type: Property
summary: Specifies the type of the [View](xref:112611), for which a View Controller is intended.
syntax:
  content: |-
    [DefaultValue(ViewType.Any)]
    public ViewType TargetViewType { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ViewType
    description: A [](xref:DevExpress.ExpressApp.ViewType) enumeration value identifying a View type.
seealso:
- linkId: DevExpress.ExpressApp.ViewController.TargetObjectType
- linkId: DevExpress.ExpressApp.ViewController.TargetViewId
- linkId: DevExpress.ExpressApp.ViewController.TargetViewNesting
- linkId: "113103"
---
View Controllers can be activated for both List and Detail Views. You can use the **TargetViewType** property to  provide View Controller activation within the List, Detail, or any type of View.

> [!NOTE]
> The **TargetViewType** property affects only ViewController's activation. [Controller.FrameAssigned](xref:DevExpress.ExpressApp.Controller.FrameAssigned) and other events that are irrelevant to the view type always fire.

Alternatively, you can implement the generic [](xref:DevExpress.ExpressApp.ViewController`1) Controller instead of the [](xref:DevExpress.ExpressApp.ViewController) and specify the View's type, for which this Controller is intended, in the **ViewType** generic parameter. In this case, you do not need to perform an additional cast when you access the View.

The example below demonstrates how to add a @DevExpress.ExpressApp.Actions.PopupWindowShowAction to all [List Views](xref:112611#list-view) in an application.


# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
public class ShowListViewController : ViewController {
    public ShowListViewController() {
        TargetViewType = ViewType.ListView;
        PopupWindowShowAction showListViewAction = new PopupWindowShowAction(this, "ShowListView",
            PredefinedCategory.Edit);
        showListViewAction.CustomizePopupWindowParams += ShowListViewAction_CustomizePopupWindowParams;
    }
    private void ShowListViewAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
        Type objectType = typeof(Person);
        e.View = Application.CreateListView(objectType, true);
    }
}
```
***