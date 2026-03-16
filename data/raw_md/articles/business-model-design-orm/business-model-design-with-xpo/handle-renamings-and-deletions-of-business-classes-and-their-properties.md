---
uid: "113254"
seealso:
- linkId: DevExpress.ExpressApp.Updating.ModuleUpdater
- linkId: "112570"
- linkId: "112796"
- linkId: "113239"
- linkId: "2632"
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/t418166/how-to-upgrade-an-existing-project-to-the-allow-deny-permission-policy-migrate-to
  altText: How to upgrade an existing project to the Allow/Deny permission policy (migrate to PermissionPolicyUser and PermissionPolicyRole)
title: 'Handle Renamings and Deletions of Business Classes and their Properties'
owner: Ekaterina Kiseleva
---
# Handle Renamings and Deletions of Business Classes and their Properties

When developing an XAF application, you may be required to rename a persistent class or property due to refactoring specifics or changed business requirements. An XAF application launched in debug mode automatically creates required tables and columns in a database after adding new classes or properties (see the [Business Classes vs Database Tables](xref:112570) topic). However, when you rename a persistent class that already has a corresponding table in a database, this class is treated as new, and a new table is created. As a result, the old table remains unused and renamed class data becomes unavailable. The same holds true when you rename a persistent property that already has a corresponding column in a database table. A new column is created for the new property and the old column remains unused. At the development stage, these are not big problems - you can manually rename a required table/column or even create a new database. But this approach is not suitable when your application is already distributed to end-users, and they have databases with production data. This topic describes a way of automatically handling database structure changes when updating an XAF application, and avoiding the manual updating of all end-user databases. Several typical scenarios are provided, and you will either follow one of them or combine them to handle more complex changes:

