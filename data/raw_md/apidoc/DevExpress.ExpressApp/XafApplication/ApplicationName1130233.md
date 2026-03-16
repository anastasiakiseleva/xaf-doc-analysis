---
uid: DevExpress.ExpressApp.XafApplication.ApplicationName
name: ApplicationName
type: Property
summary: Specifies the application's name.
syntax:
  content: public string ApplicationName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that represents the application's name.
seealso: []
---
The **ApplicationName** value is not displayed in a UI (to set a visible name, use the [XafApplication.Title](xref:DevExpress.ExpressApp.XafApplication.Title) or [IModelApplication.Title](xref:DevExpress.ExpressApp.Model.IModelApplication.Title) property). Instead, it is used in the internal application flow. For instance, the **ApplicationName** is used to check if the database is compatible with the current application when the [XafApplication.CheckCompatibilityType](xref:DevExpress.ExpressApp.XafApplication.CheckCompatibilityType) property is set to **ModuleInfo**. If the application name differs from the name stored in the database, the following error occurs in this mode: "Database is designed for the 'MyApplication1' application while you are running the 'MyApplication2' application".

If you want to change the name stored in the database manually, locate the **ModuleInfo** table, and find the record with the **True** value in the **IsMain** column and update the **Name** value there:

``UPDATE ModuleInfo SET Name='NewApplicationName' WHERE IsMain='true'``

The **ModuleInfo** table is not created and the **ApplicationName** value is not stored in the database when the **XafApplication.CheckCompatibilityType** value is **DatabaseSchema**.

If you need to rename the application itself, set the **ApplicationName** property in code:

# [C#](#tab/tabid-csharp)

```csharp
static class Program {
   static void Main() {
      //...
      MySolutionWindowsFormsApplication application = new MySolutionWindowsFormsApplication();
      application.ApplicationName = "MyApplicationName";
      //...
   }
}
```
***

When you create an XAF application using the [Template Kit](xref:405447), the **ApplicationName** property is set to the application solution name.

> [!NOTE]
> To use the same database in several XAF applications with the **XafApplication.CheckCompatibilityType** set to **ModuleInfo**, set the **ApplicationName** of all applications to the same value.