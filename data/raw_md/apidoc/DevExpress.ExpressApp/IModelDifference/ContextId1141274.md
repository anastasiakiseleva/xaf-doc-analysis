---
uid: DevExpress.ExpressApp.IModelDifference.ContextId
name: ContextId
type: Property
summary: Specifies the context identifier of the current [](xref:DevExpress.ExpressApp.IModelDifference) object that allows distinguishing model differences designed for different applications using the same database.
syntax:
  content: string ContextId { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string which is the context identifier.
seealso: []
---
For example, you can use the "Win" identifier for the WinForms application in order to store WinForms model differences separately. You can pass the _contextId_ parameter to the `ModelDifferenceDbStore` constructor to specify the current context when [setting up the database storage for model differences](xref:113698).