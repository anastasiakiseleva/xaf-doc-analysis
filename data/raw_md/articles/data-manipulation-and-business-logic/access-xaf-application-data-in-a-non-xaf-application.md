---
uid: "113709"
seealso:
- linkId: "114515"
title: Access XAF Application Data in a non-XAF Application
---
# Access XAF Application Data in a non-XAF Application

In certain scenarios, you may need to create an auxiliary application for database maintenance and use [Object Space](xref:113707) to query your primary XAF application data. This topic describes how you can create and use Object Space in a regular non-XAF application.

> [!IMPORTANT]
> We do not recommend using the approach from this topic in XAF applications. Instead, access an Object Space with context-dependent options. For more information, refer to the following topic: [](xref:113707).

In a non-XAF application, there is no `XafApplication` object with which to create an Object Space. You can instantiate the **Object Space Provider** manually and then call the provider's `CreateObjectSpace` method to create an Object Space.

{|
|-
! ORM
! Object Space Provider
|-

| XPO
| @DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider / @DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider
|-

| Entity Framework Core
| @DevExpress.ExpressApp.EFCore.EFCoreObjectSpaceProvider`1 / @DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1
|}

> [!Note]
> If you want to use the Security System in your non-XAF application, refer to the following help topic: [Use the Security (Access Control & Authentication) API in Non-XAF Applications - Free Offer](xref:113558).

## XPO Example

In XPO-based applications, the [Types Info Subsystem](xref:113669) should be initialized. The following example demonstrates how to access **MainDemo** application data (typically installed to _[!include[PathToMainDemo](~/templates/path-to-main-demo-ef-core.md)]_) and write the list of Departments to the standard output stream:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Xpo;
using DevExpress.ExpressApp;
using MainDemo.Module.BusinessObjects;
// ...
class Program {
    static void Main(string[] args) {
        XpoTypesInfoHelper.GetXpoTypeInfoSource();
        XafTypesInfo.Instance.RegisterEntity(typeof(Department));
        XPObjectSpaceProvider osProvider = new XPObjectSpaceProvider(
        @"integrated security=SSPI;pooling=false;data source=(localdb)\MSSQLLocalDB;initial catalog=MainDemo_", null);
        IObjectSpace objectSpace = osProvider.CreateObjectSpace();
        foreach (Department department in objectSpace.GetObjects<Department>()) {
            Console.WriteLine(department.Title + "\t" + department.Office);
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports Microsoft.VisualBasic
Imports DevExpress.ExpressApp.Xpo
Imports DevExpress.ExpressApp
Imports MainDemo.Module.BusinessObjects
' ...
Friend Class Program
    Shared Sub Main(ByVal args() As String)
        XpoTypesInfoHelper.GetXpoTypeInfoSource()
        XafTypesInfo.Instance.RegisterEntity(GetType(Department))
        Dim osProvider As New XPObjectSpaceProvider("integrated security=SSPI;pooling=false;data source=(localdb)\v11.0;initial catalog=MainDemo_", Nothing)
        Dim objectSpace As IObjectSpace = osProvider.CreateObjectSpace()
        For Each department As Department In objectSpace.GetObjects(Of Department)()
            Console.WriteLine(department.Title & vbTab & department.Office)
        Next department
    End Sub
End Class
```

***

## Entity Framework Core Example

Use the following code snippet to access **EFCore** console or WinForms application data, and write the list of Departments to the standard output stream.

# [C#](#tab/tabid-csharp1)

```csharp
var objectSpaceProvider = new EFCoreObjectSpaceProvider<ApplicationDbContext>(
     (builder, _) => builder
        .UseConnectionString("Data Source=(localdb)\\MSSQLLocalDB;Initial Catalog=EFCoreTestDB;Integrated Security=True;MultipleActiveResultSets=True")
  );
XafTypesInfo.Instance.RegisterEntity(typeof(Department));
IObjectSpace objectSpace = objectSpaceProvider.CreateObjectSpace();
foreach (Department department in objectSpace.GetObjects<Department>()) {
    Console.WriteLine(department.Title + "\t" + department.Office);
}
```
***

The following example demonstrates how you can access XAF data in non-XAF applications using the XAF Security System: [Role-based Access Control, Permission Management, and OData / Web / REST API Services for Entity Framework and XPO ORM](https://github.com/DevExpress-Examples/XAF_Security_E4908).

## Note

To populate the database with initial data, use the `DatabaseUpdater.Update` method as follows: 

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Updating;
// ...
DatabaseUpdater databaseUpdater = new DatabaseUpdater(
    osProvider, new ModuleBase[0], "", osProvider.ModuleInfoType);
databaseUpdater.Update();
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp.Updating
' ...
Dim databaseUpdater As New DatabaseUpdater( _
osProvider, New ModuleBase(){}, "", osProvider.ModuleInfoType)
databaseUpdater.Update()
```

***
