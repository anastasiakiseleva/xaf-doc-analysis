---
uid: DevExpress.ExpressApp.Actions.ParametrizedAction.ShortCaption
name: ShortCaption
type: Property
summary: Specifies a caption of the button attached to a Parametrized Action's editor.
syntax:
  content: |-
    [DefaultValue("")]
    public string ShortCaption { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value representing a caption of the button displayed for the current Parametrized Action.
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionBase.Changed
---
A Parametrized Action is displayed via an editor and a button. The editor is used to enter a value, the button - for validating this value. Use the `ShortCaption` property to specify a caption for the button. The images below demonstrate the **Filter by Text** Action, displayed via a button with the **GO!** caption.

The value of this property is assigned to the [IModelAction.ShortCaption](xref:DevExpress.ExpressApp.Model.IModelAction.ShortCaption) property of the [Application Model](xref:112580)'s [!include[Node_Action](~/templates/node_action111373.md)] node. You can change this property's value using the [Model Editor](xref:112830).

The default value of this property is the value that is assigned to the `ShortCaption` property of the Application Model's **Action** node. If this property's value is not specified, its value is set to the `Caption` property value.