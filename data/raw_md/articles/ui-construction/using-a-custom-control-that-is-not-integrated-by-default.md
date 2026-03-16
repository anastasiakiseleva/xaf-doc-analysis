---
uid: "113610"
seealso: []
title: "How to: Include a Custom UI Control That Is Not Integrated by Default (WinForms and ASP.NET Core Blazor)"
owner: Ekaterina Kiseleva
---
# How to: Include a Custom UI Control That Is Not Integrated by Default (WinForms and ASP.NET Core Blazor)

XAF uses standard and DevExpress controls for all UI elements such as [List Editors](xref:113189), [Property Editors](xref:113014) for default data types, [View Items](xref:112612), [Actions](xref:112622), [Action Containers](xref:112610), Templates, and so on. For scenarios not covered by the built-in XAF UI elements, XAF allows developers to integrate any other DevExpress, standard (Microsoft), and third-party UI controls into Views. This topic groups solutions by popular UI tasks.

These tasks are often performed at a lower framework level and require more knowledge and experience with XAF. This is the same knowledge required if you were to code an app without our framework. XAF-related benefits and time savings are minimal for those who want to integrate custom controls. As a rule of thumb, you should first know how to solve and optionally implement your task in a non-XAF app. This makes XAF integration much easier. For more information, refer to the following article: [Advanced UI Customization Tips](https://www.devexpress.com/products/net/application_framework/xaf-considerations-for-newcomers.xml#advanced-ui-customization).

To include a custom UI control that is not integrated by default, implement a [](xref:DevExpress.ExpressApp.Editors.ListEditor), [](xref:DevExpress.ExpressApp.Editors.PropertyEditor), or [](xref:DevExpress.ExpressApp.Editors.ViewItem) that wraps the control and serves as an adapter for the XAF infrastructure. You can also [customize a template](xref:112696) to place the control in a specific location. Refer to the table below for details on the different solutions.

{|
|-

! Task
! Task Details
! Solution&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
|-

| The custom control should visualize a list of business objects (List View).
| The custom control should appear when a user selects a [Navigation](xref:113198) item, executes a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction), or opens a Detail View of the object that contains a nested collection. For example, you can use an image gallery control to display photos, a map control to display a list of addresses as map markers, and so on.
| Implement a **List Editor**.

* [](xref:403258)
* [](xref:112659)
|-

| The custom control should visualize a value returned by a business class property.
| The custom control should appear as a Detail View's [layout](xref:112817) element, or within a grid cell in a List View. For example, you can use a trackbar control to edit a numeric value, a gauge control to display a numeric value as a circular indicator, a PDF viewer control to preview an attached document, etc.
| Implement a **Property Editor**.

* [](xref:402189)
* [](xref:112679)
* [](xref:113015)

|-

| The custom control should visualize complex data that depends on multiple objects or properties or data that is not bound to any business object or property.
| The custom control should appear as a Detail View's or Dashboard View's [layout](xref:112817) element. The control accesses data directly (for example, it should load an object collection using an Object Space, fetch data from a web server, load a local file), uses data from multiple properties of a business object, or displays static content.
| Implement a **View Item**.

* [](xref:405483)
* [](xref:113653)
* [](xref:113652)
* [Create an ASP.NET Core Blazor-Specific View Item](xref:113653#create-an-aspnet-core-blazor-specific-view-item)
* [](xref:404698)
* [](xref:404700)
* [](xref:114159)
|-

| The custom control should be added to the application window outside the View area.
| &nbsp;
| Create a custom **Template** and drop the control on it.

* [](xref:403452)
* [](xref:112618)
|-

| The custom control should be added to the main or navigation menu.
| Standard Action types do not cover the scenario or cannot be [customized](xref:113183) using the existing API.
| Create a custom **Action type**.

* [How to: Implement a Custom Action Type (Blazor)](https://github.com/DevExpress-Examples/xaf-custom-action-type-blazor)
* [How to: Create a Custom Action Type with a Custom Control (BarCheckItem) in WinForms](https://github.com/DevExpress-Examples/xaf-win-custom-action-with-custom-action-control)
|-

| An XAF application displays a fully custom non-XAF form.
| You can design a custom form or user control in Visual Studio and add it to your XAF application. In most cases, you can create a [Controller](xref:112621) and show the form on an [Action](xref:112622)'s `Execute` event.
| Show a custom **form**.

* [Blazor - How to show a fully custom non-XAF web page (with custom controls, JavaScript, Razor components, etc.)](https://supportcenter.devexpress.com/ticket/details/t939883/blazor-how-to-show-a-fully-custom-non-xaf-web-page-with-custom-controls-javascript-razor)
* [](xref:118222)
* [](xref:118165)
* [](xref:114159)
* [](xref:404698)
* [](xref:404700)
* [](xref:118240)
* [](xref:112803)


|}

