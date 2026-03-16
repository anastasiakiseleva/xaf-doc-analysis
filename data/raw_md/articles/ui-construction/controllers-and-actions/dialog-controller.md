---
uid: "112805"
seealso: []
title: Dialog Controller
owner: Ekaterina Kiseleva
---
# Dialog Controller

The XAF has several [Controllers](xref:112621) that are automatically added to each [Frame](xref:112608) and provide basic functionality in applications ([](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController), [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController), etc.). However, this does not include the [](xref:DevExpress.ExpressApp.SystemModule.DialogController)- you need to add it manually if it is required. It is used to add the **Accept** and **Cancel** buttons in pop-up [Windows](xref:112608). For instance, the Dialog Controller is contained in the pop-up Window that is invoked by a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction). This Controller provides the **OK** and **Cancel** buttons. This topic describes the Dialog Controller's behavior and how to use it in a pop-up Window.

## Dialog Controller Overview
The **DialogController** is inherited from the [](xref:DevExpress.ExpressApp.WindowController) class. It contains the following [Actions](xref:112622):

{|
|-
                                                                                                                                                                                                                                                                                                                                                                                       
! Action
! Description
|-

| Accept Action
| Specified by the [DialogController.AcceptAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.AcceptAction) property. If the current pop-up Window contains a Detail View, this Action executes the **Save** Action of the Window's **ModificationsController**. You can cancel saving by setting the [DialogController.SaveOnAccept](xref:DevExpress.ExpressApp.SystemModule.DialogController.SaveOnAccept) property to **false**. This action has no effect if the current pop-up Window contains a List View. To implement custom code before executing the default code associated with this Action, handle the [DialogController.Accepting](xref:DevExpress.ExpressApp.SystemModule.DialogController.Accepting) event.

The pop-up Window is closed after executing the Accept Action by default. To cancel closing, set the [DialogController.CanCloseWindow](xref:DevExpress.ExpressApp.SystemModule.DialogController.CanCloseWindow) parameter to **false**.
|-

| Cancel Action
| Specified by the [DialogController.CancelAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.CancelAction) property. This Action closes the current pop-up Window by default. To implement custom code before closing the Window, handle the [DialogController.Cancelling](xref:DevExpress.ExpressApp.SystemModule.DialogController.Cancelling) event. You can also cancel closing the Window by setting the [DialogController.CanCloseWindow](xref:DevExpress.ExpressApp.SystemModule.DialogController.CanCloseWindow) property to **false**.
|-

| Close Action
| This Action is not displayed in a pop-up Window because the Template that represents the Window does not contain the [Action Container](xref:112610) associated with the Action. However, this Action is executed when pressing a selected row in the pop-up Window's List View. This Action's **ExecuteCompleted** event is handled by the corresponding event handler of the Accept Action, which closes the pop-up window.
|}

The Dialog Controller has the following specificities:

* If a pop-up Window with the Dialog Controller displays a [List View](xref:112611), the [ListViewProcessCurrentObjectController.ProcessCurrentObjectAction](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.ProcessCurrentObjectAction) (executed when you click or double-click a row) closes the pop-up window and accepts the dialog. This behavior is designed for Lookup List Views. To cancel closing the pop-up Window and process the **ProcessCurrentObjectAction** as in regular windows, set the [DialogController.CloseOnCurrentObjectProcessing](xref:DevExpress.ExpressApp.SystemModule.DialogController.CloseOnCurrentObjectProcessing) property to **false**.

* In addition to Dialog Controller members related to Actions, there is a [DialogController.WindowTemplateChanged](xref:DevExpress.ExpressApp.SystemModule.DialogController.WindowTemplateChanged) event. Handle it if you need to customize the [Template](xref:112609) assigned to a pop-up Window.

* You can customize the [](xref:DevExpress.ExpressApp.SystemModule.DialogController) class by inheriting from it.

* Dialog Controllers are not added to a Frame's [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection automatically. You need to add them manually when required. 

Read the sections below for details on how to use Dialog Controllers in pop-up Windows that are invoked after executing an Action, and in pop-up Windows invoked via [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) (see [Ways to Show a View](xref:112803)).

## Dialog Controllers in Pop-up Windows Invoked via ShowViewParameters Objects
To invoke a Window after an Action is executed, specify an [ActionBaseEventArgs.ShowViewParameters](xref:DevExpress.ExpressApp.Actions.ActionBaseEventArgs.ShowViewParameters) parameter of the Action's **Execute** event handler. The following conditions should be satisfied to create the invoked Window pop-up application:

