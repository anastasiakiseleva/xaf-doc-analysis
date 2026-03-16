---
uid: DevExpress.ExpressApp.Dashboards.DashboardsModule.AddDashboardDataFromResources``1(DevExpress.ExpressApp.IObjectSpace,System.String,System.Reflection.Assembly,System.String)
name: AddDashboardDataFromResources<T>(IObjectSpace, String, Assembly, String)
type: Method
summary: Creates a dashboard data object from the specified XML [resource file](https://learn.microsoft.com/en-us/visualstudio/ide/managing-application-resources-dotnet) if there is no dashboard data with the specified _title_ parameter in the database.
syntax:
  content: |-
    public static T AddDashboardDataFromResources<T>(IObjectSpace objectSpace, string title, Assembly assembly, string embeddedResourceName)
        where T : IDashboardData
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object that specifies the [Object Space](xref:113707).
  - id: title
    type: System.String
    description: A string specifying the dashboard title.
  - id: assembly
    type: System.Reflection.Assembly
    description: An [](xref:System.Reflection.Assembly) specifying the assembly which contains the dashboard configuration as an embedded resource.
  - id: embeddedResourceName
    type: System.String
    description: A string specifying the embedded resource name which contains the dashboard configuration in XML format.
  typeParameters:
  - id: T
    description: ''
  return:
    type: '{T}'
    description: A dashboard data object.
seealso:
- linkId: DevExpress.ExpressApp.Dashboards.DashboardsModule.AddDashboardData``1(DevExpress.ExpressApp.IObjectSpace,System.String,System.String)
---
To recreate the predefined dashboard, first delete the Dashboard in the DashboardData ListView and then restart the application.
