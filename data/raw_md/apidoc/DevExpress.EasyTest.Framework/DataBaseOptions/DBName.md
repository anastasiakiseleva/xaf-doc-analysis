---
uid: DevExpress.EasyTest.Framework.DatabaseOptions.DBName
name: DBName
type: Property
summary: Returns the database name.
syntax:
  content: public string DBName { get; }
  parameters: []
  return:
    type: System.String
    description: A database name.
seealso: []
---
Use the [](xref:DevExpress.EasyTest.Framework.DatabaseOptions.#ctor(System.String,System.String,System.String,System.String,System.String,System.String,System.String,System.String)) constructor to specify the **DBName** option.

The @DevExpress.EasyTest.Framework.EasyTestFixtureContext.DropDB(System.String) and @DevExpress.EasyTest.Framework.EasyTestFixtureContext.RestoreDB(System.String) commands take this name as the parameter.