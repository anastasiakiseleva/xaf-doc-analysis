---
uid: DevExpress.ExpressApp.ModuleBase.AdditionalControllerTypes
name: AdditionalControllerTypes
type: Property
summary: Contains manually specified [Controllers](xref:112621) to be loaded to the [Application Model](xref:112580).
syntax:
  content: |-
    [Browsable(false)]
    public ControllerTypeCollection AdditionalControllerTypes { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ControllerTypeCollection
    description: A **ControllerTypeCollection** object which is a collection of Controller types to be loaded to the [Application Model](xref:112580).
seealso:
- linkId: DevExpress.ExpressApp.ModuleBase.AdditionalExportedTypes
---
Use this property in a module constructor to manually export particular Controller types to the Application Model. For example, you can export several Controllers from another assembly, which would not otherwise be available in the Application Model.