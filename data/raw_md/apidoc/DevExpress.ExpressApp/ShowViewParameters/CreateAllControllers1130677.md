---
uid: DevExpress.ExpressApp.ShowViewParameters.CreateAllControllers
name: CreateAllControllers
type: Property
summary: Specifies whether all Controllers relevant to the target [View](xref:112611) or its [Window](xref:112608) must be created.
syntax:
  content: |-
    [DefaultValue(true)]
    public bool CreateAllControllers { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` to create all relevant Controllers; `false` to create Controllers only from the @DevExpress.ExpressApp.ShowViewParameters.Controllers collection.'
seealso: []
---
When you display a View, the following Controllers are created:
* All Controllers from the [Application Model](xref:112580) that relate to your View or its Window.
* Controllers specified in the @DevExpress.ExpressApp.ShowViewParameters.Controllers collection.

Disable the `CreateAllControllers` property to create Controllers only from the @DevExpress.ExpressApp.ShowViewParameters.Controllers collection. In this case, add the `FillActionContainersController` to the @DevExpress.ExpressApp.ShowViewParameters.Controllers collection to display the Actions' buttons in the Template.