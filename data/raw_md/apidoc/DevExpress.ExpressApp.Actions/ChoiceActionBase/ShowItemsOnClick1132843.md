---
uid: DevExpress.ExpressApp.Actions.ChoiceActionBase.ShowItemsOnClick
name: ShowItemsOnClick
type: Property
summary: Specifies whether to display the drop-down with the current Action's items when the Action is clicked.
syntax:
  content: |-
    [DefaultValue(false)]
    public bool ShowItemsOnClick { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, if the drop-down list of items is shown when clicking the Action; `false` - if the Action is executed.'
seealso: []
---
To specify the Choice Action Item executed by default when `ShowItemsOnClick` is `false`, use the [ChoiceActionBase.DefaultItemMode](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.DefaultItemMode) property. You can set whether to always execute the first active item in the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection, or to execute the previously executed item.

The `ShowItemsOnClick` property's `false` value affects how [](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase) Actions' controls are rendered (for example, the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)'s control):

* As an Action's default button, if the `SingleChoiceAction.Items` collection (inherited from [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items)) contains one visible item.
* As a drop-down control with a triangle glyph, if the collection includes more than one item.

If the `ShowItemsOnClick` property's value is `true`, `ChoiceActionBase` Actions always have drop-down controls and you can execute the required action only from the drop-down.