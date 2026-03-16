---
uid: DevExpress.ExpressApp.ModuleBase.Description
name: Description
type: Property
summary: Specifies a textual description of a module.
syntax:
  content: public string Description { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that represents the current module description.
seealso: []
---
This property returns an empty string, by default. However, to specify the current module description, set this property in the module constructor.

This property value is saved to the application's .log file.