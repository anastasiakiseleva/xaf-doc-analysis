---
uid: DevExpress.ExpressApp.ReportsV2.ReportServiceController.QueryRootReportComponentName
name: QueryRootReportComponentName
type: Event
summary: Occurs when the default name of a user-defined report is queried.
syntax:
  content: public static event EventHandler<QueryRootReportComponentNameEventArgs> QueryRootReportComponentName
seealso: []
---
Handle this static event to change the default name of user-defined reports. In the event handler, assign the new name to the **Name** parameter and set the **Handled** parameter to **true**. An example is provided in the [How to: Specify the Default Name for User-Defined Reports](xref:113607) topic.