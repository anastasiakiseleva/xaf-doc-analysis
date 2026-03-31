---
uid: "113198"
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController
- linkId: "402131"
- linkId: "404199"
- linkId: "112617"
- linkId: "116417"
- linkId: "116416"
- linkId: "112920"
- linkId: "113200"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF-How-to-show-the-number-of-list-view-items-in-the-navigation-control
  altText: How to show the number of List View items in the Navigation Control
title: Navigation System
---
# Navigation System

This topic introduces the concept of the navigation system and describes its basic features. This post will cover the building blocks the navigation system includes, as well as how it operates on the inside. This document will go over how to define the navigation structure in your applications at design-time and to customize it in code. You will learn to change the navigation control style and to customize the navigation control. This topic will also introduce the concept of context navigation. A sample implementation of context navigation is however, out of the scope of this document and is described in the [How to: Implement Custom Context Navigation](xref:113200) topic.

[!include[<navigation system capabilities>](~/templates/main-demo-tip.md)]

## Navigation System Basics
An XAF application's UI consists of [Views](xref:112611). Views are abstract entities used for data representation. XAF has two basic types of Views - the Detail Views that display a single object and its properties, and List Views that display object collections. A typical XAF application includes multiple Views for viewing and editing different object types. The navigation system allows users to switch between these Views as needed. The navigation control in a UI lists all available Views and allows users to activate a View.

The main parts of the navigation system are the navigation [Action](xref:112622), navigation [Action Containers](xref:112610), [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController), and the navigation structure.

1. The navigation Action, navigation Action Containers, and `ShowNavigationItemController`. Each built-in XAF [Template](xref:112609) that corresponds to the main [Window](xref:112608) contains the navigation Action Container. This Action Container is used to host the Navigation Action, matched by a UI element of the navigation control.
	
	![NavigationControlStructure](~/images/navigationcontrolstructure116358.png)
	
	The `ShowNavigationItemController` populates the navigation Action Container with navigation Actions. `ShowNavigationItemController` reads the navigation structure and the navigation control style settings from the [Application Model](xref:112580) and customizes the navigation control accordingly. This Controller also synchronizes the selected item in the navigation control with the active View.
2. The navigation structure reflects the relationship between different Views. The Application Model's [](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems) node defines the navigation structure. The `IModelRootNavigationItems` node consists of [](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem) nodes. Each of the `IModelNavigationItem` nodes can have child nodes. 
	
	![NavigationStructure](~/images/navigationstructure116357.png)
	
	If a **NavigationItem** node has the [IModelNavigationItem.View](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem.View) property set, the corresponding item in the navigation control corresponds to a View. Selecting such an item activates the View. If the `View` property is not set, the corresponding item in the navigation control serves as a group that stores other items.

## Define the Navigation Structure

You can define and customize the navigation structure at design time and in code.