* The [ShowViewParameters.TargetWindow](xref:DevExpress.ExpressApp.ShowViewParameters.TargetWindow) property is set to [TargetWindow.NewModalWindow](xref:DevExpress.ExpressApp.TargetWindow.NewModalWindow), and the [ShowViewParameters.Context](xref:DevExpress.ExpressApp.ShowViewParameters.Context) property is set to [TemplateContext.PopupWindow](xref:DevExpress.ExpressApp.TemplateContext.PopupWindow).
* The **TargetWindow** property is set to **TargetWindow.NewModalWindow**, the **Context** property is set to [TemplateContext.Undefined](xref:DevExpress.ExpressApp.TemplateContext.Undefined) (default value), and the [ShowViewParameters.Controllers](xref:DevExpress.ExpressApp.ShowViewParameters.Controllers) collection is not empty.
* The **TargetWindow** property is set to [TargetWindow.NewWindow](xref:DevExpress.ExpressApp.TargetWindow.NewWindow), and the **Context** property is set to **PopupWindow**.
* In [SDI mode](xref:404211), the **TargetWindow** property is set to **TargetWindow.NewWindow**, the **Context** property is set to [TemplateContext.Undefined](xref:DevExpress.ExpressApp.TemplateContext.Undefined) (default value), and the **ShowViewParameters.Controllers** collection is not empty.

> [!NOTE]
> For information on which templates are created for each template context and how to customize them on different platforms, refer to the following topic: [Templates](xref:112609).

To add a Dialog Controller to the pop-up window, use the [ShowViewParameters.Controllers](xref:DevExpress.ExpressApp.ShowViewParameters.Controllers) parameter of the Action's **Execute** event handler. The following code demonstrates how to create a List View in a pop-up window and add a Dialog Controller:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.SystemModule;
// ...
void myAction_Execute(Object sender, SimpleActionExecuteEventArgs e) {
   IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(MyBusinessClass));
   string listViewId = Application.FindListViewId(typeof(MyBusinessClass));
   e.ShowViewParameters.CreatedView = Application.CreateListView(
      listViewId,
      Application.CreateCollectionSource(objectSpace, typeof(MyBusinessClass), listViewId),
      true);
   e.ShowViewParameters.TargetWindow = TargetWindow.NewWindow;
   e.ShowViewParameters.Context = TemplateContext.PopupWindow;
   e.ShowViewParameters.Controllers.Add(Application.CreateController<DialogController>());
}
```
***

> [!NOTE]
> * You can add the built-in **DialogController** or a custom one that is inherited from it.
> * If the [ShowViewParameters.CreateAllControllers](xref:DevExpress.ExpressApp.ShowViewParameters.CreateAllControllers) property is set to **false** and you want the Actions' buttons in a Template, add the **FillActionContainersController** to the **Controllers** collection.

## Dialog Controllers in Pop-up Windows Invoked via PopupWindowShowAction Type Actions
The pop-up Windows which are invoked when pressing a [Pop-up Window Show Action](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) contain a [](xref:DevExpress.ExpressApp.SystemModule.DialogController) type Dialog Controller. You can change the behavior of the Dialog Controller's Actions as follows:

{|
|-

! Action
! Description
|-

| Accept Action
| Called "OK" by default. To set another caption, use the [PopupWindowShowAction.AcceptButtonCaption](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.AcceptButtonCaption) property.

This raises the [ActionBase.Executing](xref:DevExpress.ExpressApp.Actions.ActionBase.Executing), [PopupWindowShowAction.Execute](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.Execute) and [ActionBase.Executed](xref:DevExpress.ExpressApp.Actions.ActionBase.Executed) events, sequentially. Then, if the [PopupWindowShowActionExecuteEventArgs.CanCloseWindow](xref:DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs.CanCloseWindow) parameter of the **Execute** event handler is set to **true**, it saves the changes (if the Window contains a Detail View), and closes the Window. Otherwise, it does nothing.
|-

| Cancel Action
| Called "Cancel" by default. To set another caption, use the [PopupWindowShowAction.CancelButtonCaption](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CancelButtonCaption) property.

The [PopupWindowShowAction.Cancel](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.Cancel) event is raised when an end user clicks the current pop-up Window's Cancel button (see the table above).
|}

You can use the [PopupWindowShowAction.CustomizePopupWindowParams](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams) event handler's [CustomizePopupWindowParamsEventArgs.DialogController](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.DialogController) parameter to customize the default Dialog Controller the pop-up Window uses. You can also replace this Dialog Controller with a custom one. The code below demonstrates creating a List View in a Pop-up Window and adding a custom Dialog Controller.

# [C#](#tab/tabid-csharp)

```csharp
private void MyPopupWindowShowAction_CustomizePopupWindowParams(object sender, 
      CustomizePopupWindowParamsEventArgs e) {
   IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(MyBusinessClass));
   string listViewId = Application.FindListViewId(typeof(MyBusinessClass));
   e.View =  Application.CreateListView(
      listViewId,
      Application.CreateCollectionSource(objectSpace, typeof(MyBusinessClass), listViewId),
      true);
   e.DialogController = Application.CreateController<MyDialogController>();
}
```
***
