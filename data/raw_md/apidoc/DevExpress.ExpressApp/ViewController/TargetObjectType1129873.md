---
uid: DevExpress.ExpressApp.ViewController.TargetObjectType
name: TargetObjectType
type: Property
summary: Specifies a @DevExpress.ExpressApp.ViewController's target object type. The View Controller is activated only for [View](xref:112611)s that represent this type.
syntax:
  content: |-
    [DefaultValue(null)]
    public Type TargetObjectType { get; set; }
  parameters: []
  return:
    type: System.Type
    description: An object's type.
seealso:
- linkId: DevExpress.ExpressApp.ViewController.TargetViewId
- linkId: DevExpress.ExpressApp.ViewController.TargetViewNesting
- linkId: DevExpress.ExpressApp.ViewController.TargetViewType
- linkId: "113103"
---
View Controllers are activated for both [Windows and Frames](xref:112608). However, you can specify the type of objects represented by a View to provide a View Controller activation. For this purpose, specify the **TargetObjectType** property in code.

To make a single View Controller available in Views of different business object types simultaneously, set the **TargetObjectType** property in code to an interface or their base class type, which is implemented or inherited by all these business types respectively. Also, for the same task, you can specify several View identifiers using the [ViewController.TargetViewId](xref:DevExpress.ExpressApp.ViewController.TargetViewId) property.

> [!NOTE]
> The **TargetObjectType** property affects only ViewController's activation. [Controller.FrameAssigned](xref:DevExpress.ExpressApp.Controller.FrameAssigned) and other events that are irrelevant to the object type always fire.

The following example creates a [List View](xref:112611#list-view) and displays it via a @DevExpress.ExpressApp.Actions.PopupWindowShowAction.

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
        PopupWindowShowAction showListViewAction = new PopupWindowShowAction(this, "ShowListView",
            PredefinedCategory.Edit);
        this.TargetObjectType = typeof(Note);
        showListViewAction.CustomizePopupWindowParams += ShowListViewAction_CustomizePopupWindowParams;
    }
    private void ShowListViewAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
        Type objectType = typeof(Person);
        e.View = Application.CreateListView(objectType, true);
    }
}
```
***

Alternatively, you can implement the generic [](xref:DevExpress.ExpressApp.ObjectViewController`2) Controller instead of the [](xref:DevExpress.ExpressApp.ViewController) and specify the View and object type for which this Controller should be activated in the **ViewType** and **ObjectType** generic parameters.