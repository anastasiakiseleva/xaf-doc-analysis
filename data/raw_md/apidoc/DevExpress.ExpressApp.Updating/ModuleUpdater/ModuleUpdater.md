---
uid: DevExpress.ExpressApp.Updating.ModuleUpdater
name: ModuleUpdater
type: Class
summary: A [Module](xref:118046) updater. Allows you to handle a database update when the application version changes.
syntax:
  content: public class ModuleUpdater
seealso:
- linkId: DevExpress.ExpressApp.Updating.ModuleUpdater._members
  altText: ModuleUpdater Members
- linkId: 113239#how-database-is-updated-in-debug-mode
  altText: How Database is Updated in Debug Mode
- linkId: "113254"
---
An XAF application automatically checks application and database version compatibility on each start. The application compares module versions stored in the database with actual module versions. If versions do not match, the application collects persistent classes and automatically updates the database schema. However, you may need to convert the database data to reflect changes in your application.

When you add a new module via the **New Module** template, the _Updater.cs_ (_Updater.vb_) file is automatically created in the module's project. This file contains the declaration of the `ModuleUpdater` class' descendant. To handle differences between versions of an application, override the following descendant's methods:

| Method | Description |
|---|---|
| [ModuleUpdater.UpdateDatabaseBeforeUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseBeforeUpdateSchema) | Override this method to specify the database update code that should be executed before the database schema is updated. |
| [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) | Override this method to specify the database update code that should be executed after the database schema is updated. |

When you override these methods, you can use the following protected properties:

| Property | Description |
|---|---|
| `ObjectSpace` | This property provides access to an [](xref:DevExpress.ExpressApp.IObjectSpace) object that can be used for database update operations. Do not use a custom Object Space to update the database. Instead, perform all the required operations via the Object Space returned by this property. |
| `CurrentDBVersion` | This property returns the module assembly's version stored in the database. If the database does not exist, the version is 0.0.0.0. Use this information to determine which updates to the database are necessary. |

The following code snippet contains a sample `Updater` class' implementation. Note the use of the `ObjectSpace` and `CurrentDBVersion` properties.

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : DevExpress.ExpressApp.Updating.ModuleUpdater {
    public Updater(IObjectSpace objectSpace, Version currentDBVersion) : 
        base(objectSpace, currentDBVersion) { }
    public override void UpdateDatabaseAfterUpdateSchema() {
        base.UpdateDatabaseAfterUpdateSchema();
        if(CurrentDBVersion < new Version("1.5.0.0")){
            Position developerPosition =
                ObjectSpace.FirstOrDefault<Position>(position => position.Title == "Developer");
            if(developerPosition == null) {
                developerPosition = ObjectSpace.CreateObject<Position>();
                developerPosition.Title = "Developer";
                developerPosition.Save();
            }
            Position managerPosition = 
                ObjectSpace.FirstOrDefault<Position>(position => position.Title == "Manager");
            if(managerPosition == null) {
                managerPosition = ObjectSpace.CreateObject<Position>();
                managerPosition.Title = "Manager";
                managerPosition.Save();
            }
        }
        ObjectSpace.CommitChanges();
    }
}
```
***

&nbsp;

### Methods to Acess and Modify the Database Directly

You can use the following protected methods to execute custom SQL queries:

| Method | Description |
|---|---|
| `int ExecuteNonQueryCommand(string commandText, bool silent)` | Executes the SQL statement specified by the first parameter. If the second parameter is `false` and an error occurs when the statement is executed, an exception is thrown. If the second parameter is `true` and an error occurs when executing the statement, the return value is `-1`. On success, it returns the number of rows affected. |
| `object ExecuteScalarCommand(string commandText, bool silent)` | Executes the SQL query specified by the first parameter. If the second parameter is `false` and an error occurs when the query is executed, an exception is thrown. If the second parameter is `true` and an error occurs when the query is executed, the return value is `-1`. On success, the method returns the first column of the first row in the result set that matches the query. |
| `IDataReader ExecuteReader(string commandText, bool silent)` | Executes the SQL command specified by the first parameter. If the second parameter is `false` and an error occurs when the command is executed, an exception is thrown. If the second parameter is `true` and an error occurs when the query is executed, the returned value is `null`. On success, it returns the [IDataReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.idatareader) object. |

You can also use a number of protected methods that are wrappers for frequently used queries. The following table lists these methods. Note that currently these method implementations are specific to **Microsoft SQL Server** and may not work with different database engines. If you run into an exception when using these methods with non-Microsoft SQL Server databases, you can use the `ExecuteNonQueryCommand`, `ExecuteScalarCommand`, and `ExecuteReader` commands, and pass the corresponding query as a parameter.

| Method | Description |
|---|---|
| `bool TableExists(string name)` | Checks if a table exists. Returns `true` if the table exists; otherwise, `false`. |
| `void DropTable(string name, bool silent)` | Removes a table. If the second parameter is `false` and an error occurs during removal, an exception is thrown. If the second parameter is `true` and an error occurs during removal, an execution is not interrupted. |
| `void DropColumn(string tableName, string columnName)` | Removes a column from a table. |
| `void DropIndex(string tableName, string indexName)` | Removes an index from a table. |
| `void DropConstraint(string tableName, string constraintName)` | Removes a constraint from a table. |
| `void RenameTable(string sourceTableName, string destinationTableName)` | Renames a table. The first parameter is the old table name and the second is the new name. |
| `void RenameColumn(string tableName, string currentColumnName, string newColumnName)` | Renames a column. The first parameter is the table name, the second is the old column name, and the third is the new column name. |
| `void UpdateXPObjectType(string oldTypeName, string newTypeName, string assemblyName)` | Updates the [](xref:DevExpress.Xpo.XPObjectType) table. Finds the row where the `TypeName` column value is the same as the first parameter. In this row, changes the `TypeName` column to the value of the second parameter and changes the `AssemblyName` column to the value of the third parameter. The `UpdateXPObjectType` method only updates the database. You should manually reload changed `XPObjectType` instances using the [Session.Reload](xref:DevExpress.Xpo.Session.Reload*) method. |
| `void DeleteObjectType(string typeName)` | Deletes a row from the [](xref:DevExpress.Xpo.XPObjectType) table where the `TypeName` column value equals the passed string parameter. |

The protected methods described above log their activities in the application [log file](xref:112575). To see use examples of these methods, refer to the following topic: [](xref:113254).

> [!IMPORTANT]
> These methods cannot be used when the application is connected with the database via a [Middle-tier Application Server](xref:113439), a Data Store Pool ([XpoDefault.GetConnectionPoolString](xref:DevExpress.Xpo.XpoDefault.GetConnectionPoolString*)), or a [Cached Data Store](xref:9892). In these scenarios (except for the Middle-tier Application Server), another approach can be used: cast the object space to [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace), access its [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) member, and use corresponding methods of the [](xref:DevExpress.Xpo.Session) class. For more information, refer to the following topic: [](xref:8914).

> [!NOTE]
> You can have multiple module updaters per module. To register extra updaters, edit the [ModuleBase.GetModuleUpdaters](xref:DevExpress.ExpressApp.ModuleBase.GetModuleUpdaters(DevExpress.ExpressApp.IObjectSpace,System.Version)) method's implementation located in the _Module.cs_ (_Module.vb_) file. You can return [ModuleUpdater.EmptyModuleUpdaters](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.EmptyModuleUpdaters) in this method's override if your module does not require database updates. When this method is not overridden, the module updaters are automatically collected via the reflection.
