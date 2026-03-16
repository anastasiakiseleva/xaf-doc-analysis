---
uid: DevExpress.ExpressApp.ReportsV2.Win.ReportsWindowsFormsModuleV2.CreateCustomReportDesignRepositoryItem
name: CreateCustomReportDesignRepositoryItem
type: Event
summary: Occurs when a [Repository Item](xref:114580) is created for the report parameter.
syntax:
  content: public static event EventHandler<CreateCustomReportDesignRepositoryItemEventArgs> CreateCustomReportDesignRepositoryItem
seealso: []
---
Handle this static event to specify a custom [](xref:DevExpress.XtraEditors.Repository.RepositoryItem) used to edit a parameter value when a report is being previewed. Pass your repository item via the handler's [CreateCustomReportDesignRepositoryItemEventArgs.RepositoryItem](xref:DevExpress.ExpressApp.ReportsV2.Win.CreateCustomReportDesignRepositoryItemEventArgs.RepositoryItem) parameter and set the **Handled** parameter to **true**. The specified control will be used for any report in the application. An example is provided in the [How to: Use a Custom Editor for an XtraReport Parameter](xref:113608) topic.