---
uid: DevExpress.ExpressApp.ModuleBase.GetControllerTypes
name: GetControllerTypes()
type: Method
summary: Returns a collection of [Controllers](xref:112621) loaded to the [Application Model](xref:112580).
syntax:
  content: public IEnumerable<Type> GetControllerTypes()
  return:
    type: System.Collections.Generic.IEnumerable{System.Type}
    description: An **IEnumerable\<Type>** collection of Controllers to be loaded to the Application Model.
seealso: []
---
The collection returned by the **GetControllerTypes** property is populated by the following types:

* Controllers provided by the module's [ModuleBase.AdditionalControllerTypes](xref:DevExpress.ExpressApp.ModuleBase.AdditionalControllerTypes) property.