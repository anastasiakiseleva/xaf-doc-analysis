---
uid: DevExpress.ExpressApp.SystemModule.CustomGetDefaultFileNameEventArgs.FileName
name: FileName
type: Property
summary: Specifies the name of the file to which data is exported.
syntax:
  content: public string FileName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string that is the name of the file to which data is exported.
seealso:
- linkId: "113287"
---
When handling the [ExportController.CustomGetDefaultFileName](xref:DevExpress.ExpressApp.SystemModule.ExportController.CustomGetDefaultFileName) event, use the **FileName** parameter to set a custom the name for the file to which data is exported.