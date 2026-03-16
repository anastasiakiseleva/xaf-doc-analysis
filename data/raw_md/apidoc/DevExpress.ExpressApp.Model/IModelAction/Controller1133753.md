---
uid: DevExpress.ExpressApp.Model.IModelAction.Controller
name: Controller
type: Property
summary: Indicates the Controller in which the current Action is contained.
syntax:
  content: |-
    [DataSourceProperty("Application.ActionDesign.Controllers", new string[]{})]
    IModelController Controller { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.IModelController
    description: An [](xref:DevExpress.ExpressApp.Model.IModelController) object representing the Controller node corresponding to the Controller in which the current Action is contained.
seealso: []
---
You can use this property to determine the Controller that hosts the current Action:

![IModelAction.Controller](~/images/imodelaction.controller117534.png)

For details, refer to the [Determine an Action's Controller and Identifier](xref:113484) topic.