---
uid: DevExpress.ExpressApp.Dashboards.DashboardsModule.HideDirectDataSourceConnections
name: HideDirectDataSourceConnections
type: Property
summary: Specifies if the **Data Source Wizard** allows setting direct Database connections.
syntax:
  content: |-
    [DefaultValue(false)]
    public bool HideDirectDataSourceConnections { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`false`, if the Data Source Wizard allows setting direct Database connections; otherwise, `true`.'
seealso: []
---

In a WinForms application, if the `HideDirectDataSourceConnections` property is set to `true`, only the following Data Source Types are available in the [Data Source Wizard](xref:17652):

* **Microsoft Excel workbook / CSV file**
* **Data Extract**
* **XAF Object DataSource**

In the ASP.NET Core Blazor application, if the `HideDirectDataSourceConnections` property is set to `true`, the _"Create data source..."_ link is hidden from the **Add Data Source** dialog.

!["Create data source" link in the Blazor Dashboard Designer](~/images/HideDirectDataSourceConnections_Blazor.png)
