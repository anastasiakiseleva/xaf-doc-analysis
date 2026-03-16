---
uid: DevExpress.ExpressApp.Actions.ParametrizedAction
name: ParametrizedAction
type: Class
summary: A class implementing an Action that executes custom code when a user enters a value into the Action's editor.
syntax:
  content: 'public class ParametrizedAction : ActionBase'
seealso:
- linkId: DevExpress.ExpressApp.Actions.ParametrizedAction._members
  altText: ParametrizedAction Members
- linkId: "402155"
---
The `ParametrizedAction` class inherits the basic functionality of [Actions](xref:112622) from the [](xref:DevExpress.ExpressApp.Actions.ActionBase) class.

Use Parametrized Actions to execute custom code when a user enters a value into an Action's editor.

To access the input value, use the [ParametrizedAction.Value](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.Value) property. The value is of the string type by default.

To specify another type for input values (integer or `DateTime`), use the [ParametrizedAction.ValueType](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.ValueType) property. For each type, XAF displays an appropriate control.

> [!NOTE]
> For some value types, an [Action Container](xref:112610) cannot create an appropriate control. In this case, you have to implement a special Action Container.

Handle the [ParametrizedAction.Execute](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.Execute) event to execute custom code when a user enters a value into an Action's editor. Use the handler's [ParametrizedActionExecuteEventArgs.ParameterCurrentValue](xref:DevExpress.ExpressApp.Actions.ParametrizedActionExecuteEventArgs.ParameterCurrentValue) parameter to access the input value.

For more information about how to add a Parametrized Action to a Controller, refer to the following topic: [](xref:402155).

[!include[coderush-templates-actions-controllers](~/templates/coderush-templates-actions-controllers.md)]

ASP.NET Core Blazor
:   ![|ASP.NET Core Blazor Parametrized Action, DevExpress|](~/images/parametrized_action_blazor.png)
Windows Forms
:   ![Windows Forms Parametrized Action, DevExpress](~/images/parametrized_action_win.png)
