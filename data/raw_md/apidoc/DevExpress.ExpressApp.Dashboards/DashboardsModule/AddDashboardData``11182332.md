---
uid: DevExpress.ExpressApp.Dashboards.DashboardsModule.AddDashboardData``1(DevExpress.ExpressApp.IObjectSpace,System.String,System.String)
name: AddDashboardData<T>(IObjectSpace, String, String)
type: Method
summary: Creates a dashboard data object from the specified XML string if there is no dashboard data with the specified _title_ parameter in the database.
syntax:
  content: |-
    public static T AddDashboardData<T>(IObjectSpace objectSpace, string title, string xml)
        where T : IDashboardData
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object that specifies the [Object Space](xref:113707).
  - id: title
    type: System.String
    description: A string specifying the dashboard title.
  - id: xml
    type: System.String
    description: A string specifying the dashboard configuration in XML format.
  typeParameters:
  - id: T
    description: ''
  return:
    type: '{T}'
    description: A dashboard data object.
seealso:
- linkId: DevExpress.ExpressApp.Dashboards.DashboardsModule.AddDashboardDataFromResources``1(DevExpress.ExpressApp.IObjectSpace,System.String,System.Reflection.Assembly,System.String)
---
To recreate the predefined dashboard, first delete the Dashboard in the DashboardData ListView and then restart the application.

An example of using this method is provided in the [Create a Predefined Dashboard and Add it to the Navigation](xref:117453) topic.