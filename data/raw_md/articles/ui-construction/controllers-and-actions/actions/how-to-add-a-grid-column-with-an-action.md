---
uid: "404559"
title: 'How to: Add a Grid Column with an Action (ASP.NET Core Blazor)'
---
# How to: Add a Grid Column with an Action (ASP.NET Core Blazor)

This topic explains how to add an inline [Action](xref:112622) to a List View's grid in an XAF ASP.NET Core Blazor application.

This functionality has the following limitations:
* XAF supports it only for @DevExpress.ExpressApp.Actions.SimpleAction or @DevExpress.ExpressApp.Actions.PopupWindowShowAction.
* The [Action](xref:112622) must mapped to one of the following [Action Container](xref:112610) categories: `Edit`, `RecordEdit`, or `ListView`.

> [!NOTE]
> For the purposes of this topic, you can use the **MainDemo.NET** (ASP.NET Core Blazor) application installed as a part of the XAF package. The default location of the application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\\Components\XAF_.

## Use a View Controller to Add a PopupWindowShowAction to a List View Grid

The instructions below explain how to add an Action to the `Employee` List View grid. The Action opens the selected `Employee` object's Detail View in a pop-up window.

1. Navigate to the _MainDemo.Module\Controllers_ folder. Create a new View Controller and name it _ShowPopupViewController_.

2. Replace the auto-generated code with the following code snippet:
    # [C#](#tab/tabid-csharp)
    ```csharp{11-12}
    using DevExpress.ExpressApp.Actions;
    using DevExpress.ExpressApp.Editors;
    using DevExpress.ExpressApp;
    using DevExpress.Persistent.Base;
    using MainDemo.Module.BusinessObjects;

    namespace MainDemo.Module.Controllers {
        public partial class ShowPopupViewController : ObjectViewController<ListView, Employee> {
            private PopupWindowShowAction popupAction;
            public ShowPopupViewController() : base() {
                popupAction = new PopupWindowShowAction(this, "ShowPopup", PredefinedCategory.ListView) {
                    SelectionDependencyType = SelectionDependencyType.RequireSingleObject,
                    ImageName = "State_Validation_Information"
                };
                popupAction.CustomizePopupWindowParams += PopupAction_CustomizePopupWindowParams;
            }
            private void PopupAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
                IObjectSpace objectSpace = e.Application.CreateObjectSpace(typeof(Employee));
                Employee currentObject = objectSpace.GetObject(ViewCurrentObject);
                DetailView detailView = e.Application.CreateDetailView(objectSpace, currentObject);
                detailView.ViewEditMode = ViewEditMode.Edit;
                e.View = detailView;
                e.Maximized = true;
            }
        }
    }
    ```
    [`SelectionDependencyType`]: xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType
    ***

3. Rebuild the project and run the application. Navigate to the `Employee` List View. Click the Action's icon in a grid row.

ASP.NET Core Blazor
:   ![XAF ASP.NET Core Blazor PopupWindowShowAction in the Employee List View Grid, DevExpress](~/images/xaf-blazor-inline-popupwindowshowaction-devexpress.gif)

## Use ActionAttribute to Add an Inline Action to a List View Grid

The instructions below explain how use a method of an entity class and @DevExpress.Persistent.Base.ActionAttribute to add an Action to the `Task` List View grid.

In ASP.NET Core Blazor application, when a user clicks the Action, the status of the selected `Task` object changes to `Completed.`

1. Navigate to the _MainDemo.Module\BusinessObjects_ folder and open the _Task.cs_ file.

2. Add the `MarkCompleted` method to the class:
    # [C# ASP.NET Core Blazor](#tab/tabid-csharp-blazor)
    ```csharp{12}
    // ...
    using System.ComponentModel;
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;
    using System.Text.Json.Serialization;

    namespace MainDemo.Module.BusinessObjects;

    [DefaultProperty(nameof(Subject))]
    public class Task : BaseObject {
        // ...
        [Action(ImageName = "State_Task_Completed", SelectionDependencyType = MethodActionSelectionDependencyType.RequireSingleObject)]
        public void MarkCompleted() {
            Status = TaskStatus.Completed;
        }
        // ...
    }
    //...
    ```
     ***
    @DevExpress.Persistent.Base.ActionAttribute maps the Action to the `RecordEdit` [Action Container](xref:112610) category.

3. Rebuild the project and run the application. Navigate to the `Task` List View and click the Action's icon in a grid row.

ASP.NET Core Blazor
:   ![XAF ASP.NET Core Blazor SimpleAction in the Task List View Grid, DevExpress](~/images/xaf-blazor-inline-simpleaction-devexpress.gif)

## Customize Inline Action Control

The code sample below demonstrates how to change the tooltip message of inline Actions. Actions are embedded in a List View (grid control) that displays `Task` objects.

Cast the `CustomizeControlEventsArgs.Control` object to `ListEditorInlineActionControl` and handle its `CustomizeInlineActionButton` event:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors.ActionControls;
using DevExpress.ExpressApp.SystemModule;
using MainDemo.Module.BusinessObjects; 

namespace MainDemo.Blazor.Server.Controllers {
    public class CustomizeInlineActionController : ObjectViewController<ListView, DemoTask> {
        private void Action_CustomizeControl(object sender, DevExpress.ExpressApp.Actions.CustomizeControlEventArgs e) {
            if (e.Control is ListEditorInlineActionControl control) {
                control.CustomizeInlineActionButton += Control_CustomizeInlineActionButton;
            }
        }
        private void Control_CustomizeInlineActionButton(object sender, DevExpress.ExpressApp.Blazor.Components.CustomizeInlineActionButtonEventArgs e) {
            if (e.DataItem is DemoTask task) {
                e.Tooltip = $"Change the status '{task.Status}' to 'Completed'";
            }
        }
        protected override void OnFrameAssigned() {
            base.OnFrameAssigned();
            var objectMethodController = Frame.GetController<ObjectMethodActionsViewController>();
            if (objectMethodController != null) {
                var action = objectMethodController.Actions.FirstOrDefault(s => s.Id == "Task.MarkCompleted");
                if (action != null) {
                    action.CustomizeControl += Action_CustomizeControl;
                }
            }
        }
    }
}
```