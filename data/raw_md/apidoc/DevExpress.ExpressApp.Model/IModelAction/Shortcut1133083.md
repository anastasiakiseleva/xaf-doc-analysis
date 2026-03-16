---
uid: DevExpress.ExpressApp.Model.IModelAction.Shortcut
name: Shortcut
type: Property
summary: Defines the keyboard shortcut that executes the current Action.
syntax:
  content: string Shortcut { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string that specifies the current Action's shortcut.
seealso: []
---

You can change or look up the `Shortcut` property's value for each Action in the [!include[Node_Action](~/templates/node_action111373.md)] node in the [Model Editor](xref:112582).

![IModelActionProperties-Shortcuts](~/images/imodelactionproperties-shortcuts131319.png)

This property derives its value from the [ActionBase.Shortcut](xref:DevExpress.ExpressApp.Actions.ActionBase.Shortcut) property that defines default shortcuts.

[!include[shortcutwindowsforms](~/templates/shortcutwindowsforms.md)]

[!include[shortcutblazor](~/templates/shortcutblazor.md)]
