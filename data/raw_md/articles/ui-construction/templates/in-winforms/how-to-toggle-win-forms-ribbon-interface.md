---
uid: "404212"
title: 'How to: Enable the Main Menu Bars or Ribbon in WinForms'
---
# How to: Enable the Main Menu Bars or Ribbon in WinForms

This article describes how to enable the [Ribbon User Interface](xref:2500) in your WinForms application.

> [!tip]
> For the purposes of this article, you can use the **MainDemo** application installed as a part of the XAF package. The default location of the application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\\Components\XAF_.


1. In the **Solution Explorer**, expand the _MainDemo.Win_ project and double-click the _Model.xafml_ file to open it in the [Model Editor](xref:112582).

2. Navigate to the **Options** node. Here you can customize the appearance and behavior of the application's UI.

3. Focus the `FormStyle` property and choose the **Ribbon** option from the drop-down menu.
	
	![Ribbon UI Setup in Model Editor, DevExpress](~/images/xaf-win-form-style-in-model-editor.png)
	
4. Run the application to see the result.

   ![Windows Forms Ribbon UI, DevExpress](~/images/xaf-win-form-style-ribbon.png)
	
> [!TIP]
> You can find additional options for Ribbon UI element customization in the **Options** | **RibbonOptions** node.
