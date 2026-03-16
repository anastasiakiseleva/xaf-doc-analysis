---
uid: DevExpress.ExpressApp.Actions.ActionBase.Shortcut
name: Shortcut
type: Property
summary: Defines the keyboard shortcut that executes the current Action.
syntax:
  content: |-
    [DefaultValue(null)]
    public string Shortcut { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string that specifies the current Action's shortcut in an XAF ASP.NET Core Blazor or Windows Forms application.
seealso: []
---

Use this property to assign shortcuts for [Actions](xref:112622) in code.

The [Application Model](xref:112579) uses the [ActionBase.Shortcut](xref:DevExpress.ExpressApp.Actions.ActionBase.Shortcut) value as the default value for the [IModelAction.Shortcut](xref:DevExpress.ExpressApp.Model.IModelAction.Shortcut) property. You can override it in the [!include[Node_Action](~/templates/node_action111373.md)] node of the [Model Editor](xref:112582).

[!include[shortcutwindowsforms](~/templates/shortcutwindowsforms.md)]

[!include[shortcutblazor](~/templates/shortcutblazor.md)]
