---
uid: DevExpress.ExpressApp.ModuleBase.AdditionalExportedTypes
name: AdditionalExportedTypes
type: Property
summary: Contains manually specified business classes to be loaded to the [Application Model](xref:112580).
syntax:
  content: |-
    [Browsable(false)]
    public ExportedTypeCollection AdditionalExportedTypes { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ExportedTypeCollection
    description: An **ExportedTypeCollection** object which is a collection of types to be loaded to the [Application Model](xref:112580).
seealso:
- linkId: DevExpress.ExpressApp.ModuleBase.AdditionalControllerTypes
---
Use this property in a module constructor to manually export particular types to the Application Model. For example, you can export several types from another assembly, which are not used by your business classes and would not otherwise be available in the Application Model.

[!example[XAF - Customize an XPO Business Model at Runtime](https://github.com/DevExpress-Examples/xaf-customize-xpo-business-model-at-runtime)]