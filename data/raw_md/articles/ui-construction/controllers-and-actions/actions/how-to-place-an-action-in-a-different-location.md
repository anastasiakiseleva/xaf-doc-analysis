---
uid: "402145"
title: 'How to: Place an Action in a Different Location'
seealso:
- linkId: "112610"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_how-to-add-custom-buttons-actions-to-the-lookup-and-popup-windows
  altText: 'GitHub Example: XAF - Add Custom Buttons (Actions) to Lookup and Popup Windows'
---
# How to: Place an Action in a Different Location

This article explains how to move an [Action](xref:112622) to another [Action Container](xref:112610).

_Actions_ are toolbar items or other controls that execute associated code when a user interacts with them.

_Action Containers_ are controls that display one or more Actions. XAF maps Actions to Action Containers based on the [](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property values.

To change the location of an Action in the application's UI, move the Action from its current Action Container to another one.

> [!NOTE]
> For the purposes of this article, you can use the **MainDemo** application installed as a part of the XAF package. The default location of the application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\\Components\XAF_.

In the **MainDemo** application, the `ClearTaskAction` Action belongs to the `RecordEdit` Action Container. The image below shows the current location of `ClearTaskAction` in the UI:

ASP.NET Core Blazor

:   ![ASP.NET Core Blazor - Current location of ClearTaskAction, DevExpress](~/images/how-to-place-action-cleartasks-original-location.png)

Windows Forms

:   ![Windows Forms - Current location of ClearTaskAction, DevExpress](~/images/how-to-place-action-cleartasks-original-location-winforms.png)

The instructions below explain how to move `ClearTaskAction` to another location.

1. In the **Solution Explorer**, expand the `MainDemo.Module` project and double-click the _Model.DesignedDiffs.xafml_ file to open it in the [Model Editor](xref:112582).

2. Navigate to the **ActionDesign** | **ActionToContainerMapping** node and expand it. Child nodes of the **ActionToContainerMapping** node correspond to the Action Containers of your application.

3. Expand the **RecordEdit** node. Drag the **ClearTasksAction** child node to the **View** node.

   ![Rearrangement of Actions in Model Editor, DevExpress](~/images/how-to-place-action-rearrange-actions.gif)   

4. Save the changes and run the application. When you invoke the **Employee** Detail View, the `ClearTaskAction` Action appears in a different location:

   ASP.NET Core Blazor

   :   ![ASP.NET Core Blazor - New location of ClearTaskAction, DevExpress](~/images/how-to-place-action-cleartasks-target-location.png)

   Windows Forms

   :   ![windows Forms - New location of ClearTaskAction, DevExpress](~/images/how-to-place-action-cleartasks-target-location-winforms.png)

> [!TIP]
> To change the location of an Action in code, handle the [ActionControlsSiteController.CustomizeContainerActions](xref:DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomizeContainerActions) event.
