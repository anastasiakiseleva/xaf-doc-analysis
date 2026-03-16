---
uid: "402151"
title: ORM Layer Performance
owner: Alexey Kazakov
seealso:
  - linkType: HRef
    linkId: https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/21.1.3+/Benchmarks
    altText: '.NET App Security API Benchmark for EF Core and XPO'
  - linkType: HRef
    linkId: https://github.com/DevExpress/XPO/tree/master/Benchmarks
    altText: '.NET Core ORM Benchmark'
---
# ORM Layer Performance

This article explains how to fix the most frequent SQL-related performance issues caused by ORM data model design, business logic, or UI settings.

Use the diagnostic information from the [Database Performance](xref:402149) help topic to analyze the code of ORM persistent classes as described in this topic.

## ORM Best Practices

Follow the best practices for your ORM to achieve the best performance results.

- **XPO**: 
    - [](xref:403711) 
    - [XPO Worst Practices](https://supportcenter.devexpress.com/ticket/details/k18428/xpo-worst-practices)
- **EF Core**: 
    - [Efficient Querying](https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying)
    - [Efficient Updating](https://learn.microsoft.com/en-us/ef/core/performance/efficient-updating)
    - [Modeling for Performance](https://learn.microsoft.com/en-us/ef/core/performance/modeling-for-performance)
    - [Advanced Performance Topics](https://learn.microsoft.com/en-us/ef/core/performance/advanced-performance-topics)
    - [](xref:404429)
    - [](xref:404292)
    - [](xref:404862)

If your code already follows these best practices, review SQL queries with the highest call count and/or execution time. Note that if SQL query execution takes up the most time in end-user operations, then SQL query optimization must be performed.

> [!note]
> [!include[server-based-data-access-modes-part-1-template](~/templates/server-based-data-access-modes-part-1-template.md)]

## Troubleshooting

Check this list of the most frequent causes of performance issues and make sure you apply all recommendations from this list.

### A ListView loads data slowly if the corresponding database table contains more than 100K records (or more than 10K records with complex structure).

**Solution 1:** If you do not need to show all records simultaneously, [add a server-side filter to your ListView](xref:403238).

**Solution 2:** For Grid List Editors, set [List View Data Access Modes](xref:113683) to values other than `Client`. For Pivot Grid List Editors, see [Ways to improve Pivot Grid List Editor or PivotChart performance with large amounts of data](https://supportcenter.devexpress.com/ticket/details/t687056/ways-to-improve-pivot-grid-list-editor-or-pivotchart-performance-with-large-amounts-of). 

For more information, refer to the following video: [Data Access in DevExpress XAF & ORM-related Performance Considerations - Data Access Modes in ListView - DEMO](https://www.youtube.com/watch?v=RUyXX2pJcjM&t=442s).


### The main SELECT query takes a long time to execute, although not many rows are returned.

This may occur if each persistent object contains many fields with images, long text, references to complex persistent objects, etc.

**Solution 1:** For List Editors, set the ListView's [DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelListView.DataAccessMode) to `DataView`, `ServerView` or `InstantFeedbackView` to load only required properties (by default, all object properties are loaded except for collections). For reports, use [ViewDataSource](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource).

**Solution 2:** Enable [Delayed Loading](xref:2024) for BLOB and complex reference properties. Note that delayed properties should not be displayed in the ListView.

### XPO or EF Core sends additional queries to load associated (referenced) objects.

For _XPO_, this behavior is expected; it loads related object IDs in the main query, and then loads all of these objects in the second query by these IDs. In most cases, this behavior should not cause performance issues. If it does, there are two ways to address these issues:

**Solution 1:** Include referenced objects in the main SELECT query by applying the [ExplicitLoading](xref:DevExpress.Xpo.ExplicitLoadingAttribute) attribute to the corresponding properties.

**Solution 2:** If related objects are not used in list views, you can use [Delayed Loading](xref:2024) for them.

In most cases, all referenced objects of the same type are loaded through a single additional query for all records. If additional queries are performed for each record, see the next case.

For EF Core, review the following topics:
- [](xref:404429)
- [](xref:404862)

### XPO or EF Core executes a separate query or multiple queries for each record.

For more information, see:
- [What is the “N+1 selects problem” in ORM (Object-Relational Mapping)?](https://stackoverflow.com/questions/97197/what-is-the-n1-selects-problem-in-orm-object-relational-mapping) (StackOverFlow) 
- [Fixing an N+1 performance problem in XAF/XPO with entirely undocumented APIs](https://blog.delegate.at/2020/09/21/fixing-an-n1-performance-problem-in-xaf-xpo-with-totally-undocumented-apis.html)
- [Eager Loading of Reference (Foreign Key, Complex Type) Properties (EF Core)](xref:404429)
- [](xref:404862)

To resolve such issues, see what additional queries are executed and analyze your business class to understand what code causes this. Below are the most common cases.

- **Additional queries load a property of the current business class that is not loaded in the main SELECT query.**

    **Solution:** This property is likely delayed, and there is a ListView column that displays it. In this case, either do not use delayed loading for this property, or remove the ListView column (see [](xref:113679)). The same issue occurs if the delayed property is accessed in code while the view loads objects. Such code may be located in another property's getter or in the OnLoaded method.

- **Additional queries select data from other tables according to a PersistentAlias expression.**

    This may happen if the expression uses collection properties (such as `Orders.Sum(Amount)`) or join operands (such as `[<Task>][AssignedTo.Oid = ^.Oid].Single()`). The `EvaluateAlias` method evaluates a `PersistentAlias` attribute expression on the client side. If the expression contains a collection property, ORM loads the collection when the getter is called.

    **Solution 1:** For List Editors, set the ListView's DataAccessMode to DataView, ServerView, or InstantFeedbackView. For reports, use ViewDataSource. In this case, when ORM constructs the main SELECT query, it includes all queries that can run server side (PersistentAlias expressions). The application will not use any client-side code that loads data.

    **Solution 2:** Pre-fetch associated collections using the `Session.PreFetch` and `XPObjectSpace.SetPrefetchPropertyNames` methods. In this case, all associated objects will be loaded in a single query. You can find an example in the following ticket: [How do I prefetch related details data to increase performance for calculated fields](https://supportcenter.devexpress.com/ticket/details/q558707/how-do-i-prefetch-related-details-data-to-increase-performance-for-calculated-fields).

    **Solution 3:** Use the `Session.Evaluate` method instead of the `EvaluateAlias` method in getters of such properties. The `Session.Evaluate` method evaluates the specified expression on the database side and returns a single value. XPO still sends a separate query for each row, but these queries require less time and memory.

    **Solution 4:** Implement a calculated column in the database and map it to an XPO property using the [FetchOnly](xref:DevExpress.Xpo.FetchOnlyAttribute) attribute (v18.2+).


- **Additional queries are executed for an unknown reason.**

    **Solution:** To determine why an object of a certain type is loaded, set a breakpoint in its constructor. Run the app and open the corresponding ListView. When the debugger stops at the specified breakpoint, open the call stack window and review the methods that lead to object initialization. This may be the business logic from property getters or an `OnLoaded` method call.

    If your class loads objects in the `OnLoaded` method, try to move this logic to a calculated property getter. This calculated property should be hidden from the ListView. To show calculated values in the ListView, implement a `PersistentAlias` property and optimize it as described in the previous case.

### The applications frequently perform the same queries that return the same database records.

**Solution:** If these records are rarely changed, it makes sense to [enable caching at the Data Layer level](https://supportcenter.devexpress.com/ticket/details/k18356/how-to-use-xpo-data-layer-caching-in-xaf) to prevent repetitive requests.

### An XPO-based WinForms app repeatedly creates and closes database connections on performing asynchronous operations in Instant Feedback mode.

**Solution:** Make sure data store provider's [connection pooling](xref:DevExpress.Xpo.XpoDefault.GetConnectionPoolString*) is enabled in _Startup.cs_:

# [C#](#tab/tabid-csharp)

```csharp
builder.ObjectSpaceProviders
    .AddSecuredXpo((application, options) => {
        //...
        options.EnablePoolingInConnectionString = true;
    })
```

***
### Validation may take significant time when an object that must be saved exposes a large collection of aggregated objects.

**Solution:** Aggregated objects are integral to a master object and should be validated together. The [PersistenceValidationController](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController) loads the entire aggregated collection in such cases. Refer to the following article for more information and possible solutions: [Validation performance - PersistenceValidationController and the Aggregated attribute trigger the selection of child records one at a time when the master object is saved](https://supportcenter.devexpress.com/ticket/details/t241762/validation-performance-persistencevalidationcontroller-and-the-aggregated-attribute).

### Your persistent classes have many reference and collection properties (or the entire object graph is complex), and thus the profile confirms excessive JOIN/additional queries.

Consider if you can [denormalize](https://en.wikipedia.org/wiki/Denormalization) your database table or map your persistent class to a database view with only required columns from your database table. In the UI, you may lose the capability to navigate to certain reference sub-properties, but this may be unimportant for users (so the changes are justified).

- [How to: Map to Custom Tables (Views) and Columns](xref:2058)
- [How to: Map a Persistent Class to a Database View Which Has No Key Field](xref:113281)

---

This article lists only the most common performance issues. You can also encounter issues related to a certain database provider or legacy database, scenario-specific issues, and so on. We recommend that you find out how the query or the database table can be modified to improve performance, and then try to modify your persistent objects accordingly.


## Next Steps

If you still experience performance issues after you followed the advice in this topic, review the next article in our optimization guide: [Application Performance](xref:402150).
