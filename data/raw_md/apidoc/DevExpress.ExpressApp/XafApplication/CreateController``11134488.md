---
uid: DevExpress.ExpressApp.XafApplication.CreateController``1
name: CreateController<ControllerType>()
type: Method
summary: Creates a [Controller](xref:112621) of a specified type. If there is a Controller of the same type, assigns its settings to the new Controller.
syntax:
  content: |-
    public virtual ControllerType CreateController<ControllerType>()
        where ControllerType : Controller, new()
  typeParameters:
  - id: ControllerType
    description: ''
  return:
    type: '{ControllerType}'
    description: A [](xref:DevExpress.ExpressApp.Controller) of the specified type.
seealso: []
---
When you implement a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction), you may need to provide a custom Dialog Controller for the Action's pop-up Window. Use the **CreateController\<ControllerType>** method to create this custom Dialog Controller:

# [C#](#tab/tabid-csharp)

```csharp
private void MyPopupWindowShowAction_OnCustomizePopupWindowParams(Object sender,
      CustomizePopupWindowParamsEventArgs e) {
   //...
   e.DialogController = Application.CreateController<MyDialogController>();
}
```
***

This method creates a Controller of the specified type. If a Controller of the same type already exists, the [Controller.Actions](xref:DevExpress.ExpressApp.Controller.Actions) of the found Controller serve as a source for the [ActionBase.Model](xref:DevExpress.ExpressApp.Actions.ActionBase.Model) property of the new Controller's [Actions](xref:112622).