---
uid: "404353"
title: Runtime Layout Customization in ASP.NET Core Blazor Applications
seealso:
  - linkId: "112817"
  - linkId: "404428"
  - linkType: HRef
    linkId: https://supportcenter.devexpress.com/ticket/details/e372/xaf-how-to-access-a-tab-control-in-a-detail-view-layout
    altText: How to access a tab control in a Detail View layout

---
# Runtime Layout Customization in ASP.NET Core Blazor Applications

XAF ASP.NET Core Blazor applications support View Item layout customization in a Detail View at runtime.

You can customize the layout in a simple Detail View and [Split Layout](xref:404203).

## Enable Layout Customization

This functionality is available by default.

You can customize the Detail View. To activate customization mode, right-click the empty area of the Detail View you wish to edit and select **Customize Layout** in the invoked context menu.

![|Customize Layout in a Detail View of an XAF ASP.NET Core Blazor Application, DevExpress|](~/images/xaf-blazor-detail-view-customization-mode-activation-devexpress.png)

The invoked _Customization Form_ contains a structured view of all View Items available in the Detail View and a list of View Items hidden in the Detail View.

![|Customization Form in a Detail View of an XAF ASP.NET Core Blazor Application, DevExpress|](~/images/xaf-blazor-detail-view-customization-form-devexpress.png)

To deactivate customization mode, close the **Customization Form** or right-click an empty area and select **Hide Customization Form** from the context menu.

## Disable Layout Customization

To disable runtime layout customization in a specific Detail View: open the [Model Editor](xref:112830), navigate to the **Views** | **\<Namespace\>** | **\<Class\>_DetailView** node, and set the @DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled property value to `false`.

To disable runtime layout customization in all Views, open the Model Editor, navigate to the **Options** node, and set the `CustomizationEnabled` property to `false`.

## Add Reference Properties to a Detail View

![ASP.NET Core Blazor: Hidden Items list in the Customization form, DevExpress](~/images/xaf-blazor-hidden-items-customization-devexpress.png)

Click the **Customize** button at the bottom of the **Hidden Items** list in the **Customization** window to invoke the **Object Model** dialog window. Check the items that you want to add to the **Hidden Items** list.

[!include[disableobjectmodelcontroller](~/templates/disableobjectmodelcontroller.md)]

> [!NOTE]
> If you have an extensive and complicated data model, the structure in the **Object Model** dialog window may be confusing. To see the path to a reference property, hover your mouse over the property in the **Object Model** dialog window. This may help you distinguish between similar properties.

[!include[customizemodelobjectdialog](~/templates/customizemodelobjectdialog.md)]

## Persist Layout Customization for Individual Users

A user can customize a Detail View's layout according to their needs. XAF stores the changes in the [user differences](xref:112580#application-model-layers) layer of the Application Model independently for each user. The next time a user invokes a customized View, XAF applies the most recent changes.

XAF supports this behavior if you used the [Template Kit](xref:405447) and selected **Standard (requests login and password)** in the **Security Options** section. For more information on how to enable this behavior in an existing application, refer to the following topic: [Store Application Model Differences in the Database](xref:113698).

The following article describes how users can share changes made during runtime layout customization: [](xref:113704).

## Supported Scenarios

### Change a View Item's Position

Drag a View Item and drop it at the required position. A blue line indicates where you can place the View Item.

![Change a View Item's Position in Customization Mode, DevExpress](~/images/xaf-blazor-detail-view-customization-change-item-position-devexpress.gif)

> [!NOTE]
> If an item group becomes empty as a result of this action, it disappears from the layout.

### Resize a View Item

Drag the vertical splitter between adjacent View Items.

![Resize an Item in Customization Mode, DevExpress](~/images/xaf-blazor-detail-view-customization-resize-item-devexpress.gif)

> [!NOTE]
> When you release the splitter, it sticks to the nearest 1/12th of the container width because of Blazor's [Form Layout Structure](xref:DevExpress.Blazor.DxFormLayout#layout-structure). You can use nested [groups](#create-a-group) with hidden captions to resize View Items with more precision.

### Hide a View Item

You can use either of the following options:

* Right-click an item and select the **Hide Item** option in the [context menu](xref:2177).

  ![Context Menu Option to Hide an Item in Customization Mode, DevExpress](~/images/xaf-blazor-detail-view-customization-hide-item-context-devexpress.gif)

* Drag an item to the **Hidden Items** list in the **Customization Form**.

  ![Drag-and-Drop to Hide an Item in Customization Mode, DevExpress](~/images/xaf-blazor-detail-view-customization-hide-item-dragndrop-devexpress.gif)

> [!NOTE]
> If you hide an entire group, all its View Items become hidden and the group itself disappears from the layout.

### Display a Hidden View Item

Drag a View Item from the **Customization Form** and drop it at the required position.

![Drag-and-Drop to Display a Hidden Item in Customization Mode, DevExpress](~/images/xaf-blazor-detail-view-customization-display-item-dragndrop-devexpress.gif)

### Create a Group

Right-click a View Item you want to add to a group and select the **Group** option in the [context menu](xref:2177).

![Create a Group in Customization Mode, DevExpress](~/images/xaf-blazor-detail-view-customization-create-group-devexpress.gif)

Use the context menu to ungroup View Items.

### Create a Tabbed Group

Right-click an item or a group's caption and select the **Create Tabbed Group** option in the [context menu](xref:2177).

![Create a Tabbed Group in Customization Mode, DevExpress](~/images/xaf-blazor-detail-view-customization-create-tabbed-group-devexpress.gif)

### Convert a Group to a Tab

Click a group, then right-click a tabbed group's header and select the **Convert Selected Group to Tab** option in the [context menu](xref:2177).

![Convert a Group To a Tab in Customization Mode, DevExpress](~/images/xaf-blazor-detail-view-customization-convert-group-to-tab-devexpress.gif)

## Reset View Item Layout

If you need to revert your changes, right-click an empty area in the Detail View at runtime and select **Reset Layout** in the invoked context menu.

![|Reset Layout Changes in a Detail View of an XAF ASP.NET Core Blazor Application, DevExpress|](~/images/xaf-blazor-detail-view-customization-reset-changes-devexpress.png)

## Limitations of Runtime Layout Customization

XAF does not support runtime layout customization in the following elements:

* [Pop-up Window](xref:403450#popup-window-template-popupwindowtemplate)
* [Dashboard View](xref:DevExpress.ExpressApp.DashboardView)
* [Dashboard View Item](xref:DevExpress.ExpressApp.Editors.DashboardViewItem)
* [Detail Property Editor](xref:113572#detailpropertyeditor)
* [Split Layout](xref:404203) for [Collection Properties](xref:113568)

It is also not available on smartphones or mobile devices with small displays.
