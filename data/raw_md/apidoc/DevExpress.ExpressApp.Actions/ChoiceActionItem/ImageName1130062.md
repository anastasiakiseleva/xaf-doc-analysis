---
uid: DevExpress.ExpressApp.Actions.ChoiceActionItem.ImageName
name: ImageName
type: Property
summary: Specifies the name of the image which is displayed by the Choice Action Item's control.
syntax:
  content: |-
    [DefaultValue("")]
    public string ImageName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that represents the name of the current Choice Action Item image.
seealso: []
---
If the Choice Action Item's [ChoiceActionItem.Model](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Model) property is specified, the **ImageName** property value is stored in the corresponding Application Model Node. You can use the [Model Editor](xref:112830) to set the required image at design time.

When setting a value to this property, the [ChoiceActionBase.ItemsChanged](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.ItemsChanged) event is raised.

See the [Add an Action with Option Selection](xref:402159) topic, to learn how to use this property.

> [!NOTE]
> The Choice Action Item can be displayed without an image. It depends on the Action Container that displays this Action and the Action Container settings. Built-in Action Containers support image display.