---
uid: DevExpress.ExpressApp.Actions.ActionBase.HasImage
name: HasImage
type: Property
summary: Indicates whether an [Action](xref:112622) has an image assigned to it.
syntax:
  content: |-
    [Browsable(false)]
    public bool HasImage { get; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true** if the current Action's **ImageName** is not null or empty; otherwise, **false**."
seealso: []
---
Use the [ActionBase.ImageName](xref:DevExpress.ExpressApp.Actions.ActionBase.ImageName) property to specify the name of the image that will be displayed  for the current Action. By default, the **ImageName** property is not set.