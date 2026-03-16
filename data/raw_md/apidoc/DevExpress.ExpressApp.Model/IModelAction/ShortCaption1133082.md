---
uid: DevExpress.ExpressApp.Model.IModelAction.ShortCaption
name: ShortCaption
type: Property
summary: Specifies the caption for a Parametrized Action's button.
syntax:
  content: string ShortCaption { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the caption for a Parametrized Action's button.
seealso: []
---
This property is considered for Actions of the [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction) type. A Parametrized Action is displayed via an editor and a button. The editor is used to enter a value, the button - for validating this value. Use this property to specify a caption for the button. For example, for the **FullTextSearch** Action's short caption can be set to "Go".

By default, this property is set to the current node's [IModelAction.Caption](xref:DevExpress.ExpressApp.Model.IModelAction.Caption) property value.