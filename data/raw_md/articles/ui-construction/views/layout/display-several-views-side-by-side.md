---
uid: "113296"
seealso:
- linkId: DevExpress.ExpressApp.DashboardView
- linkId: "113198"
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/xaf/archive/2012/11/07/visiting-dashboards.aspx
  altText: Visiting Dashboards
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/e4916/xaf-how-to-implement-dependent-views-in-a-dashboardview-filter-based-on-selection
  altText: How to implement dependent views in a DashboardView (filter based on selection)
title: 'Display Multiple Views Side-by-Side (Dashboard View)'
---
# Display Multiple Views Side-by-Side (Dashboard View)

This topic explains how to display multiple [Views](xref:112611) side-by-side on a single screen within a [Dashboard View](xref:DevExpress.ExpressApp.DashboardView). The Dashboard View can show any number of unrelated Views in a single [Frame](xref:112608). 

![|XAF Dashboard View|](~/images/dashboard1116788.png)

## Create a Dashboard View

### Add a Dashboard View

Open the [Model Editor](xref:112582) for the `MySolution.Module` project (or for a platform-specific module). Right-click the **Views** node and add a [Dashboard View](xref:DevExpress.ExpressApp.DashboardView).

![XAF add Dashboard View](~/images/dashboardtutorial1116789.png)

Set the View's **Id** property to **MyDashboardView**.

![XAF add Dashboard View](~/images/dashboardtutorial1_1116791.png)

### Specify the Views to Be Displayed on the Dashboard View

The Dashboard View displays inner Views within the [Dashboard View Items](#available-dashboard-view-items).

Right-click the **Items** node and add a Dashboard View Item.

![XAF add Dashboard View Item](~/images/dashboardtutorial2116790.png)

Use the **View** property to select a View displayed within the newly created Dashboard View Item. Specify the Dashboard View Item's **Id**.

![XAF add Dashboard View Item](~/images/dashboardtutorial2_1116792.png)

Repeat the steps above to add another Dashboard View Item.


### Configure the Dashboard View Layout

Configure the Dashboard View layout as you like. For a thorough explanation of how to customize a View layout, refer to the following topic: [View Items Layout Customization](xref:112817).

![XAF Dashboard View Change Layout](~/images/dashboardtutorial3116795.png)

### Create a Navigation Item

Create a Navigation Item to allow users to invoke the Dashboard View. In the Model Editor, right-click the **NavigationItems | Items** node and add a Navigation Item.

![XAF Dashboard View Navigation Item](~/images/dashboardtutorial4116796.png)

Set the **Id** and **View** properties to **MyDashboardView**.

![XAF Dashboard View Navigation Item](~/images/dashboardtutorial4_1116797.png)

Run the application, and open the "MyDashboardView" item to see the newly created Dashboard View in action.

![|XAF dashboard view blazor|](~/images/dashboard-tutorial-result.png)

## Available Dashboard View Items

The Dashboard View supports the following View Item types:

- [Views](xref:112611)
- [Images](xref:DevExpress.ExpressApp.Editors.StaticImage)
- [Blocks of text](xref:DevExpress.ExpressApp.Editors.StaticText)
- [Action Containers](xref:DevExpress.ExpressApp.Editors.ActionContainerViewItem)
