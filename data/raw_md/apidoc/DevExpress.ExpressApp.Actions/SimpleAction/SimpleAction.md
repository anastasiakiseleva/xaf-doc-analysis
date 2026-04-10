---
uid: DevExpress.ExpressApp.Actions.SimpleAction
name: SimpleAction
type: Class
summary: A class that implements a Simple Action to execute custom code when a user clicks a button in an Action Container.
syntax:
  content: 'public class SimpleAction : ActionBase'
seealso:
- linkId: DevExpress.ExpressApp.Actions.SimpleAction._members
  altText: SimpleAction Members
---
The `SimpleAction` class inherits the basic functionality of [Actions](xref:112622) from the [](xref:DevExpress.ExpressApp.Actions.ActionBase) class. Built-in [Action Containers](xref:112610) display Simple Actions as buttons. The [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event holds custom code that runs in response to button clicks.

![|ASP.NET Core Blazor, Simple Action in XAF, DevExpress|](~/images/simple-action.png)

### Add a Simple Action

You can add a Single Choice Action to a [Controller](xref:112621) as described in the following topic: [](xref:402157).

Alternatively, you can use the [](xref:DevExpress.Persistent.Base.ActionAttribute) to convert a business class' method to an Action (see [How to: Create an Action Using the Action Attribute](xref:112619)).

[!include[coderush-templates-actions-controllers](~/templates/coderush-templates-actions-controllers.md)]
