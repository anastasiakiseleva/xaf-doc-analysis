---
uid: "112609"
seealso:
- linkId: "112696"
title: Templates
owner: Ekaterina Kiseleva
---
# Templates

Templates define the appearance of [Windows and Frames](xref:112608) in applications. They contain elements like [Action Containers](xref:112610) and a [View](xref:112611) site. Built-in Templates let developers focus on business logic instead of designing a UI from scratch. You can customize or replace default templates as needed.

The XAF includes the following built-in Templates:

- [Blazor Application Templates](xref:403450)
- [WinForms Application Templates](xref:403446)


Refer to the following topic to learn how to customize the default Templates: 

- [Template Customization](xref:112696)


## How It Works

A Template is a control that implements the [](xref:DevExpress.ExpressApp.Templates.IFrameTemplate) or [](xref:DevExpress.ExpressApp.Templates.IWindowTemplate) interface. These interfaces provide methods that specify a Template's Action Containers collection, and assign a View to be displayed. 

The `IWindowTemplate` interface is inherited from the `IFrameTemplate` interface. The difference is that the `IWindowTemplate` interface additionally provides a store for status messages, a Template's caption and a flag indicating whether it should be sizeable. This means that a Template that implements the `IWindowTemplate` interface behaves like a standard form.

The controls that are used to display List and Detail Views support end-user customization. For instance, in WinForms applications, users can customize the layout of toolbars, columns in grid controls, controls in detail forms, etc. All built-in Windows Forms Templates are designed to save these end-user customizations to the [Application Model](xref:112580), so changes made will persist between application runs.