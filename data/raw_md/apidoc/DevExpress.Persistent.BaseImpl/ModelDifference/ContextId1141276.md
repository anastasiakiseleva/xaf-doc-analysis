---
uid: DevExpress.Persistent.BaseImpl.ModelDifference.ContextId
name: ContextId
type: Property
summary: Specifies the context identifier of the current [](xref:DevExpress.Persistent.BaseImpl.ModelDifference) object that allows you to distinguish model differences designed for different applications using the same database.
syntax:
  content: public string ContextId { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string which is the context identifier.
seealso: []
---
For example, use the "Win" identifier for a WinForms application and "Blazor" - for an ASP.NET Core Blazor application in order to store WinForms and ASP.NET Core Blazor model differences separately.

You can pass the `contextId` parameter to the `ModelDifferenceDbStore` constructor to specify the current context when [setting up the database storage for model differences](xref:113698).