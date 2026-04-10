---
uid: "113011"
title: View Variants (Switch Document Layouts)
seealso:
  - linkId: DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController
  - linkType: HRef
    linkId: https://community.devexpress.com/blogs/xaf/archive/2011/07/04/best-practices-of-creating-reusable-xaf-modules-by-example-of-a-view-variants-module-extension.aspx
    altText: Best practices of creating reusable XAF modules by example of a View Variants module extension
  - linkType: HRef
    linkId: https://github.com/DevExpress-Examples/xaf-how-to-save-the-currently-opened-view-as-a-new-view-variant-at-runtime
    altText: XAF - How to save the currently opened View as a new View Variant at runtime
  - linkType: HRef
    linkId: https://github.com/DevExpress-Examples/xaf-save-and-share-custom-view-settings
    altText: XAF - How to Save and Share Custom View Settings
---
# View Variants (Switch Document Layouts)

The XAF allows [View](xref:112611) customization at design time, in code, and by end-users. You may wish to implement multiple customized variants of the same View, and allow an end-user to choose the desired View Variant at runtime. For instance, end-users may need to use different List View column sets and Detail View layouts in different scenarios. They may also need to use two List View modes: a single List View and a List View with a Detail View (see [IModelListView.MasterDetailMode](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailMode)). XAF offers built-in implementation of this feature in the [](xref:DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsModule), which is declared in the _DevExpress.ExpessApp.ViewVariantsModule.v<:xx.x:>.dll_ assembly. This topic teaches you to create multiple versions of the same View.

To apply the **View Variants** module capabilities, add this module to your application project.

> [!NOTE]
> * [!include[<@DevExpress.ExpressApp.ApplicationBuilder.ViewVariantsApplicationBuilderExtensions.AddViewVariants``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0},System.Action{DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsOptions})>,<ASP.NET Core Blazor/WinForms>](~/templates/ExtraModulesNote_ApplicationBuilder.md)]
> * [!include[ExtraModulesNote1](~/templates/extramodulesnote1111180.md)]
> * To add an extra module in code, add it to the [XafApplication.Modules](xref:DevExpress.ExpressApp.XafApplication.Modules) or [ModuleBase.RequiredModuleTypes](xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes) list (adding a reference to the module assembly is insufficient).

To see a demonstration of View Variants, you can run the **Feature Center** application that ships with XAF (the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ folder), and navigate to the **View Variants** item, or refer to the [Feature Center demo online](https://demos.devexpress.com/XAF/featurecenter).

## Overview
The **View Variants** module provides the [](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController) [View Controller](xref:112621). It contains the **ChangeVariant** [Action](xref:112622), which allows end-users to select a View Variant to be displayed within the current Window (Frame). This Action is of the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) type and has the **ChangeVariant** ID. Its items are specified by the [!include[Node_Views](~/templates/node_views112047.md)] | **Variants** node of the [Application Model](xref:112580). The action is visible if there are two or more **Variants** child nodes in the current View node.

### In a Windows Forms application:

![ViewChangeActionInWindow](~/images/viewchangeactioninwindow115369.png)

### In an ASP.NET Core Blazor application:

![Change View](~/images/view-variants-blazor.png)

To add View Variants, do the following:

* Define a new View for the required object type in the Application Model. To do this, add a new **ListView** or **DetailView** node to the **Views** node, and specify its **ModelClass** and **Id** properties. In the node's context menu, choose **Generate content** and specify the required settings (column set, layout, etc.). Repeat this step to add as many Views as required.
* Define a new View that will represent the varied List View or Detail View for the required object type. Give it a meaningful ID to distinguish it from other Views of this object type (for instance, add the "_Varied" suffix). This View node will store view variants. Right-click it and select **Add…** | **Variants**. The Variants child node will be added.
* Invoke the context menu for the Variants node and select the **Add ListView** menu item. Specify the newly added node's [IModelVariant.Caption](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelVariant.Caption) and [IModelView.Id](xref:DevExpress.ExpressApp.Model.IModelView.Id) properties. Specify the [IModelVariant.Id](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelVariant.Id) property by selecting View from the drop-down list. Note that the View will be present in this drop-down list if its [IModelObjectView.ModelClass](xref:DevExpress.ExpressApp.Model.IModelObjectView.ModelClass) property has the same value as the current View. Additionally, you can specify the [IModelNode.Index](xref:DevExpress.ExpressApp.Model.IModelNode.Index) property to set a custom sort order for variants. Repeat this step to add all newly created Views and the default View.
* Specify the [IModelVariants.Current](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelVariants.Current) property of the Variants node by selecting a variant ID from the drop-down list. This variant will be used by default.
* Set the required object's [IModelClass.DefaultListView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultListView) ([IModelClass.DefaultDetailView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultDetailView)) property to the **Id** of the varied View. Alternatively, you can change the **View** property of a specific **NavigationItem** node or **DetailView** of a specific **ListView** node, to specify the varied view instead of the default view.
* Make sure you have selected the correct Data Access Mode for the root View and for each variant View. See [IModelListView.DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelListView.DataAccessMode) for details.

The following image illustrates how the varied View and its View Variants are organized in the Application Model.

![Tutorial_EM_Lesson2_2_4](~/images/tutorial_em_lesson2_2_4116620.png)

The image below illustrates the **ChangeVariant** Action available in a WinForms application after following the steps above.

![Tutorial_EM_Lesson2_3](~/images/tutorial_em_lesson2_3115524.png)

A variant can be chosen from the drop-down list. Variants are sorted according to their [IModelNode.Index](xref:DevExpress.ExpressApp.Model.IModelNode.Index) property values. Additionally, you can set the **Current** property of the **Variants** node to specify the default variant. The previously selected variant ID is stored with user customizations (in the _Model.User.xafml_ file or in browser cookies).

## Display View Variants in Navigation
View Variants can be also added to the Navigation. Set the [IModelNavigationItemsVariantSettings.GenerateRelatedViewVariantsGroup](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelNavigationItemsVariantSettings.GenerateRelatedViewVariantsGroup) property to true in the Model Editor.

![Tutorial_EM_Lesson2_5](~/images/tutorial_em_lesson2_5117208.png)

The image below illustrates the result.

![Tutorial_EM_Lesson2_6](~/images/tutorial_em_lesson2_6117209.png)

## Customize the List of View Variants
You can create a custom [](xref:DevExpress.ExpressApp.ViewVariantsModule.IVariantsProvider) object that loads View Variants in a custom manner. Assign your VariantsProvider to the [ViewVariantsModule.VariantsProvider](xref:DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsModule.VariantsProvider) property to replace the default [](xref:DevExpress.ExpressApp.ViewVariantsModule.ModelVariantsProvider) that loads View Variants from the Application Model.
