---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.GenerateNavigationItem(DevExpress.ExpressApp.Model.IModelApplication,DevExpress.ExpressApp.ViewShortcut,System.String,System.String,System.String)
name: GenerateNavigationItem(IModelApplication, ViewShortcut, String, String, String)
type: Method
summary: Creates an [Application Model](xref:112580)'s **NavigationItem** node that defines an item of the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController)'s **ShowNavigationItem** Action.
syntax:
  content: public static IModelNavigationItem GenerateNavigationItem(IModelApplication modelApplication, ViewShortcut viewShortcut, string groupName, string navigationItemId, string caption)
  parameters:
  - id: modelApplication
    type: DevExpress.ExpressApp.Model.IModelApplication
    description: An [](xref:DevExpress.ExpressApp.Model.IModelApplication) object represents the Application Model.
  - id: viewShortcut
    type: DevExpress.ExpressApp.ViewShortcut
    description: A [](xref:DevExpress.ExpressApp.ViewShortcut) object that presents key information for creating a new **NavigationItem** node.
  - id: groupName
    type: System.String
    description: A string value representing the name of the **NavigationItem** node to which the new **NavigationItem** node will be added.
  - id: navigationItemId
    type: System.String
    description: A string value that represents an identifier of the new **NavigationItem** node.
  - id: caption
    type: System.String
    description: A string value that represents an identifier of the new **NavigationItem** node.
  return:
    type: DevExpress.ExpressApp.SystemModule.IModelNavigationItem
    description: An [](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem) object representing the Application Model's NavigationItem node.
seealso: []
---
Use this method to create a new **NavigationItem** node and add it to the Application Model.