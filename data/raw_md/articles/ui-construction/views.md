---
uid: "112611"
seealso:
- linkId: "112803"
- linkId: "113011"
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/xaf/archive/2011/03/04/one-more-dive-into-the-xaf-views-structure.aspx
  altText: One more dive into the XAF Views Structure
title: Views
owner: Vera Ulitina
---
# Views

XAF automatically generates Views as [a part of the UI](xref:112607) and uses them to show objects. Views have access to a specified data store and allow end-users to browse and edit data. XAF uses three main View types which are [](xref:DevExpress.ExpressApp.View) class descendants: a Detail View, List View, and Dashboard View. This topic describes the View types and how to access and customize them.

## Composite View and Object View
The [](xref:DevExpress.ExpressApp.CompositeView) class specifies the Composite View, which contains [View Items](xref:112612). Composite Views store View Items in the [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection.

XAF has two actual Composite View types - the [](xref:DevExpress.ExpressApp.DashboardView) and [](xref:DevExpress.ExpressApp.DetailView). The [](xref:DevExpress.ExpressApp.ListView) class also derives from the **CompositeView**, but it does not support the View Items' layout.

![Views](~/images/views132313.png)

The [](xref:DevExpress.ExpressApp.ObjectView) class (a **CompositeView** descendant) specifies the Object View and has the **DetailView** and the **ListView** sub-types. The **ObjectView** and its descendants are bound to data directly - to a single data object, or an object collection.

## Detail View

ASP.NET Core Blazor
:   ![A Detail View in an XAF ASP.NET Core Blazor application](~/images/views_detailview_blazor.png)
Windows Forms
:   ![A Detail View in an XAF Windows Forms application](~/images/views_detailview_win132339.png)

The [](xref:DevExpress.ExpressApp.DetailView) class specifies the Detail View. A Detail View displays a particular business class object. You can access this object in code using the [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) property.

A Detail View uses platform-specific data-oriented [Property Editors](xref:113014) and [View Items](xref:112612) to display persistent and non-persistent data, respectively.

## List View

ASP.NET Core Blazor
:   ![ List View in Blazor UI application](~/images/views_listview_blazor.png)
Windows Forms
:   ![A List View in a WinForms application](~/images/views_listview_win132343.png)

The [](xref:DevExpress.ExpressApp.ListView) class defines a List View. A List View displays a collection of objects of the same class using a [](xref:DevExpress.ExpressApp.CollectionSourceBase) class descendant.

List Views use [List Editors](xref:113189) (see [](xref:DevExpress.ExpressApp.Editors.ListEditor)) to show data. XAF creates a List Editor's control before displaying a List View. The default controls are:
- **GridControl** in Windows Forms applications.
- **DXGrid** in Blazor UI applications.

Refer to the [List View Column Generation](xref:113285) topic to learn how XAF generates columns for List Views.

XAF has a special List View type - the Lookup List View. The Lookup List View is displayed in Lookup Property Editors or pop-up windows and contains fewer columns than the regular List View. You can use a regular List View as a Lookup List View and vice versa. 

## Dashboard View

Windows Forms
:   ![A Dashboard View in a WinForms application](~/images/views_dashboardview_win132346.png)
ASP.NET Core Blazor
:   ![A Dashboard View in a Blazor UI application](~/images/views-dashboard-blazor.png)

The [](xref:DevExpress.ExpressApp.DashboardView) class defines Dashboard Views. They are not bound to data directly and display several Views side-by-side in a single [Frame](xref:112608). These embedded Views reside within [](xref:DevExpress.ExpressApp.Editors.DashboardViewItem) objects. XAF creates a nested Frame for each **DashboardViewItem** before displaying a Dashboard View. These Frames show the **DashboardViewItem**s' Views. 

Dashboard Views can also display custom or built-in [View Items](xref:112612) (for example, [](xref:DevExpress.ExpressApp.Editors.StaticText) or [](xref:DevExpress.ExpressApp.Editors.StaticImage)).

## Customize Views
You can customize Views in your application, for example, change the editor's layout in a Detail View, or a column's visibility in a List View, using one of the following approaches:

* **Customize Views in the Model Editor**

    You can access and configure the [Application Model](xref:112580)'s **Views** node in the [Model Editor](xref:112582) at design time and runtime. The topics below describe how to do this:

    [](xref:403217)

    [](xref:113679)

    [](xref:112817)

    [Display a Detail View with a List View](xref:404203)

    [Filter List Views](xref:403238)

    [How to: Display Several Views Side-by-Side](xref:113296)

    [List View Columns Customization](xref:113679)

    [List View Edit Modes](xref:113249)
* **Customize Views at Runtime**

    The following topics describe how end-users can customize their views: 

    [Default Runtime Customization](xref:2307)

    [End-User Capabilities](xref:833)

    [List View Columns Customization](xref:113679)

    [](xref:112817#runtime-customization)

    [](xref:404353)
* **Access and Customize Views in Code**

    You can customize Views in code by creating a [Controller](xref:112621) and changing the [](xref:DevExpress.ExpressApp.View) class descendants' properties. Refer to the following articles for more information:

    [](xref:402154)
    
    [Access and Customize View Items in Code](xref:112612#access-and-customize-view-items-in-code)
    
    [Access the Application Model in Code](xref:112810)
    
    [Customize Controllers and Actions](xref:112676)
    
    [Data Types Supported by built-in Editors](xref:113014)
    
    [How to: Customize Action Controls](xref:113183)

    [How to: Detect a Lookup List View in Code](xref:112908)
    
    [](xref:113610)
    
    [Ways to Show a Confirmation Dialog](xref:118240)

    [XAF - How to show filter dialog before a List View](https://github.com/DevExpress-Examples/XAF_how-to-show-filter-dialog-before-listview)
