---
uid: DevExpress.ExpressApp.Actions.ParametrizedAction.NullValuePrompt
name: NullValuePrompt
type: Property
summary: Specifies the default text that is displayed in the Parametrized Action's control.
syntax:
  content: |-
    [DefaultValue("")]
    public string NullValuePrompt { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the default text for the Parametrized Action's control.
seealso: []
---
Gets or sets the text displayed within the editor that contains the current Parametrized Action, when the editor's value is null.

This property is set to the value of the [IModelAction.NullValuePrompt](xref:DevExpress.ExpressApp.Model.IModelAction.NullValuePrompt) property of the corresponding **Application** | [!include[Node_Action](~/templates/node_action111373.md)] node.

If you set another value to this property in code, it will be saved to the Application Model.