---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelActionBlazor.ConfirmUnsavedChanges
name: ConfirmUnsavedChanges
type: Property
summary: Specifies whether or not a confirmation dialog is displayed by a browser when there are unsaved changes and a user executes the current Action.
syntax:
  content: |-
    [DefaultValue(false)]
    bool ConfirmUnsavedChanges { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if a confirmation dialog is enabled; otherwise, **false**.'
seealso: []
---
The following confirmation is displayed by browser when a user clicks an Action whose **ConfirmUnsavedChanges** property is **true**.

![Action.ConfirmUnsavedChanges](~/images/confirmunsavedchanges120572.png)

You can change the **ConfirmUnsavedChanges** value in the [Model Editor](xref:112582).

![ConfirmUnsavedChanges_Action](~/images/confirmunsavedchanges_action120578.png)

By default, the **ConfirmUnsavedChanges** option is set to **true** for the following Actions:

* **Cancel**
* **ChangeVariant**
* **ChooseTheme**
* **DialogCancel**
* **DialogClose**
* **Edit**
* **Logoff**
* **NextObject**
* **New**
* **PreviousObject**
* **Refresh**

These are Actions, whose execution may lead to loss of unsaved data. If you have implemented a custom Action, you can set the **ConfirmUnsavedChanges** property to **true** to display a warning dialog before your Action is executed and there are unsaved data modifications in the current View.
