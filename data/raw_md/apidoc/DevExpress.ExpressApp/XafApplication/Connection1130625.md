---
uid: DevExpress.ExpressApp.XafApplication.Connection
name: Connection
type: Property
summary: Specifies the connection to the database used by the application.
syntax:
  content: |-
    [Browsable(false)]
    public IDbConnection Connection { get; set; }
  parameters: []
  return:
    type: System.Data.IDbConnection
    description: A [](xref:System.Data.IDbConnection) object representing an open connection to a data source.
seealso: []
---
To set the appropriate connection, specify the `Connection` property in code between the `XafApplication` object's creation and setup:

# [C#](#tab/tabid-csharp)

```csharp
static void Main() {
   //...
   MySolutionWindowsFormsApplication application = new MySolutionWindowsFormsApplication();
   application.Connection = new OracleConnection(...);
   application.Setup();
   //...
}
```
***

By default, SQL connection is used.