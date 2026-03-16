---
uid: DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportStoreMode
name: ReportStoreMode
type: Property
summary: Specifies the format used to store reports in the [](xref:DevExpress.ExpressApp.ReportsV2.ReportsStorage).
syntax:
  content: public ReportStoreModes ReportStoreMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ReportsV2.ReportStoreModes
    description: A [](xref:DevExpress.ExpressApp.ReportsV2.ReportStoreModes) enumeration value that specifies the format used to store reports.
seealso: []
---
Supported formats are `DOM` and `XML`. Using the `XML` format instead of `DOM` can decrease the loading time of a complex report.

> [!IMPORTANT]
> * Ensure that you use the same `ReportStoreMode` value in all versions of your application that utilize the same database.
> * Reports previously created by users will fail to open after changing the `ReportStoreMode` value, with the error message similar to "_Data at the root level is invalid. Line 1, position 1_". To fix the error, use the module updater demonstrated in the [How to fix the 'Data at the root level is invalid. Line 1, position 1.' exception after setting the ReportsModuleV2.ReportStoreMode property to XML](https://supportcenter.devexpress.com/ticket/details/t308208/how-to-fix-the-data-at-the-root-level-is-invalid-line-1-position-1-exception-after) KB article.

The [Template Kit](xref:405447) sets the `ReportStoreMode` value to `XML` an all newly created XAF applications.