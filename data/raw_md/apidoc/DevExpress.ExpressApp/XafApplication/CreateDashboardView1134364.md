---
uid: DevExpress.ExpressApp.XafApplication.CreateDashboardView(DevExpress.ExpressApp.IObjectSpace,System.String,System.Boolean)
name: CreateDashboardView(IObjectSpace, String, Boolean)
type: Method
summary: Creates a [Dashboard View](xref:112611) using information from the [Application Model](xref:112580)'s **Views** | **DashboardView** node specified by the _dashboardViewID_ parameter.
syntax:
  content: public DashboardView CreateDashboardView(IObjectSpace objectSpace, string dashboardViewId, bool isRoot)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the Object Space which is used to work with the database. This object is assigned to the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property.
  - id: dashboardViewId
    type: System.String
    description: A string that represents an identifier of the [Application Model](xref:112580) node that serves as an information source for creating a new Dashboard View.
  - id: isRoot
    type: System.Boolean
    description: '**true**, if the created Dashboard View is independent and owns the Object Space passed using the _objectSpace_ parameter; **false**, if the created Detail View is nested to another root View that owns the Object Space. This value is assigned to the [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot) property.'
  return:
    type: DevExpress.ExpressApp.DashboardView
    description: The created [Dashboard View](xref:112611).
seealso: []
---
Use this method to create a Dashboard View and initialize its properties by the values passed as parameters.

> [!NOTE]
> Do not use another View's Object Space for the creation of a new root View in it. Instead, create a new Object Space via the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method for the new root View.