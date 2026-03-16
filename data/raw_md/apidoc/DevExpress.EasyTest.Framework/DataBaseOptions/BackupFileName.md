---
uid: DevExpress.EasyTest.Framework.DatabaseOptions.BackupFileName
name: BackupFileName
type: Property
summary: Returns the fully qualified name of the database backup file.
syntax:
  content: public string BackupFileName { get; }
  parameters: []
  return:
    type: System.String
    description: The database backup file name.
seealso: []
---
Use the [](xref:DevExpress.EasyTest.Framework.DatabaseOptions.#ctor(System.String,System.String,System.String,System.String,System.String,System.String,System.String,System.String)) constructor to specify the **BackupFileName** option.

Use the returned value in the [](xref:DevExpress.EasyTest.Framework.EasyTestFixtureContext.RestoreDB(System.String)) method.