1. The [Model Editor](xref:112582) is meant for design-time customization of the navigation structure. Invoke the Model Editor, navigate to the **NavigationItem** node and customize it as required. This technique is detailed in the following tutorial: [Add an Item to the Navigation Control](xref:402131).
2. In code, you can do one of the following to define and customize the navigation structure:
	
	Apply the [](xref:DevExpress.Persistent.Base.NavigationItemAttribute) or [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) to the required business classes. The `NavigationItem` attribute adds a navigation item to the navigation control. The most frequently used constructor accepts one string parameter that specifies a first-level child node of the [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node. The constructor adds a **NavigationItem** node that corresponds to the List View of the business class to the specified node. The `DefaultClassOptions` attribute produces the same effect as the `NavigationItemAttribute` but adds certain extra attributes. Refer to the [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) class description for details.
	
	Customize the Application Model's [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node directly, in a custom Controller, for instance. This technique is described in the following help topic: [Access the Application Model in Code](xref:112810).

> [!NOTE]
> In Windows Forms applications with the Navigation Bar and Accordion style, you cannot use a group to navigate to a View, even if the View property is specified because groups serve only as containers for other navigation items.

## Control Styles in an ASP.NET Core Blazor Application

The following section illustrates the appearance of the navigation control in an ASP.NET Core Blazor application with different style settings.

### Accordion

![Navigation Control - Accordion Blazor](~/images/NavigationControlAccordionBlazor.png)

To apply this style to your Blazor application, set the [IModelRootNavigationItems.NavigationStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property to `Accordion`.

This is the default style used in XAF Blazor applications.

### Tree List

![Navigation Control - TreeList Blazor](~/images/NavigationControlTreeListBlazor.png)

To apply this style to your Blazor application, set the [IModelRootNavigationItems.NavigationStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property to `TreeList`.

### Show Images

Default navigation items display icons. To hide icons, set the [IModelRootNavigationItems.ShowImages](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.ShowImages) property to `False`.

![Navigation Accordion Without Icons](~/images/NavigationControlAccordionBlazorNoIcons.png)

## Control Styles in a WinForms Application

The following section illustrates the appearance of the navigation control in a WinForms application with different style settings.

### Accordion

![NavigationControlAccordionWin](~/images/NavigationControlAccordionWin.png)

To apply this style to your WinForms application, set the [IModelRootNavigationItems.NavigationStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property to `Accordion`. 
	
This is a default style for new XAF WinForms applications. 
	
All nodes except nodes of the last nesting level correspond to the accordion's group elements.

### Navigation Bar with Large Icons
	
![NavigationControlNavBarWin](~/images/navigationcontrolnavbarwin116360.png)
	
To apply this style to your WinForms application, do the following:
	
* Set the [IModelRootNavigationItems.NavigationStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property to `NavBar`.
* Set the [IModelRootNavigationItems.DefaultChildItemsDisplayStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.DefaultChildItemsDisplayStyle) property to `Large Icons`.
	
First-level child nodes are displayed in the navigation pane as navigation groups, and second-level child nodes are displayed as a set of icons.

### Navigation Bar with List
	
![NavigationControlStructure](~/images/navigationcontrolstructure116358.png)
	
To apply this style to your WinForms application, do the following:
	
* Set the [IModelRootNavigationItems.NavigationStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property to `NavBar`.
* Set the [IModelRootNavigationItems.DefaultChildItemsDisplayStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.DefaultChildItemsDisplayStyle) property to `List`.
	
First-level child nodes are displayed in the navigation pane as navigation groups. The content of each group is displayed as a TreeList.

### Tree List
	
![NavigationControlTreeListWin](~/images/navigationcontroltreelistwin116359.png)
	
To apply this style to your WinForms application, set the [IModelRootNavigationItems.NavigationStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property to `TreeList`.
	
All nodes are displayed as a tree list.

### Navigation Bar with Outlook Style
	
![NavigationSystem_NavBar_OutlookSimple](~/images/navigationsystem_navbar_outlooksimple123263.png)
	
To apply this style to your WinForms application, do the following:
	
* Set the [IModelRootNavigationItems.NavigationStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property to `NavBar`.
* Set the [IModelRootGroupsStyle.RootGroupsStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelRootGroupsStyle.RootGroupsStyle) property to `OutlookSimple` or `OutlookAnimated`.
* Set the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property to `Ribbon`.
* Set the [IModelOptionsWin.UIType](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.UIType) property to `SingleWindowSDI` or `MultipleWindowSDI`.

XAF displays each root navigation group as a [](xref:DevExpress.XtraBars.Navigation.NavigationBarItem) in the [Office Navigation Bar](xref:114558). When the [IModelChoiceActionItemChildItemsDisplayStyle.ChildItemsDisplayStyle](xref:DevExpress.ExpressApp.Model.IModelChoiceActionItemChildItemsDisplayStyle.ChildItemsDisplayStyle) property is set to `List` for the current group and this group has second-level child nodes, XAF displays the group content as a `TreeList`. When the `ChildItemsDisplayStyle` property is set to `LargeIcons` for the current group, XAF displays the group content as `NavBarItems`. In this case, only the first-level nodes are displayed.

> [!Note]
> If you need to customize the navigation control's appearance further, you can do it in code. You can implement a custom Controller and customize the control as required. The following help topic contains an a navigation control customization example: [How to: Access Navigation Control](xref:112617).

## Keyboard Shortcuts in WinForms Applications

When you use the [Multiple Document Interface](xref:404211) in the application, hold down the Shift key and click a navigation item to invoke a new View in a separate window instead of a new tab.

You can use arrow keys to navigate a tree list control. Click a tree list region that is not occupied by navigation items to enter keyboard navigation mode. Use the up arrow and down arrow keys to navigate between items. To expand a group item, press ctrl+right arrow. To collapse a group item, press ctrl+left arrow.

## Context Navigation

The navigation system supports context navigation. A module can track the item generation process in the navigation control. The module can add additional child navigation items to a created navigation item that meets specific criteria. The following built-in modules implement context navigation: [Reports V2](xref:113591), and [View Variants](xref:113011).

Context navigation is disabled for these modules. Use the following properties of the [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node to enable this feature:

* [IModelNavigationItemsForReports.GenerateRelatedReportsGroup](xref:DevExpress.ExpressApp.ReportsV2.IModelNavigationItemsForReports.GenerateRelatedReportsGroup)
* [IModelNavigationItemsVariantSettings.GenerateRelatedViewVariantsGroup](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelNavigationItemsVariantSettings.GenerateRelatedViewVariantsGroup)

Use the following properties of the [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node to customize context navigation group captions:

* [IModelNavigationItemsForReports.RelatedReportsGroupCaption](xref:DevExpress.ExpressApp.ReportsV2.IModelNavigationItemsForReports.RelatedReportsGroupCaption)
* [IModelNavigationItemsVariantSettings.RelatedViewVariantsGroupCaption](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelNavigationItemsVariantSettings.RelatedViewVariantsGroupCaption)

![NavigationContext](~/images/navigationcontext116361.png)

The **ViewVariants** module adds the **View Variants** navigation items for the Views that have predefined View variants. The **Analysis** and **Report** modules add navigation items for business classes associated with existing analysis/report objects.

![NavigationControlContext](~/images/navigationcontrolcontext116362.png)

You can also implement custom context navigation. To see an example, refer to the following help topic: [How to: Implement Custom Context Navigation](xref:113200).