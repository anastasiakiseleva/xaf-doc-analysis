---
uid: DevExpress.ExpressApp.ModuleBase.GetExportedTypes
name: GetExportedTypes()
type: Method
summary: Returns a collection of business classes loaded to the [Application Model](xref:112580).
syntax:
  content: public IEnumerable<Type> GetExportedTypes()
  return:
    type: System.Collections.Generic.IEnumerable{System.Type}
    description: An **IEnumerable\<Type>** collection of business classes to be loaded to the Application Model.
seealso: []
---
The collection returned by the **GetExportedTypes** property is populated by the following business classes:

* Types provided by the module's [ModuleBase.AdditionalExportedTypes](xref:DevExpress.ExpressApp.ModuleBase.AdditionalExportedTypes) property.