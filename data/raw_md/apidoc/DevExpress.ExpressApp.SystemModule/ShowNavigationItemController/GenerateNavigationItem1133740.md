---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.GenerateNavigationItem(DevExpress.ExpressApp.Model.IModelApplication,System.String,System.String,System.String,System.String,System.String)
name: GenerateNavigationItem(IModelApplication, String, String, String, String, String)
type: Method
summary: Creates an Application Model's NavigationItem node that defines an item of the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController)'s **ShowNavigationItem** Action.
syntax:
  content: public static IModelNavigationItem GenerateNavigationItem(IModelApplication modelApplication, string navigationItemGroupName, string navigationItemId, string navigationItemCaption, string viewId, string objectKey)
  parameters:
  - id: modelApplication
    type: DevExpress.ExpressApp.Model.IModelApplication
    description: An [](xref:DevExpress.ExpressApp.Model.IModelApplication) object represents the Application Model.
  - id: navigationItemGroupName
    type: System.String
    description: A string value representing the name of the **NavigationItem** node to which the new **NavigationItem** node will be added.
  - id: navigationItemId
    type: System.String
    description: A string value that represents an identifier of the new **NavigationItem** node.
  - id: navigationItemCaption
    type: System.String
    description: A string value that represents an identifier of the new **NavigationIte**m node.
  - id: viewId
    type: System.String
    description: A string representing the identifier of a [](xref:DevExpress.ExpressApp.View) that is displayed when the created Navigation Item is clicked in the navigation control.
  - id: objectKey
    type: System.String
    description: A string representing the key property value of the object which should be opened in the View specified by the _viewId_ parameter.
  return:
    type: DevExpress.ExpressApp.SystemModule.IModelNavigationItem
    description: An [](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem) object representing the Application Model's NavigationItem node.
seealso: []
---
Use this method to create a new **NavigationItem** node and add it to the Application Model.