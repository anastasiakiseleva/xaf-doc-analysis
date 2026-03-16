---
uid: DevExpress.EasyTest.Framework.DatabaseOptions.Server
name: Server
type: Property
summary: Returns the SQL server instance name.
syntax:
  content: public string Server { get; }
  parameters: []
  return:
    type: System.String
    description: An SQL server instance name.
seealso: []
---
Use the [](xref:DevExpress.EasyTest.Framework.DatabaseOptions.#ctor(System.String,System.String,System.String,System.String,System.String,System.String,System.String,System.String)) constructor to specify the **Server** option.

For example, this attribute can be `(localdb)\mssqllocaldb` for Microsoft SQL Server or `.\SQLEXPRESS` for Microsoft SQL Server Express.