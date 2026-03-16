---
uid: DevExpress.ExpressApp.IObjectSpaceProvider.SchemaUpdateMode
name: SchemaUpdateMode
type: Property
summary: Specifies how to handle compatibility checking for the database associated with the current [](xref:DevExpress.ExpressApp.IObjectSpaceProvider).
syntax:
  content: SchemaUpdateMode SchemaUpdateMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SchemaUpdateMode
    description: A [](xref:DevExpress.ExpressApp.SchemaUpdateMode) enumeration value that specifies how to handle database compatibility checking.
seealso: []
---
If you use [multiple databases](https://supportcenter.devexpress.com/ticket/details/e4896/how-to-connect-different-data-models-to-several-databases-within-a-single-application) and multiple Object Space Providers, you may want to prevent the application from updating the schema of certain databases. Use the **SchemaUpdateMode** property for this purpose.
