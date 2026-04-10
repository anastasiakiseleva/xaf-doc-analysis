---
uid: DevExpress.ExpressApp.Actions.ActionBase.ImageName
name: ImageName
type: Property
summary: Specifies a name of the image displayed for an [Action](xref:112622).
syntax:
  content: |-
    [DefaultValue(null)]
    public string ImageName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that represents the name of the current Action's image.
seealso:
- linkId: "404201"
- linkId: "404209"
- linkId: "112792"
---
Use the **ImageName** property to specify the name of the image that will be displayed  for the current Action. By default, this property is not set. You can set a value in the Controller's constructor. This value will be saved to the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Model.IModelAction) node. You can change this value in the [Model Editor](xref:112582). In a UI, the value which is specified in the Application Model's .xafml file loaded last will be displayed. For information on the order of Application Model differences loading, refer to the [Application Model Basics](xref:112580) topic.

When setting a value to this property, the [ActionBase.Changed](xref:DevExpress.ExpressApp.Actions.ActionBase.Changed) event is raised.

To learn the concept by which XAF displays images for Actions and other UI elements, refer to the [](xref:112792) topic.