* [Rename the Persistent Property](#rename-the-persistent-property)
* [Remove the Persistent Property](#remove-the-persistent-property)
* [Change the Persistent Property's Data Type](#change-the-persistent-propertys-data-type)
* [Rename the Persistent Class](#rename-the-persistent-class)
* [Rename the Persistent Class Participant in a Many-to-Many Relationship](#rename-the-persistent-class-participant-in-many-to-many-relationship)
* [Rename the Persistent Class Used as the Data Type in Analysis](#rename-the-persistent-class-used-as-the-data-type-in-analysis)
* [Rename the Persistent Class Used as the Data Type in Reports](#rename-a-persistent-class-used-as-the-data-type-in-reports)
* [Remove the Persistent Class](#remove-the-persistent-class)

> [!IMPORTANT]
> Some of the [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) class' protected methods, like **RenameTable** and **RenameColumn** demonstrated in this topic, are applicable when you are directly connected to Microsoft SQL Server, and may not work with different database engines. If you run into an exception when using these methods, you can pass an appropriate query to the **ExecuteNonQueryCommand**, **ExecuteScalarCommand** or **ExecuteReader** commands instead.

## Rename the Persistent Property
Lets assume you have the **Department** class with the **Office** property, and it is required to rename this property to **Room**.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions ]
public class Department : BaseObject {
    // ...
    private string office;
    public string Office {
        get { return office; }
        set { SetPropertyValue(nameof(Office), ref office, value); }
    }
    // ...
```
***

The following steps are required to rename a property, and handle the database and application model changes.

* **Rename the Property in C# sources**
	
	Use the Visual Studio **Refactor** | **Rename…** command to look through your solution sources and rename the property anywhere it is used.
	
	![HowToHandleDbChanges1](~/images/howtohandledbchanges1116575.png)
	
	Rebuild the solution to ensure that it is compilable, but do not run the application to avoid the creation of a new table column for the new property name.
* **Rename the Property in XAFML and BO Files**
	
	Refactoring tools do not update XAFML code. Use the **Find and Replace** dialog to look through XAFML files to rename a property. This dialog is available in Visual Studio using the **Edit** | **Find and Replace** | **Quick Replace** menu command or the CTRL-H shortcut. For instance, this may be required if you have a customized Department Detail View layout, or if the Office property is used in the filter criteria. Otherwise, the customizations will be lost.
	
	![HowToHandleDbChanges11](~/images/howtohandledbchanges11116585.png)
* **Rename the Table Column Holding the Renamed Property Values**
	
	The **Office** column in the database table storing the **Office** property values should be renamed before updating database schema.
	
	![HowToHandleDbChanges5](~/images/howtohandledbchanges5116579.png)
	
	The [ModuleUpdater.UpdateDatabaseBeforeUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseBeforeUpdateSchema) method is intended to update an application database before the database schema is updated. We will override this method to perform the required changes with the database structure. The [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) class exposes the **RenameColumn** protected method, which renames the required column in the database table. The following snippet illustrates how to rename the **Office** column in the **Department** table to **Room**.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	public class Updater : ModuleUpdater {
	    // ...
	    public override void UpdateDatabaseBeforeUpdateSchema() {
	        base.UpdateDatabaseBeforeUpdateSchema();
	        if (CurrentDBVersion < new Version("1.1.0.0") 
	            && CurrentDBVersion > new Version("0.0.0.0")) {
	            RenameColumn("Department", "Office", "Room");
	        }
	     }
	    // ...
	```
	***
	
	The "1.1.0.0" string is the application version in which changes are introduced. So, the column will be renamed only if the database version is less than "1.1.0.0". It is required to check if the database version is greater than "0.0.0.0", to make changes only when the database exists and is filled with data (the empty database version is "0.0.0.0", by default).
	
	The SQL command actually executed within this example is:
	
	``EXECUTE sp_rename N'Department.Office', N'Room"', 'COLUMN'``
	
	The SQL command text is written to the application [Log File](xref:112575) with the "ExecuteNonQueryCommand:" prefix before being executed. If an error occurs while executing the **RenameColumn** method, the exception text is also logged. However, the application execution is not interrupted in the case of an error. You can refer to the application log file for debugging purposes.
* Increment the application version, run the application and ensure that the property name changed and that data is available.

You can check that the column name was modified during the database update. If your database server is Microsoft SQL Server, run Microsoft SQL Management Studio and navigate to the modified column using the Object Explorer.

![HowToHandleDbChanges4](~/images/howtohandledbchanges4116578.png)

If you use another database server, use the appropriate database tool to check if the column name was actually modified.

## Remove the Persistent Property
If you remove the persistent property from the application code, it will not be visible in the application interface. But, the corresponding column will still exist in the application database. To remove a column, use the **DropColumn** protected method, exposed by the [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) class. This method removes the specified column on the specified table. The following snippet illustrates how to remove the **Room** column from the **Department** table.

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModuleUpdater {
    // ...
    public override void UpdateDatabaseBeforeUpdateSchema() {
        base.UpdateDatabaseBeforeUpdateSchema();
        if (CurrentDBVersion < new Version("1.1.0.0"))
            && CurrentDBVersion > new Version("0.0.0.0")) {
            DropColumn("Department", "Room");
        }
    }
    // ...
```
***

The "1.1.0.0" string is the application version in which changes are introduced. So, the column will be removed only if the database version is less than "1.1.0.0". Checking to determine if the database version is greater then "0.0.0.0" is required to handle a scenario when the database is empty or does not exist.

The SQL command actually executed within this example is:

``ALTER TABLE dbo.Department DROP COLUMN [Room]``

The SQL command text is written to the application [Log File](xref:112575) with the "ExecuteNonQueryCommand:" prefix before being executed. If an error occurs when executing the **DropColumn** method, the exception text is also logged. However, application execution is not interrupted. You can refer to the application log file for debugging purposes.

> [!NOTE]
> Removing a property affects the Layout of Detail Views where the property was previously visible. Layout adjustments may be required after removing a property.

You can check that the column was removed during a database update. If your database server is Microsoft SQL Server, run Microsoft SQL Management Studio and navigate to the modified table in the Object Explorer. If you use another database server, use the appropriate database tool to check if the column was actually removed.

## Change the Persistent Property's Data Type
Lets assume you have the **Department** class with the **Description** string property.

# [C#](#tab/tabid-csharp)

```csharp
public class Department : BaseObject {
    // ...
    private string description;
    public string Description {
        get { return description; }
        set { SetPropertyValue(nameof(Description), ref description, value); }
    }
    // ...
```
***

100 characters is the default size of a text property in **XPO**. For instance, if your database server is Microsoft SQL Server 2005, a column with the **nvarchar(100)** data type is created for the string property.

![HowToHandleDbChanges2](~/images/howtohandledbchanges2116576.png)

When the property's column is initially created, the data type can be specified by adding the **Size** or **DbType** attribute to the property's declaration (refer to the [How to Increase the Text Field Size of a Persistent Object](https://supportcenter.devexpress.com/ticket/details/a2728/how-to-increase-the-text-field-size-of-a-persistent-object) knowledge base article). 
To change the data type of an existing column, use the **ExecuteNonQueryCommand** protected method exposed by the [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) class. This method executes the specified SQL statement. The following snippet illustrates how to set the **Description** column data type to **nvarchar(200)**.

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModuleUpdater {
    // ...
    public override void UpdateDatabaseBeforeUpdateSchema() {
        base.UpdateDatabaseBeforeUpdateSchema();
        if (CurrentDBVersion < new Version("1.1.0.0") 
            && CurrentDBVersion > new Version("0.0.0.0"))  {
            ExecuteNonQueryCommand(
                "alter table Department alter column Description nvarchar(200)", true);
        }
    }
    // ...
```
***

The "1.1.0.0" string is the application version in which changes are introduced. So, the data type will be changed only if the database version is less than "1.1.0.0". It is required to check if the database version is greater then "0.0.0.0" to make changes only when the database exists and is filled with data (the empty database version is "0.0.0.0", by default). Available data types depend on the database server, so ensure that the specified data type is valid. The SQL command text is written to the application [Log File](xref:112575) with the "ExecuteNonQueryCommand:" prefix before being executed. If an error occurs when executing the **ExecuteNonQueryCommand** method, an exception text is also logged. However, application execution is not interrupted. You can refer to the application log file for debugging purposes. If it is required to throw an exception when an error occurs, set the second parameter of the **ExecuteNonQueryCommand** method to **false**.

> [!NOTE]
> Ensure that the Property Editor allows you to input text of the required size. In the [Model Editor](xref:112582), modify the **Size** property of the **BOModel** | **Department** | **Description** node, if necessary. This attribute specifies the maximum number of characters that can be typed in the Property Editor.

You can check that the data type was modified during the database update. If your database server is Microsoft SQL Server, run Microsoft SQL Management Studio and navigate to the modified column in the Object Explorer.

![HowToHandleDbChanges3](~/images/howtohandledbchanges3116577.png)

If you use another database server, use the appropriate database tool to check if the data type was actually modified.

## Rename the Persistent Class
Lets assume you have a **Department** persistent class that should be renamed to **Division**. The following steps are required to rename the class and handle the required database and application model changes:

* **Rename the Class in C# Sources**
	
	Use the Visual Studio **Refactor**| **Rename…** command to look through your solution sources and rename the class anywhere it is used.
	
	![HowToHandleDbChanges6](~/images/howtohandledbchanges6116580.png)
	
	Rebuild the solution to ensure that it is compilable, but do not run the application to avoid creating a new table for the new class name.
* **Rename the Class in XAFML and BO Files**
	
	Refactoring tools do not update XAFML code. Use the **Find and Replace** dialog to look through XAFML files' code to rename the class anywhere it is used. This dialog is available in Visual Studio using the **Edit** | **Find and Replace** | **Quick Replace** menu command or the CTRL-H shortcut.
	
	![HowToHandleDbChanges9](~/images/howtohandledbchanges9116583.png)
	
	> [!NOTE]
	> The List View and Detail View IDs should be modified. For instance, the "Department_ListView" ID should be renamed to "Division_ListView". So, do not check the "Match whole word" option.
* **Rename the Database Table Holding the Renamed Class Data and Update the XPObjectType Table**
	
	The **Department** table in the database should be renamed before updating the database schema.
	
	![HowToHandleDbChanges8](~/images/howtohandledbchanges8116582.png)
	
	The [](xref:DevExpress.Xpo.XPObjectType) table, automatically created and containing all the valid persistent object types, should also be modified.
	
	![HowToHandleDbChanges7](~/images/howtohandledbchanges7116581.png)
	
	The [ModuleUpdater.UpdateDatabaseBeforeUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseBeforeUpdateSchema) method is intended to update an application database before the database schema is updated. We will override this method to perform the required changes in the database structure. The [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) class exposes the **RenameTable** and **UpdateXPObjectType** protected methods. The **RenameTable** method renames the specified table. The first parameter is the old name and the second is the new name. The **UpdateXPObjectType** method updates the **XPObjectType** table. This method finds the row where the TypeName column value equals the first parameter. In this row, it changes the TypeName column to the value specified by the second parameter and changes the AssemblyName column to the value specified by the third parameter. The following snippet illustrates how to rename the **Department** table to **Division** and update the **XPObjectType** table.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	public class Updater : ModuleUpdater {
	    // ...
	    public override void UpdateDatabaseBeforeUpdateSchema() {
	        base.UpdateDatabaseBeforeUpdateSchema();
	        if (CurrentDBVersion < new Version("1.1.0.0") 
	            && CurrentDBVersion > new Version("0.0.0.0")) {
	            RenameTable("Department", "Division");
	            UpdateXPObjectType(
	                "MySolution.Module.Department", "MySolution.Module.Division", "MySolution.Module");
	        }
	    }
	    // ...
	```
	***
	
	The "1.1.0.0" string is the application version in which changes are introduced. So, the column will be removed only if the database version is less than "1.1.0.0". Checking if the database version is greater than "0.0.0.0" is required to make changes only when the database exists and is filled with data.
	
	The SQL commands actually executed within this example are:
	
	``sp_rename 'Department', 'Division', 'OBJECT'``
	 
	``update XPObjectType set TypeName = 'MySolution.Module.Division', AssemblyName = 'MySolution.Module'``
    
	``where TypeName = 'MySolution.Module'``
	
	The SQL command text is written to the application [Log File](xref:112575) with the "ExecuteNonQueryCommand:" prefixes before being executed. If an error occurs when executing the **RenameTable** or **UpdateXPObjectType** method, the exception text is also logged. However, in the case of an error, the application execution is not interrupted. You can refer to the application log file for debugging purposes.

Increment the application version, run the application and ensure that the class name changed and data is available.

You can check that the class' table name was modified during the database update. If your database server is Microsoft SQL Server, run Microsoft SQL Management Studio and navigate to the modified table in the Object Explorer.

![HowToHandleDbChanges8_1](~/images/howtohandledbchanges8_1116584.png)

If you use another database server, use the appropriate database tool to check if the table name was actually modified.

## Rename the Persistent Class Participant in Many-to-Many Relationship
Lets assume you have the Department and Position classes and there is a Department-Position many-to-many relationship. It is required to rename the **Department** to **Division**.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions ]
public class Department : BaseObject {
    // ...
    [Association("Departments-Positions")]
    public XPCollection<Position> Positions {
        get { return GetCollection<Position>(nameof(Positions)); }
    }
    // ...
}
[DefaultClassOptions]
public class Position : BaseObject {
    // ...
    [Association("Departments-Positions")]
    public XPCollection<Department> Departments {
        get { return GetCollection<Department>(nameof(Departments)); }
    }
    // ...
}
```
***
All the steps described in the [Rename a Persistent Class](#rename-the-persistent-class) section are required in this case. But, there are two additional steps.

* Rename the **Position.Departments** property to **Divisions** and modify the property name used in this property's getter. Change the "Departments-Positions" association name to "Divisions-Positions".
* Modifying the **PositionPositions_DepartmentDepartments** database table while storing the relationship information is required - rename the Departments column and the table itself.
	
	![HowToHandleDbChanges12](~/images/howtohandledbchanges12116586.png)
	
	To perform the renaming, add the following code to the **UpdateDatabaseBeforeUpdateSchema** method.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	if (TableExists("PositionPositions_DepartmentDepartments")) {
	    RenameColumn("PositionPositions_DepartmentDepartments", "Departments", "Divisions");
	    RenameTable("PositionPositions_DepartmentDepartments", "PositionPositions_DivisionDivisions");
	}
	```
	***

## Rename the Persistent Class Used as the Data Type in Analysis
If the Analysis business class is used in your application, it may be required to modify the Analysis table in end-user databases. This is necessary because end-users can have Analysis objects with **DataType** properties pointing to a renamed class. 
So, after performing the steps described in the [Rename a Persistent Class](#rename-the-persistent-class) section, add the following code to the **UpdateDatabaseBeforeUpdateSchema** method.

# [C#](#tab/tabid-csharp)

```csharp
ExecuteNonQueryCommand(
    "update Analysis set ObjectTypeName = 'MySolution.Module.Division' " + 
    "where ObjectTypeName = 'MySolution.Module.Department'", true);
```
***

## Rename a Persistent Class Used as the Data Type in Reports
If the [Reports V2 Module](xref:113591) is added to your application, it is required to modify the report's data. This is necessary because end-users may have reports with the [IReportDataV2.DataType](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2.DataType) property pointing to a renamed class. So, after performing the steps described in the [Rename a Persistent Class](#rename-the-persistent-class) section, add the following code to the **UpdateDatabaseBeforeUpdateSchema** method.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.ReportsV2;
//...
ReportDataProvider.MassUpdateDataType<ReportDataV2>(
    ObjectSpace, "MySolution.Module.Department", typeof(Division));
```
***

In the code above, the [ReportDataProvider.MassUpdateDataType\<T>](xref:DevExpress.ExpressApp.ReportsV2.ReportDataProvider.MassUpdateDataType*) method is used instead of **ExecuteNonQueryCommand**.

## Remove the Persistent Class
If you remove the persistent class from the application code, it will not be visible in the application interface. But, the corresponding table will still exist in the application database. To remove the table, use the **DropTable** protected method exposed by the [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) class. This method removes the specified table.  The following snippet illustrates how to remove the **Division** table.

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModuleUpdater {
    // ...
    public override void UpdateDatabaseBeforeUpdateSchema() {
        base.UpdateDatabaseBeforeUpdateSchema();
        if (CurrentDBVersion < new Version("1.1.0.0")
            && CurrentDBVersion > new Version("0.0.0.0")) {
            DropTable("Division", true);
            DeleteObjectType("MySolution.Module.Division");
        }
    }
    // ...
```
***

The "1.1.0.0" string is the application version in which changes are introduced. So, the table will be removed only if the database version is less than "1.1.0.0". It is required to check if the database version is greater then "0.0.0.0" to make changes only when the database exists and is filled with data (the empty database version is "0.0.0.0", by default).

The SQL commands actually executed within this example are:

``drop table Division``

``delete from XPObjectType where TypeName = 'MySolution.Module.Division'``

The SQL commands text is written to the application [Log File](xref:112575) with the "ExecuteNonQueryCommand:" prefix, before being executed. If an error occurs when executing the **DropTable** or **DeleteObjectType** method, the exception text is also logged. However, application execution is not interrupted. You can refer to the application log file for debugging purposes. If it is required to throw an exception if an error occurs when deleting the table, set the second parameter of the **DropTable** method to **false**.

You can check that the table was removed during the database update. If your database server is Microsoft SQL Server, run Microsoft SQL Management Studio and navigate to the application database table list in the Object Explorer. If you use another database server, use the appropriate database tool to check if the table was actually removed.
