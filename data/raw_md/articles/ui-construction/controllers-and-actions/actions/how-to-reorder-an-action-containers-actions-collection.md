---
uid: "112815"
title: "How to: Reorder an Action Container's Actions Collection"
seealso:
- linkId: "402157"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_how-to-add-custom-buttons-actions-to-the-lookup-and-popup-windows
  altText: 'GitHub Example: XAF - Add Custom Buttons (Actions) to Lookup and Popup Windows'
---
# How to: Reorder an Action Container's Actions Collection

In an XAF application UI, [Actions](xref:112622) are located within [Action Containers](xref:112610). You can use the [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property and the Application Model's **ActionDesign** | **ActionToContainerMapping** node to move the Action to another Action Container (see [](xref:402145)). This topic describes how to reorder Actions within a specific container.

Presume you have the **MyAction** Action implemented in the **MyController** [Controller](xref:112621). The [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property is set to **View** for this Action. This means that the Action is displayed within the **View** Action Container. This Container may also contain other Actions - custom Actions, and actions from referenced modules.  To reorder Actions of the **View** Action Container (or any other Action Container), invoke the [Model Editor](xref:112582) for the WinForms or ASP.NET Core Blazor application project. Locate the **ActionDesign** | **ActionToContainerMapping** | **View** node. The following image shows that there are three Actions in the **View** Action Container.

![PlaceActionToPosition_InitialSate](~/images/placeactiontoposition_initialsate115602.png)

To reorder these Actions, change the **Index** property for each Action. For instance, use the "0" value for **MyAction**, "1" - for **Refresh**, "2" - for **ExecuteReport**.

![PlaceActionToPosition_Index](~/images/placeactiontoposition_index115601.png)

If you run the application, you can ensure that the Actions order is changed as follows.

![PlaceActionToPosition_Runtime](~/images/placeactiontoposition_runtime115603.png)
> [!NOTE]
> * Actions from the **Unspecified** Action Container can be displayed by another container if you change the [IFrameTemplate.DefaultContainer](xref:DevExpress.ExpressApp.Templates.IFrameTemplate.DefaultContainer) value for the current [Template](xref:112609). These Actions are appended to the end of the collection. If you need to change their position within the Container, then first specify their Action Container explicitly.
> * In the application with the **TabbedMDI** UI type (see [](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy)), the main window's Actions collection is merged with the child window's Actions, which can influence the resulting Actions order.

> [!TIP]
> To change Action Containers order and location, [customize the Template](xref:112618). In WinForms applications, you can also use the [runtime customization capabilities](xref:117515).