---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.GenerateNavigationItem(DevExpress.ExpressApp.Model.IModelApplication,DevExpress.ExpressApp.ViewShortcut,System.String)
name: GenerateNavigationItem(IModelApplication, ViewShortcut, String)
type: Method
summary: Creates an [Application Model](xref:112580)'s **NavigationItem** node that defines an item of the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController)'s **Navigation** Action.
syntax:
  content: public static IModelNavigationItem GenerateNavigationItem(IModelApplication modelApplication, ViewShortcut viewShortcut, string groupName)
  parameters:
  - id: modelApplication
    type: DevExpress.ExpressApp.Model.IModelApplication
    description: An [](xref:DevExpress.ExpressApp.Model.IModelApplication) object representing the Application Model.
  - id: viewShortcut
    type: DevExpress.ExpressApp.ViewShortcut
    description: A [](xref:DevExpress.ExpressApp.ViewShortcut) object that presents key information for creating a new **NavigationItem** node.
  - id: groupName
    type: System.String
    description: A string value representing the name of the **NavigationItem** node to which the new **NavigationItem** node will be added.
  return:
    type: DevExpress.ExpressApp.SystemModule.IModelNavigationItem
    description: An [](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem) object representing the Application Model's NavigationItem node.
seealso: []
---
Use this method to create a new **NavigationItem** node and add it to the Application Model.

If you need to specify a particular value for the new **NavigationItem** node's **Id** and **Caption**, use another override of this method.