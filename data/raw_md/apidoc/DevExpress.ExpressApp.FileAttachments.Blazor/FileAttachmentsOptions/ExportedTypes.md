---
uid: DevExpress.ExpressApp.FileAttachments.Blazor.FileAttachmentsOptions.ExportedTypes
name: ExportedTypes
type: Property
summary: Returns the list of Module-specific types exported to the Application Model.
syntax:
  content: public IList<Type> ExportedTypes { get; }
  parameters: []
  return:
    type: System.Collections.Generic.IList{System.Type}
    description: The list of Module-specific types exported to the Application Model.
seealso: []
---
The following example demonstrates how to specify this property:

[!include[<options.ExportedTypes.Add(typeof(MyFileDataClass));>](~/templates/AddFileAttachments_Blazor_example.md)]