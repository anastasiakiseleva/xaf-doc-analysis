---
uid: DevExpress.Persistent.Base.ReportsV2.DataSourceBase.CreateObjectSpace(System.Type,System.IServiceProvider)
name: CreateObjectSpace(Type, IServiceProvider)
type: Method
summary: Creates an [Object Space](xref:113707).
syntax:
  content: public static IObjectSpace CreateObjectSpace(Type dataType, IServiceProvider serviceProvider)
  parameters:
  - id: dataType
    type: System.Type
    description: A [](xref:System.Type) object that specifies the business object type for which the Object Space is retrieved.
  - id: serviceProvider
    type: System.IServiceProvider
    description: An [IServiceProvider](https://learn.microsoft.com/en-us/dotnet/api/system.iserviceprovider) object.
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object.
seealso: []
---
To access data in an XAF application, you do not need to use an ORM-specific context or query data from the database directly. Instead of these techniques, use an Object Space's methods (see [Data Manipulation and Business Logic](xref:113708)).

The `CreateObjectSpace` static method allows you to access an Object Space in [report scripts](xref:2593):

# [C#](#tab/tabid-csharp)

```csharp
private void report_BeforePrint(object sender, System.Drawing.Printing.PrintEventArgs e) {
    DevExpress.ExpressApp.IObjectSpace objectSpace = 
        DevExpress.Persistent.Base.ReportsV2.DataSourceBase.CreateObjectSpace(typeof(MyObject), (DevExpress.XtraReports.UI.XtraReport)sender);
}
```
***
