---
uid: DevExpress.Persistent.Base.ReportsV2.DataSourceBase.EnableAsyncLoading
name: EnableAsyncLoading
type: Property
summary: Specifies whether or not the asynchronous report data source loading is enabled.
syntax:
  content: public static bool EnableAsyncLoading { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the asynchronous report data source loading is enabled; otherwise, **false**.'
seealso: []
---
The data is loaded in reports in the separate thread by default. When data for a report is loaded simultaneously with data from an another thread and [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider) works in a non-thread-safe manner, the _"Reentrancy or cross thread operation detected"_ exception can occur. You can use the **XPObjectSpaceProvider** instance in a thread-safe manner passing **true** as the last argument of its constructor. If using of the thread-safe **XPObjectSpaceProvider** is not possible in your application, disable asynchronous data loading in the reports setting the **EnableAsyncLoading** property to **false**.