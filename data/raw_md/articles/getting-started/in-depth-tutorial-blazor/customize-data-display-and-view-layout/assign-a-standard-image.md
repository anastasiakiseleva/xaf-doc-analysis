---
uid: "404201"
title: Assign a Standard Image
owner: Anastasiya Kisialeva
---
# Assign a Standard Image

This lesson explains how to associate an entity class with a standard image from the _DevExpress.Images_ assembly. This image illustrates the entity class in the following sections of the UI:

* Navigation control
* Detail View
* List View

The instructions below describe how to assign images to the entity classes in the Model Editor.

## Step-by-Step Instructions

1. In the **MySolution.Module** project, open the _Model.DesignedDiffs.xafml_ file in the [Model Editor](xref:112582).

2. Navigate to the **BOModel** | **MySolution.Module.BusinessObjects** | **Employee** node. In the **Appearance** section of the node's properties, locate the **ImageName** property and set its value to `BO_Employee`. 

   > [!TIP]
   > Focus the **ImageName** property field and click an ellipsis button that appears to the right of the property value to invoke the **Image Picker** dialog and browse all available images.

   After you change this value, XAF automatically recalculates the values of the following properties:

   | Node | Property | Description |
   |--|-|-|
   | **BOModel** \| **MySolution.Module.BusinessObjects** \| **Employee** | **DefaultDetailViewImage** | Specifies the name of the image displayed in the default Detail View of the `Employee` class. |
   | **BOModel** \| **MySolution.Module.BusinessObjects** \| **Employee** | **DefaultListViewImage**   | Specifies the name of the image displayed in the default List View of the `Employee` class. |
   | **NavigationItems** \| **Items** \| **Default** \| **Items** \| **Employees** | **ImageName** | Specifies the name of the image displayed with the **Employees** item in the navigation control. | 

   ![Assign standard image in Model Editor](~/images/assign-standard-image-model-editor.gif)

3. Run the application to see the new image in the UI:

   ASP.NET Core Blazor:

   :   ![|ASP.NET Core Blazor Standard Image for Department|](~/images/tutorial-standard-image-blazor.png)

   Windows Forms:

   :   ![Windows Forms Standard Image for Department](~/images/tutorial-standard-image-winforms.png)

4. In the same manner, assign images to the following classes:

   | Class | Image name |
   |-------|------------|
   | `Department` | `BO_Department` |
   | `Position` | `BO_Position` |
   | `DemoTask` | `BO_Task` |
   | `Payment`  | `BO_Invoice` |

   After you apply the changes, the UI of your application should look as follows:

   ASP.NET Core Blazor:

   :   ![|ASP.NET Core Blazor Standard Images|](~/images/tutorial-standard-image-final-blazor.png)

   Windows Forms:

   :   ![Windows Forms Standard Images](~/images/tutorial-standard-image-winforms-final.png)

## Next Lesson

[](xref:403287)