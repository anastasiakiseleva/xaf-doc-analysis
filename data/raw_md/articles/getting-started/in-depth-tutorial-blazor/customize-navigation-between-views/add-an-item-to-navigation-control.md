---
uid: "402131"
title: Add an Item to the Navigation Control
seealso:
  - linkId: DevExpress.Persistent.Base.DefaultClassOptionsAttribute
  - linkId: DevExpress.Persistent.Base.NavigationItemAttribute
---
# Add an Item to the Navigation Control

This lesson explains how to add the **Notes** item to the navigation control. When clicked, this Notes item is used to display a List View for the `Note` business class that you added in the previous lesson: [Add an Action that Displays a Pop-Up Window](xref:402158).

## Step-by-Step Instructions

1. Expand the _MySolution.Module_ project and double-click the _Model.DesignedDiffs.xafml_ file to invoke the [Model Editor](xref:112582).

   The Model Editor pane consists of two major elements: the node tree and the context-sensitive property grid. When you select a node or focus a property, the Model Editor displays its type and a short description at the bottom of the pane.

   ![|Model Editor pane|](~/images/tutorial-model-editor.png)

2. In the tree, navigate to the **NavigationItems** | **Items** | **Default** | **Items** node. The structure of the **NavigationItems** node and its child nodes corresponds to the structure of the navigation control. To add a child item to a navigation item, right-click the **Items** node and select **Add…** | **NavigationItem** in the context menu:

   ![|XAF ASP.NET Core Blazor add navigation item|](~/images/blazor_tutorial_uic_add_navigation_item.png)

3. Specify the following properties for the new item:
   
   * Set the **View** property to `Note_ListView`. This property specifies the type of View the application displays when you select the **Notes** item in the navigation control.
   * Set the **Caption** property to `Notes`. This property specifies the name of the navigation item in the application's UI.
   * Set the **Id** property to `Note`. This property specifies the unique node identifier.
	
   ![|Navigation item properties|](~/images/blazor_tutorial_add_navgation_item_properties.png)

   When you change the **View** property value, the value of the **ImageName** property also changes. XAF checks the name of the View and looks for the corresponding image in the standard image library. If such image exists, XAF assigns it to the navigation item. For additional information, refer to the following lesson of this tutorial: [](xref:404201).
	
4. Run the application. You can see the **Notes** navigation item in the navigation control. Select this item to see the List View of the `Note` entity class.

   ASP.NET Core Blazor
	
   :   ![|ASP.NET Core Blazor: add a navigation item|](~/images/blazor_tutorial_add_navigation_item_result.png)

   Windows Forms

   :   ![Windows Forms: add a navigation item](~/images/blazor_tutorial_add_navigation_item_result_winforms.png)

## Next Lesson

[Rename and Rearrange Navigation Items](xref:404199)