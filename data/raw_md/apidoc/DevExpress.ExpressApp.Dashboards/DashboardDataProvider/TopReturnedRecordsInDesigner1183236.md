---
uid: DevExpress.ExpressApp.Dashboards.DashboardDataProvider.TopReturnedRecordsInDesigner
name: TopReturnedRecordsInDesigner
type: Property
summary: Specifies the maximum number of records to be retrieved from a data store in the Dashboard Designer.
syntax:
  content: public int TopReturnedRecordsInDesigner { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value that specifies the maximum number of records to be retrieved from a data store.
seealso: []
---
To change this property value, navigate to the _MySolution\Module_ project and add the following code to the modules's constructor declared in the _MySolutionModule.cs_ file.

# [C#](#tab/tabid-csharp)

```csharp
DashboardsModule.DataProvider.TopReturnedRecordsInDesigner = 100;
```
***