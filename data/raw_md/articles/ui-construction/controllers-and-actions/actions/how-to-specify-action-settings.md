---
uid: "402146"
title: 'How to: Modify Action Properties in the Model Editor'
seealso:
  - linkId: "112622"
  - linkId: "112701"
---
# How to: Modify Action Properties in the Model Editor

This article describes how to modify an Action's properties in the [Model Editor](xref:112582). This tool allows you to browse and edit an [Application Model](xref:112580) in Visual Studio.

An _Action_ is an abstract UI element. XAF generates the default UI based on the business classes you declare and the Application Model.

An _Application Model_ is metadata that defines the navigation structure, data display formats, and available commands. It has a neutral format that you can adapt to any target platform.


> [!NOTE]
> For the purposes of this article, you can use the **MainDemo** application installed as a part of the XAF package. The default location of the application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\\Components\XAF_.

The instructions below explain how to change the tooltip and the confirmation message of the **Clear Tasks** button in the [Main Toolbar](xref:400496).

1. In the **Solution Explorer**, expand the `MainDemo.Module` project and double-click the _Model.DesignedDiffs.xafml_ file to open it in the **Model Editor**.
   
   ![Application Model file, DevExpress](~/images/how-to-modify-action-properties-appmodel-file.png)

2. Navigate to the **ActionDesign** | **Actions** | **ClearTasksAction** node. In the right pane, find the **Misc** section of the properties.
   
   ![Misc properties section of the ClearTasksAction node, DevExpress](~/images/how-to-modify-action-properties-node-properties.png)

3. Set the `ConfirmationMessage` property to `This action will remove all tasks of the current Employee. Do you still want to proceed?`.
4. Set the `Tooltip` property to `Clear the task list of the current Employee`.
5. Save the changes and run the application. Open the **Employee** Detail View. Hover the mouse pointer over the **Clear Tasks** button to see the tooltip:

   ASP.NET Core Blazor

   :   ![ASP.NET Core Blazor - new tooltip, DevExpress](~/images/how-to-modify-action-properties-tooltip.png)

   Windows Forms

   :   ![Windows Forms - new tooltip, DevExpress](~/images/how-to-modify-action-properties-tooltip-winforms.png)

6. Click the **Clear Tasks** button to see the confirmation message:

   ASP.NET Core Blazor

   :   ![ASP.NET Core Blazor - new confirmation message, DevExpress](~/images/how-to-modify-action-properties-confirmessage.png)

   Windows Forms

   :   ![Windows Forms - new confirmation message, DevExpress](~/images/how-to-modify-action-properties-confirmessage-winforms.png)

> [!NOTE]
> You can also modify Action properties in code. Refer to the following topics for details:
>
> [](xref:402157)
> :   Describes how to implement a custom Action.
> [](xref:112676)
> :   Explains how to customize a built-in Action or a third-party module Action.
